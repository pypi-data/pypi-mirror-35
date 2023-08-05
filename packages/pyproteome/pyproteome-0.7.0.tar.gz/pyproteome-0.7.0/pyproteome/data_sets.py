"""
This module provides functionality for manipulating proteomics data sets.

Functionality includes merging data sets and interfacing with attributes in a
structured format.
"""

# Built-ins
from __future__ import absolute_import, division

from collections import OrderedDict
import copy
import logging
import os
import warnings
from itertools import chain
from functools import partial

# Core data analysis libraries
import pandas as pd
import numpy as np
import numpy.ma as ma
from scipy.stats import ttest_ind, pearsonr, spearmanr

from . import levels, loading, modification, paths, protein, sequence, utils
from .motifs import motif as pymotif


LOGGER = logging.getLogger("pyproteome.data_sets")
DEFAULT_FILTER_BAD = dict(
    ion_score=15,
    isolation=50,
    median_quant=1000,
    q=0.05,
)
DATA_SET_COLS = [
    "Proteins",
    "Sequence",
    "Modifications",
    "Validated",
    "Confidence Level",
    "Ion Score",
    "q-value",
    "Isolation Interference",
    "Missed Cleavages",
    "Ambiguous",
    "Charges",
    "Masses",
    "RTs",
    "Intensities",
    "Raw Paths",
    "Scan Paths",
    "Scan",
]


class DataSet:
    """
    Class that encompasses a proteomics data set.

    Includes peptide list, scan list, channels, groups, etc.

    Attributes
    ----------
    search_name : str, optional
    psms : :class:`pandas.DataFrame`
        Contains at least "Proteins", "Sequence", and "Modifications" columns.
    channels : dict of str, str
        Maps label channel to sample name.
    groups : dict of str, list of str
        Maps groups to list of sample names. The primary group is considered
        as the first in this sequence.
    cmp_groups : list of list of str
    name : str
    levels : dict or str, float, optional
    sets : int
        Number of sets merged into this data set.
    """
    def __init__(
        self,
        name="",
        search_name=None,
        channels=None,
        groups=None,
        cmp_groups=None,
        lvls=None,
        dropna=False,
        pick_best_ptm=True,
        merge_duplicates=True,
        filter_bad=True,
        check_raw=True,
        log_stats=True,
        load=True,
    ):
        """
        Initializes a data set.

        Parameters
        ----------
        name : str, optional
        search_name : str, optional
            Read psms from MASCOT / Discoverer data files.
        channels : dict of (str, str), optional
            Ordered dictionary mapping sample names to quantification channels
            (i.e. {"X": "126", "Y": "127", "Z": "128", "W": "129"})
        groups : dict of str, list of str, optional
            Ordered dictionary mapping sample names to larger groups
            (i.e. {"WT": ["X", "Y"], "Diseased": ["W", "Z"]})
        lvls : dict or str, float, optional
        dropna : bool, optional
            Drop scans that have any channels with missing quantification
            values.
        pick_best_ptm : bool, optional
            Select the peptide sequence for each scan that has the highest
            MASCOT ion score. (i.e. ["pSTY": 5, "SpTY": 10, "STpY": 20] =>
            "STpY")
        merge_duplicates : bool, optional
            Merge scans that have the same peptide sequence into one peptide,
            summing the quantification channel intensities to give a weighted
            estimate of relative abundances.
        filter_bad : bool or dict, optional
            Remove peptides that do not have a "High" confidence score from
            ProteomeDiscoverer.
        log_stats : bool, optional
        load : bool, optional
        """
        if search_name is None:
            search_name = name

        if search_name and os.path.splitext(search_name)[1] == "":
            search_name += ".msf"

        self.channels = channels or OrderedDict()
        self.groups = groups or OrderedDict()
        self.cmp_groups = cmp_groups or None
        self.group_a, self.group_b = None, None

        species, lst = set(), []

        if search_name and load:
            self.psms, species, lst = loading.load_mascot_psms(
                search_name,
                pick_best_ptm=pick_best_ptm,
            )
            for col in DATA_SET_COLS:
                assert col in self.psms.columns
        else:
            self.psms = pd.DataFrame(
                columns=DATA_SET_COLS + list(self.channels.values()),
            )

        self.name = name
        self.levels = lvls
        self.search_name = search_name
        self.species = species

        self.intra_normalized = False
        self.sets = 1

        if check_raw:
            self.check_raw()

        if dropna:
            LOGGER.info(
                "{}: Dropping channels with NaN values.".format(self.name)
            )
            self.dropna(inplace=True)

        if filter_bad is True:
            filter_bad = DEFAULT_FILTER_BAD.copy()

            if pd.isnull(self.psms["q-value"]).all() and "q" in filter_bad:
                del filter_bad["q"]

            if pd.isnull(self.psms[list(self.channels.values())]).all().all():
                del filter_bad["median_quant"]

        if log_stats:
            self.log_stats()

        if filter_bad:
            LOGGER.info(
                "{}: Filtering peptides using: {}"
                .format(self.name, filter_bad)
            )
            self.filter(
                filter_bad,
                inplace=True,
            )

        if pick_best_ptm and (
            not search_name or
            os.path.splitext(search_name)[1] != ".msf" or
            any(i for i in lst)
        ):
            LOGGER.info(
                "{}: Picking peptides with best ion score for each scan."
                .format(self.name)
            )
            self._pick_best_ptm()

        if merge_duplicates:
            LOGGER.info(
                "{}: Merging duplicate peptide hits together."
                .format(self.name)
            )
            self.merge_duplicates(inplace=True)

        if cmp_groups:
            self.norm_cmp_groups(cmp_groups, inplace=True)

        self.update_group_changes()

        if log_stats:
            self.log_stats()

    def copy(self):
        """
        Make a copy of self.

        Returns
        -------
        :class:`DataSet<pyproteome.data_sets.DataSet>`
        """
        new = copy.copy(self)

        new.psms = new.psms.copy()
        new.channels = new.channels.copy()
        new.groups = new.groups.copy()
        new.species = new.species.copy()

        return new

    @property
    def samples(self):
        return list(self.channels.keys())

    def __str__(self):
        return (
            "<pyproteome.DataSet object" +
            (
                ": " + self.name
                if self.name else
                " at " + hex(id(self))
            ) +
            ">"
        )

    def __getitem__(self, key):
        if isinstance(key, slice):
            new = self.copy()
            new.psms = new.psms[key]
            return new

        if any(
            isinstance(key, i)
            for i in [str, list, set, tuple, pd.Series, np.ndarray]
        ):
            return self.psms[key]

        raise TypeError(type(key))

    @property
    def shape(self):
        return self.psms.shape

    def _pick_best_ptm(self):
        reject_mask = np.zeros(self.shape[0], dtype=bool)

        for index, row in self.psms.iterrows():
            hits = np.logical_and(
                self.psms["Scan"] == row["Scan"],
                self.psms["Sequence"] != row["Sequence"],
            )

            if "Rank" in self.psms.columns:
                better = self.psms["Rank"] < row["Rank"]
            else:
                better = self.psms["Ion Score"] > row["Ion Score"]

            hits = np.logical_and(hits, better)

            if hits.any():
                reject_mask[index] = True

        self.psms = self.psms[~reject_mask].reset_index(drop=True)

    def merge_duplicates(self, inplace=False):
        """
        Merge together all duplicate peptides. New quantification values are
        calculated from a weighted sum of each channel's values.

        Parameters
        ----------
        inplace : bool, optional
            Modify the data set in place, otherwise create a copy and return
            the new object.

        Returns
        -------
        :class:`DataSet<pyproteome.data_sets.DataSet>`
        """
        new = self

        if not inplace:
            new = new.copy()

        if len(new.psms) < 1:
            return

        channels = list(new.channels.values())
        agg_dict = {}

        for channel in channels:
            weight = "{}_weight".format(channel)

            if weight in new.psms.columns:
                new.psms[channel] *= new.psms[weight]
                agg_dict[weight] = _nan_sum

            agg_dict[channel] = _nan_sum

        def _first(x):
            if not all(i == x.values[0] for i in x.values):
                LOGGER.warning(
                    "{}: Mismatch between peptide data: '{}' not in {}"
                    .format(
                        new.name,
                        x.values[0],
                        [str(i) for i in x.values[1:]],
                    )
                )

            return x.values[0]

        agg_dict["Proteins"] = _first
        agg_dict["Modifications"] = _first
        agg_dict["Missed Cleavages"] = _first
        agg_dict["Validated"] = all

        agg_dict["Scan Paths"] = utils.flatten_set
        agg_dict["Raw Paths"] = utils.flatten_set

        agg_dict["Ambiguous"] = all

        agg_dict["Masses"] = utils.flatten_set
        agg_dict["Charges"] = utils.flatten_set
        agg_dict["Intensities"] = utils.flatten_set
        agg_dict["RTs"] = utils.flatten_set

        agg_dict["Scan"] = utils.flatten_set
        agg_dict["Ion Score"] = max
        agg_dict["q-value"] = min
        agg_dict["Confidence Level"] = partial(
            max,
            key=lambda x: ["Low", "Medium", "High"].index(x),
        )
        agg_dict["Isolation Interference"] = min

        new.psms = new.psms.groupby(
            by=[
                "Sequence",
            ],
            sort=False,
            as_index=False,
        ).agg(agg_dict)

        for channel in channels:
            weight = "{}_weight".format(channel)

            if weight in new.psms.columns:
                new.psms[channel] = (
                    new.psms[channel] / new.psms[weight]
                )

        new.psms = new.psms.reset_index(drop=True)

        return new

    def merge_subsequences(self, inplace=False):
        """
        Merges petides that are a subsequence of another peptide.

        Only merges peptides that contain the same set of modifications and
        that map to the same protein(s).
        """
        new = self

        if not inplace:
            new = new.copy()

        # Find all proteins that have more than one peptide mapping to them
        for index, row in new.psms[
            new.psms.duplicated(subset="Proteins", keep=False)
        ].iterrows():
            seq = row["Sequence"]

            # Then iterate over each peptide and find other non-identical
            # peptides that map to the same protein
            for o_index, o_row in new.psms[
                np.logical_and(
                    new.psms["Proteins"] == row["Proteins"],
                    new.psms["Sequence"] != seq,
                )
            ].iterrows():
                # If that other peptide is a subset of this peptide, rename it
                if o_row["Sequence"] in seq:
                    cols = [
                        "Sequence",
                        "Modifications",
                        "Missed Cleavages",
                    ]
                    new.psms.at[o_index, cols] = row[cols]

        # And finally group together peptides that were renamed
        return new.merge_duplicates(inplace=inplace)

    def __add__(self, other):
        """
        Concatenate two data sets.

        Combines two data sets, adding together the channel values for any
        common data.

        Parameters
        ----------
        other : :class:`DataSet<pyproteome.data_sets.DataSet>`

        Returns
        -------
        :class:`DataSet<pyproteome.data_sets.DataSet>`
        """
        return merge_data([self, other])

    def rename_channels(self, inplace=False):
        """
        Rename all channels from quantification channel name to sample name.
        (i.e. "126" => "Mouse 1337")

        Parameters
        ----------
        inplace : bool, optional
        """
        new = self

        if not inplace:
            new = new.copy()

        for new_channel, old_channel in new.channels.items():
            if new_channel != old_channel:
                new_weight = "{}_weight".format(new_channel)

                if (
                    new_channel in new.psms.columns or
                    new_weight in new.psms.columns
                ):
                    raise Exception(
                        "Channel {} already exists, cannot rename to it"
                        .format(new_channel)
                    )

                new.psms[new_channel] = new.psms[old_channel]
                del new.psms[old_channel]

                old_weight = "{}_weight".format(old_channel)

                if old_weight in new.psms.columns:
                    new.psms[new_weight] = new.psms[old_weight]
                    del new.psms[old_weight]

        new.channels = OrderedDict([
            (key, key) for key in new.channels.keys()
        ])

        return new

    def inter_normalize(self, norm_channels=None, other=None, inplace=False):
        """
        Normalize runs to one channel for inter-run comparions.

        Parameters
        ----------
        norm_channels : list of str, optional
        other : :class:`DataSet<pyproteome.data_sets.DataSet>`, optional
        inplace : bool, optional
            Modify this data set in place.

        Returns
        -------
        :class:`DataSet<pyproteome.data_sets.DataSet>`
        """
        assert (
            norm_channels is not None or
            other is not None
        )

        new = self

        if not inplace:
            new = new.copy()

        new = new.rename_channels(inplace=inplace)

        if norm_channels is None:
            norm_channels = set(new.channels).intersection(other.channels)

        if len(norm_channels) == 0:
            return new

        # Filter norm channels to include only those in other data set
        norm_channels = [
            chan
            for chan in norm_channels
            if not other or chan in other.channels
        ]
        for channel in new.channels.values():
            weight = "{}_weight".format(channel)

            if weight not in new.psms.columns:
                new.psms[weight] = (
                    new.psms[channel] *
                    (100 - new.psms["Isolation Interference"]) / 100
                )

        # Calculate the mean normalization signal from each shared channel
        new_mean = new.psms[norm_channels].mean(axis=1)

        # Drop values for which there is no normalization data
        new.psms = new.psms[~new_mean.isnull()].reset_index(drop=True)

        if other:
            merge = pd.merge(
                new.psms,
                other.psms,
                on=[
                    "Proteins",
                    "Sequence",
                    "Modifications",
                ],
                how="left",
                suffixes=("_self", "_other"),
            )
            assert merge.shape[0] == new.shape[0]

            self_mean = merge[
                ["{}_self".format(i) for i in norm_channels]
            ].mean(axis=1)

            other_mean = merge[
                ["{}_other".format(i) for i in norm_channels]
            ].mean(axis=1)

            for channel in new.channels.values():
                vals = merge[
                    channel
                    if channel in merge.columns else
                    "{}_self".format(channel)
                ]

                # Set scaling factor to 1 where other_mean is None
                cp = other_mean.copy()
                cp[other_mean.isnull()] = (
                    self_mean[other_mean.isnull()]
                )

                if self_mean.any():
                    vals *= cp / self_mean

                assert new.shape[0] == vals.shape[0]
                new.psms[channel] = vals

        new.update_group_changes()

        return new

    def normalize(self, lvls, inplace=False):
        """
        Normalize channels to given levels for intra-run comparisons.

        Divides all channel values by a given level.

        Parameters
        ----------
        lvls : dict of str, float or
        :class:`DataSet<pyproteome.data_sets.DataSet>`
            Mapping of channel names to normalized levels. Alternatively,
            a data set to pass to levels.get_channel_levels() or use
            pre-calculated levels from.
        inplace : bool, optional
            Modify this data set in place.

        Returns
        -------
        :class:`DataSet<pyproteome.data_sets.DataSet>`
        """
        new = self

        # Don't normalize a data set twice!
        assert not new.intra_normalized

        if not inplace:
            new = new.copy()

        if hasattr(lvls, "levels"):
            if not lvls.levels:
                lvls.levels = levels.get_channel_levels(lvls)

            lvls = lvls.levels

        new_channels = utils.norm(self.channels)

        for key, norm_key in zip(
            self.channels.values(),
            new_channels.values(),
        ):
            new.psms[norm_key] = new.psms[key] / lvls[key]
            del new.psms[key]

        new.intra_normalized = True
        new.channels = new_channels
        new.groups = self.groups.copy()

        new.update_group_changes()

        return new

    def check_raw(self):
        """
        Checks that all raw files referenced in search data can be found in
        paths.MS_RAW_DIR

        Returns
        -------
        found_all : bool
        """
        try:
            raw_dir = [
                i.lower()
                for i in os.listdir(paths.MS_RAW_DIR)
            ]
        except OSError:
            raw_dir = []

        found_all = True

        for raw in utils.flatten_set(
            row["Raw Paths"]
            for _, row in self.psms.iterrows()
        ):
            if raw.lower() not in raw_dir:
                LOGGER.warning(
                    "{}: Unable to locate raw file for {}"
                    .format(self.name, raw)
                )
                found_all = False

        return found_all

    def dropna(
        self,
        columns=None,
        how=None,
        thresh=None,
        groups=None,
        inplace=False,
    ):
        """
        Drop any channels with NaN values.

        Parameters
        ----------
        columns : list of str, optional
        how : str, optional
        groups : list of str, optional
            Only drop rows with NaN in columns within groups.
        inplace : bool, optional

        Returns
        -------
        :class:`DataSet<pyproteome.data_sets.DataSet>`
        """
        new = self

        if not inplace:
            new = new.copy()

        if columns is None:
            columns = list(new.channels.values())

        if how is None and thresh is None:
            how = "any"

        if groups is not None:
            columns = [
                new.channels[col]
                for group in groups
                for col in new.groups[group]
                if col in new.channels
            ]

        new.psms = new.psms.dropna(
            axis=0,
            how=how,
            thresh=thresh,
            subset=columns,
        ).reset_index(drop=True)

        return new

    def add_peptide(self, insert):
        defaults = {
            "Proteins": protein.Proteins(),
            "Sequence": sequence.Sequence(),
            "Modifications": modification.Modifications(),
            "Validated": False,
            "Confidence Level": "High",
            "Ion Score": 100,
            "q-value": 0,
            "Isolation Interference": 0,
            "Missed Cleavages": 0,
            "Ambiguous": False,
            "Charges": set(),
            "Masses": set(),
            "RTs": set(),
            "Intensities": set(),
            "Raw Paths": set(),
            "Scan Paths": set(),
            "Scan": set(),
        }

        for key, val in defaults.items():
            if key not in insert:
                insert[key] = val

        for col in DATA_SET_COLS:
            assert col in insert

        self.psms = self.psms.append(pd.Series(insert), ignore_index=True)

    def filter(
        self,
        filters=None,
        inplace=False,
        **kwargs
    ):
        """
        Filters a data set.

        Parameters
        ----------
        filters : list of dict or dict, optional
            List of filters to apply to data set. Filters are also pulled from
            `kwargs` (see below).
        inplace : bool, optional
            Perform the filter on self, other create a copy and return the
            new object.

        Notes
        -----
        These parameters filter your data set to only include peptides that
        match a given attribute. For example::

            >>> data.filter(mod="Y", p=0.01, fold=2)

        This function interprets both the argument filter and python `kwargs`
        magic. The three functions are all equivalent::

            >>> data.filter(p=0.01)
            >>> data.filter([{"p": 0.01}])
            >>> data.filter({"p": 0.01})

        Filter parameters can be one of any below:

        ================    ===================================================
        Name                Description
        ================    ===================================================
        series              Use a pandas series (data.psms[series]).
        fn                  Use data.psms.apply(fn).
        group_a             Calculate p / fold change values from group_a.
        group_b             Calculate p / fold change values from group_b.
        ambiguous           Include peptides with ambiguous PTMs if true,
                            filter them out if false.
        confidence          Discoverer's peptide confidence (High|Medium|Low).
        ion_score           MASCOT's ion score.
        isolation           Discoverer's isolation inference.
        missed_cleavage     Missed cleaves <= cutoff.
        median_quant        Median quantification signal > cutoff.
        p                   p-value < cutoff.
        q                   q-value < cutoff.
        asym_fold           Change > val if cutoff > 1 else Change < val.
        fold                Change > cutoff or Change < 1 / cutoff.
        motif               Filter for motif.
        protein             Filter for protein or list of proteins.
        sequence            Filter for sequence or list of sequences.
        mod                 Filter for modifications.
        only_validated      Use rows validated by CAMV.
        inverse             Use all rows that are rejected by a filter.
        rename              Change the new data sets name to a new value.
        ================    ===================================================

        Returns
        -------
        :class:`DataSet<pyproteome.data_sets.DataSet>`
        """
        new = self

        if filters is None:
            filters = []

        if filters and not isinstance(filters, (list, tuple)):
            filters = [filters]

        if kwargs:
            filters += [kwargs]

        if not inplace:
            new = new.copy()

        confidence = {
            "High": ["High"],
            "Medium": ["Medium", "High"],
            "Low": ["Low", "Medium", "High"],
        }

        fns = {
            "series": lambda val, psms:
            val,

            "fn": lambda val, psms:
            psms.apply(val, axis=1),

            "ambiguous": lambda val, psms:
            psms["Ambiguous"] == val,

            "confidence": lambda val, psms:
            psms["Confidence Level"].isin(confidence[val]),

            "ion_score": lambda val, psms:
            psms["Ion Score"] >= val,

            "isolation": lambda val, psms:
            psms["Isolation Interference"] <= val,

            "missed_cleavage": lambda val, psms:
            psms["Missed Cleavages"] <= val,

            "median_quant": lambda val, psms:
            np.nan_to_num(
                np.nanmedian(
                    psms[
                        [chan for chan in new.channels.values()]
                    ],
                    axis=1,
                )
            ) >= val,

            "p": lambda val, psms:
            (~psms["p-value"].isnull()) &
            (psms["p-value"] <= val),

            "q": lambda val, psms:
            (~psms["q-value"].isnull()) &
            (psms["q-value"] <= val),

            "asym_fold": lambda val, psms:
            (~psms["Fold Change"].isnull()) &
            (
                psms["Fold Change"] >= val
                if val > 1 else
                psms["Fold Change"] <= val
            ),

            "fold": lambda val, psms:
            (~psms["Fold Change"].isnull()) &
            (
                psms["Fold Change"].apply(
                    lambda x:
                    x if x > 1 else (1 / x if x else x)
                ) >= (val if val > 1 else 1 / val)
            ),

            "motif": lambda val, psms:
            psms["Sequence"].apply(
                lambda x:
                any(
                    val.match(nmer)
                    for nmer in pymotif.generate_n_mers(
                        x,
                        letter_mod_types=f.get("mod", None),
                    )
                )
            ),

            "protein": lambda val, psms:
            psms["Proteins"].apply(
                lambda x: bool(set(val).intersection(x.genes))
            )
            if isinstance(val, (list, set, tuple, pd.Series)) else
            psms["Proteins"] == val,

            "sequence": lambda val, psms:
            psms["Sequence"].apply(lambda x: any(i in x for i in val))
            if isinstance(val, (list, set, tuple, pd.Series)) else
            psms["Sequence"] == val,

            "mod": lambda val, psms:
            psms["Modifications"].apply(
                lambda x: bool(list(x.get_mods(val).skip_labels()))
            ),

            "only_validated": lambda val, psms:

            psms["Validated"] == val,

            "scan_paths": lambda val, psms:
            psms["Scan Paths"]
            .apply(lambda x: any(i in val for i in x))
        }

        with warnings.catch_warnings():
            warnings.filterwarnings(
                'ignore',
                r'All-NaN (slice|axis) encountered',
            )

            for f in filters:
                group_a = f.pop("group_a", None)
                group_b = f.pop("group_b", None)

                if group_a or group_b:
                    new.update_group_changes(
                        group_a=group_a,
                        group_b=group_b,
                    )

                inverse = f.pop("inverse", False)
                rename = f.pop("rename", None)

                if rename is not None:
                    new.name = rename

                for key, val in f.items():
                    # Skip filtering if psms is empty (fixes pandas type error)
                    if new.shape[0] < 1:
                        continue

                    mask = fns[key](val, new.psms)

                    if inverse:
                        mask = ~mask

                    assert mask.shape[0] == new.shape[0]

                    new.psms = new.psms.loc[mask].reset_index(drop=True)

        new.psms.reset_index(inplace=True, drop=True)

        return new

    def get_groups(self, group_a=None, group_b=None):
        """
        Get channels associated with two groups.

        Parameters
        ----------
        group_a : str or list of str, optional
        group_b : str or list of str, optional

        Returns
        -------
        samples : list of str
        labels : list of str
        groups : tuple of (str or list of str)
        """
        groups = [
            val
            for key, val in self.groups.items()
            if any(chan in self.channels for chan in val)
        ]
        labels = [
            key
            for key, val in self.groups.items()
            if any(chan in self.channels for chan in val)
        ]

        group_a = group_a or self.group_a
        group_b = group_b or self.group_b

        if group_a is None:
            label_a = labels[0] if labels else None
            samples_a = groups[0] if groups else []
        elif isinstance(group_a, str):
            label_a = group_a
            samples_a = self.groups[group_a]
        else:
            group_a = [
                group
                for group in group_a
                if any(
                    sample in self.channels
                    for sample in self.groups[group]
                )
            ]
            label_a = ", ".join(group_a)
            samples_a = [
                sample
                for i in group_a
                for sample in self.groups[i]
                if sample in self.channels
            ]

        if group_b is None:
            label_b = labels[1] if labels[1:] else None
            samples_b = groups[1] if groups[1:] else []
        elif isinstance(group_b, str):
            label_b = group_b
            samples_b = self.groups[group_b]
        else:
            group_b = [
                group
                for group in group_b
                if any(
                    sample in self.channels
                    for sample in self.groups[group]
                )
            ]
            label_b = ", ".join(group_b)
            samples_b = [
                sample
                for i in group_b
                for sample in self.groups[i]
                if sample in self.channels
            ]

        return (samples_a, samples_b), (label_a, label_b), (group_a, group_b)

    def update_group_changes(self, group_a=None, group_b=None):
        """
        Update a table's Fold-Change, and p-value columns.

        Values are calculated based on changes between group_a and group_b.

        Parameters
        ----------
        psms : :class:`pandas.DataFrame`
        group_a : str or list of str, optional
        group_b : str or list of str, optional
        """
        (group_a, group_b), _, (self.group_a, self.group_b) = self.get_groups(
            group_a=group_a,
            group_b=group_b,
        )

        channels_a = [
            self.channels[i]
            for i in group_a
            if i in self.channels
        ]

        channels_b = [
            self.channels[i]
            for i in group_b
            if i in self.channels
        ]

        if channels_a and channels_b and self.shape[0] > 0:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                self.psms["Fold Change"] = pd.Series(
                    np.nanmean(self.psms[channels_a], axis=1) /
                    np.nanmean(self.psms[channels_b], axis=1),
                    index=self.psms.index,
                )

                pvals = ttest_ind(
                    self.psms[channels_a],
                    self.psms[channels_b],
                    axis=1,
                    nan_policy="omit",
                )[1]

                if ma.is_masked(pvals):
                    pvals = ma.fix_invalid(pvals, fill_value=np.nan)
                elif isinstance(pvals, float):
                    pvals = [pvals]
                elif pvals.shape == ():
                    pvals = [pvals]

                self.psms["p-value"] = pd.Series(pvals, index=self.psms.index)
        else:
            self.psms["Fold Change"] = np.nan
            self.psms["p-value"] = np.nan

    def norm_cmp_groups(self, cmp_groups, inplace=False):
        """
        Normalize between groups in a list. This can be used to compare data
        sets that have comparable control groups.

        Channnels within each list of groups are normalized to the mean of the
        group's channels.

        Parameters
        ----------
        cmp_gorups : list of list of str
            List of groups to be normalized to each other.
            i.e. [["CK-p25 Hip", "CK Hip"], ["CK-p25 Cortex", "CK Cortex"]]
        inplace : bool, optional
            Modify the data set in place, otherwise create a copy and return
            the new object.

        Examples
        --------
        >>> channels = ["a", "b", "c", "d"]
        >>> groups = {i: [i] for i in channels}
        >>> ds = data_sets.DataSet(channels=channels, groups=groups)
        >>> ds.add_peptide({'a': 1000, 'b': 500, 'c': 100, 'd': 25})
        >>> ds = ds.norm_cmp_groups([["a", "b"], ["c", "d"]])
        >>> {i: vals.psms.iloc[0][i] for i in channels}
        {"a": 1, "b": 0.5, "c": 1, "d": .25}

        Returns
        -------
        :class:`DataSet<pyproteome.data_sets.DataSet>`
        """
        new = self

        if not inplace:
            new = new.copy()

        if new.cmp_groups:
            raise Exception("cmp_groups normalization already set")

        new.cmp_groups = [
            tuple(i) for i in cmp_groups
        ]

        # if len(cmp_groups) < 2:
        #     return new

        # assert not any(
        #     group in [
        #         i
        #         for o_groups in cmp_groups[ind + 1:]
        #         for i in o_groups
        #     ]
        #     for ind, groups in enumerate(cmp_groups)
        #     for group in groups
        # )

        for groups in cmp_groups:
            channels = [
                [
                    new.channels[name]
                    for name in new.groups[group]
                    if name in new.channels
                ]
                for group in groups
            ]

            if not any(len(i) > 0 for i in channels):
                continue

            vals = new[
                [chan for chan_group in channels for chan in chan_group]
            ]

            norm_vals = vals[channels[0]].median(axis=1)

            vals = vals.apply(lambda col: col / norm_vals)

            new.psms[
                [chan for chan_group in channels for chan in chan_group]
            ] = vals

        return new

    def log_stats(self):
        data_p = self.filter(mod=[(None, "Phospho")])
        data_pst = self.filter(mod=[("S", "Phospho"), ("T", "Phospho")])
        data_py = self.filter(mod=[("Y", "Phospho")])

        LOGGER.info(
            (
                "{}: {} pY - {} pST ({:.0%} phospho specificity) -"
                " {} total peptides - {} unique proteins"
            ).format(
                self.name,
                len(data_py.psms),
                len(data_pst.psms),
                len(data_p.psms) / max([len(self.psms), 1]),
                len(self.psms),
                len(self.genes),
            )
        )

        per_amb = (
            data_p.filter(ambiguous=True).shape[0] /
            max([data_p.shape[0], 1])
        )

        LOGGER.info(
            (
                "{}: {:.0%} of phosphopeptides have an ambiguous assignment"
            ).format(self.name, per_amb)
        )

        labeled = self.filter(
            fn=lambda x:
            x["Sequence"].is_labeled
        ).shape[0]

        underlabeled = self.filter(
            fn=lambda x:
            x["Sequence"].is_underlabeled
        ).shape[0]

        per_lab = labeled / max([self.shape[0], 1])
        per_under_lab = underlabeled / max([self.shape[0], 1])

        LOGGER.info(
            (
                "{}: {:.0%} labeled - {:.0%} underlabeled"
            ).format(self.name, per_lab, per_under_lab)
        )

        mmc = self.psms["Missed Cleavages"].mean()

        LOGGER.info(
            (
                "{}: {:.1f} mean missed cleavages"
            ).format(self.name, mmc)
        )

    @property
    def genes(self):
        return sorted(
            set(
                gene
                for i in self.psms["Proteins"]
                for gene in i.genes
            )
        )

    @property
    def accessions(self):
        return sorted(
            set(
                gene
                for i in self.psms["Proteins"]
                for gene in i.accessions
            )
        )

    @property
    def data(self):
        """
        Get the raw data corresponding to each channels' intensities for each
        peptide.

        Returns
        -------
        :class:`pandas.DataFrame`
        """
        return self.psms[
            [
                self.channels[chan]
                for group in self.groups.values()
                for chan in group
                if chan in self.channels
            ]
        ]


def load_all_data(
    chan_mapping=None,
    group_mapping=None,
    loaded_fn=None,
    norm_mapping=None,
    merge_mapping=None,
    merged_fn=None,
    kw_mapping=None,
    merge_only=True,
    **kwargs
):
    """
    Parameters
    ----------
    chan_mapping : dict, optional
    group_mapping : dict, optional
    loaded_fn : func, optional
    norm_mapping : dict, optional
    merge_mapping : dict, optional
    """
    chan_mapping = chan_mapping or {}
    group_mapping = group_mapping or {}
    norm_mapping = norm_mapping or {}
    merge_mapping = merge_mapping or {}
    kw_mapping = kw_mapping or {}

    datas = OrderedDict()

    for f in os.listdir(paths.MS_SEARCHED_DIR):
        name, ext = os.path.splitext(f)

        if ext not in [".msf"]:
            continue

        if (
            merge_mapping and
            merge_only and
            name not in utils.flatten_set(list(merge_mapping.values()))
        ):
            continue

        kws = kw_mapping.get(name, {})
        kws.update(kwargs)

        chan = kws.pop("channels", None)
        group = kws.pop("groups", None)

        for key, val in chan_mapping.items():
            if name.startswith(key):
                chan = val
                break

        for key, val in group_mapping.items():
            if name.startswith(key):
                group = val
                break

        datas[name] = DataSet(
            name=name,
            channels=chan,
            groups=group,
            **kws
        )

    if loaded_fn:
        datas = loaded_fn(datas)

    datas, mapped_names = norm_all_data(datas, norm_mapping)
    datas = merge_all_data(
        datas, merge_mapping,
        mapped_names=mapped_names,
        merged_fn=merged_fn,
    )

    return datas


def norm_all_data(datas, norm_mapping):
    mapped_names = OrderedDict()
    datas_new = datas.copy()

    if norm_mapping in ["self"]:
        norm_mapping = {
            name: name
            for name in datas.keys()
            if not name.endswith("-norm")
        }

    for key, val in norm_mapping.items():
        for name, data in datas.items():
            if not name.startswith(key) or name.endswith("-norm"):
                continue

            mapped_names[name] = "{}-norm".format(name)

            datas_new[mapped_names[name]] = data.normalize(datas[val])
            datas_new[mapped_names[name]].name += "-norm"

    return datas_new, mapped_names


def merge_all_data(datas, merge_mapping, mapped_names=None, merged_fn=None):
    datas = datas.copy()

    if mapped_names is None:
        mapped_names = {}

    rmap = {val: key for key, val in mapped_names.items()}

    if merge_mapping:
        for name in datas.keys():
            if not any(
                name in vals or
                rmap.get(name, name) in vals or
                name == key
                for key, vals in merge_mapping.items()
            ):
                LOGGER.warning("Unmerged data: {}".format(name))

    for key, vals in merge_mapping.items():
        if not any([mapped_names.get(val, val) in datas for val in vals]):
            continue

        datas[key] = merge_data(
            [
                datas[mapped_names.get(val, val)]
                for val in vals
                if mapped_names.get(val, val) in datas
            ],
            name=key,
        )

        if merged_fn:
            datas[key] = merged_fn(key, datas[key])

    return datas


def merge_data(
    data_sets,
    name=None,
    norm_channels=None,
    merge_duplicates=True,
):
    """
    Merge a list of data sets together.

    Parameters
    ----------
    data_sets : list of :class:`DataSet<pyproteome.data_sets.DataSet>`
    name : str, optional
    merge_duplicates : bool, optional

    Returns
    -------
    :class:`DataSet<pyproteome.data_sets.DataSet>`
    """
    new = DataSet(
        name=name,
        log_stats=False,
        load=False,
    )

    if len(data_sets) < 1:
        return new

    # if any(not isinstance(data, DataSet) for data in data_sets):
    #     raise TypeError(
    #         "Incompatible types: {}".format(
    #             [type(data) for data in data_sets]
    #         )
    #     )

    for index, data in enumerate(data_sets):
        data = data.rename_channels()

        # Update new.groupss
        for group, samples in data.groups.items():
            if group not in new.groups:
                new.groups[group] = samples
                continue

            new.groups[group] += [
                sample
                for sample in samples
                if sample not in new.groups[group]
            ]

        # Normalize data sets to their common channels
        if len(data_sets) > 1:
            data = data.inter_normalize(
                other=new if index > 0 else None,
                norm_channels=(
                    norm_channels
                    if norm_channels else (
                        set(data.channels).intersection(new.channels)
                        if index > 0 else
                        set(data.channels).intersection(data_sets[1].channels)
                    )
                ),
            )

        for key, val in data.channels.items():
            assert new.channels.get(key, val) == val

            if key not in new.channels:
                new.channels[key] = val

        new.psms = _concat(
            [new.psms, data.psms],
        ).reset_index(drop=True)

        if merge_duplicates:
            new.merge_duplicates(inplace=True)

    new.sets = sum(data.sets for data in data_sets)

    new.group_a = next(
        (i.group_a for i in data_sets if i.group_a is not None),
        None,
    )
    new.group_b = next(
        (i.group_b for i in data_sets if i.group_b is not None),
        None,
    )
    new.cmp_groups = sorted(
        set(
            grp
            for i in data_sets
            if i.cmp_groups is not None
            for grp in i.cmp_groups
        )
    ) or None
    new.species = set(
        species
        for i in data_sets
        for species in i.species
    )

    new.update_group_changes()

    if name:
        new.name = name

    new.log_stats()

    return new


def merge_proteins(ds, inplace=False):
    new = ds

    if not inplace:
        new = new.copy()

    if len(new.psms) < 1:
        return new

    channels = list(new.channels.values())
    agg_dict = {}

    for channel in channels:
        weight = "{}_weight".format(channel)

        if weight in new.psms.columns:
            # XXX: Use weight corresponding to median channel value?
            # (not median weight)
            agg_dict[weight] = _nan_median

        agg_dict[channel] = _nan_median

    def _unfirst(x):
        return x.values[0]

    def _first(x):
        if not all(i == x.values[0] for i in x.values):
            LOGGER.warning(
                "{}: Mismatch between peptide data: '{}' not in {}"
                .format(
                    new.name,
                    x.values[0],
                    [str(i) for i in x.values[1:]],
                )
            )

        return x.values[0]

    agg_dict["Sequence"] = _unfirst
    agg_dict["Modifications"] = _unfirst
    agg_dict["Missed Cleavages"] = _unfirst
    agg_dict["Validated"] = all

    agg_dict["Scan Paths"] = _unfirst
    agg_dict["Raw Paths"] = _unfirst

    agg_dict["Ambiguous"] = _unfirst

    agg_dict["Masses"] = _unfirst
    agg_dict["Charges"] = _unfirst
    agg_dict["Intensities"] = _unfirst
    agg_dict["RTs"] = _unfirst

    agg_dict["Scan"] = _unfirst
    agg_dict["Ion Score"] = max
    agg_dict["q-value"] = min
    agg_dict["Confidence Level"] = partial(
        max,
        key=lambda x: ["Low", "Medium", "High"].index(x),
    )
    agg_dict["Isolation Interference"] = min
    agg_dict["Unique Peptides"] = len

    new.psms["Unique Peptides"] = np.nan

    new.psms = new.psms.groupby(
        by=[
            "Proteins",
        ],
        sort=False,
        as_index=False,
    ).agg(agg_dict)

    new.update_group_changes()

    return new


def _nan_median(lst):
    if all(np.isnan(i) for i in lst):
        return np.nan
    else:
        return np.nanmedian(lst)


def _nan_sum(lst):
    if all(np.isnan(i) for i in lst):
        return np.nan
    else:
        return np.nansum(lst)


def update_correlation(ds, corr, metric="spearman", min_periods=5):
    """
    Update a table's Fold-Change, and p-value columns.

    Values are calculated based on changes between group_a and group_b.

    Parameters
    ----------
    ds : :class:`DataSet<pyproteome.data_sets.DataSet>`
    corr : :class:`pd.Series`
    metric : str, optional
    min_periods : int, optional
    """
    ds = ds.copy()

    metric = {
        "spearman": partial(spearmanr, nan_policy="omit"),
        "pearson": pearsonr,
    }[metric]

    def _map_corr(row):
        a = pd.to_numeric(row[list(corr.index)])
        b = pd.to_numeric(corr)
        c = [np.nan, np.nan]

        if (~(a.isnull()) & ~(b.isnull())).sum() >= min_periods:
            try:
                c = metric(
                    a,
                    b,
                )
            except ValueError:
                pass

        return pd.Series(
            [c[0], c[1]],
            index=["Fold Change", "p-value"],
        )

    vals = ds.psms.apply(
        lambda row:
        _map_corr(row),
        axis=1,
    )

    for col in vals.columns:
        ds.psms[col] = vals[col]

    return ds


def _concat(dfs):
    cols = []

    for frame in dfs:
        for col in frame.columns:
            if col not in cols:
                cols.append(col)

    df_dict = dict.fromkeys(cols, [])

    def _fast_flatten(input_list):
        return list(chain.from_iterable(input_list))

    for col in cols:
        # Flatten and save to df_dict
        df_dict[col] = list(
            chain.from_iterable(
                frame[col]
                if col in frame.columns else
                [np.nan] * frame.shape[0]
                for frame in dfs
            )
        )

    df = pd.DataFrame.from_dict(df_dict)[cols]

    return df
