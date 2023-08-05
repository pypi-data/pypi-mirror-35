"""This module defines data structures and functions to display analysis results
given a PairedCompResultSet instance,
learned from a set of data from a paired-comparison experiment.

Results are shown as figures and tables.
Figures are saved in eps format.
Tables are saved in LaTeX tabular format OR in tab-delimited text files.
Thus, both figures and tables can be easily imported into a LaTeX document.

*** Main Class:
PairedCompDisplaySet = a structured container for all display results

Each display element can be accessed and modified by the user, before saving.

Each display set can include data for one or two predictive distributions,
selected among the following three types:
*1: a random individual in a Group of test subjects, for whom paired-comp data are available
*2: a random individual in the Population from which test subjects were recruited,
    but for whom no data have been collected
*3: the mean (=median) across all individuals in the Population

*** Usage Example:
    pc_ds = PairedCompDisplaySet(pc_result.predictive_group_individual(),
                                 pc_result.predictive_population_mean())
    OR other combinations of predictive distributions.

    pc_ds = display(pc_result)
        gives a default display of population individual and mean distributions.

    The display elements are accessible as, e.g.,
    pc_ds.quality.groups['NormalHearing'].attr['Intelligibility'].range.percentile_plot.ax
        is the Axes object where percentiles are plotted for this group, pooled across all test conditions
    pc_ds.quality.groups['NormalHearing'].attr['Intelligibility'].range.percentile_tab
        is the table where the same percentiles are displayed numerically
    pc_ds.quality.groups['NormalHearing'].attr['Intelligibility'].range_by_test_cond['SNR'].boxplot.ax
        is the Axes object where boxplots of individual participant results are plotted,
        sub-divided among categories within test_factor 'SNR'
        NOTE: boxplots are used only for predictive_group_individual results.
    pc_ds.correlation.groups['NormalHearing'] is a table of credible correlations,
        in the results for the selected group
    pc_ds.correlation.groups[('NormalHearing','ImpairedHearing')] is a table of credible correlations,
        in the results pooled across both groups

The method PairedCompDisplaySet.save(path)
saves all display elements in a directory tree, corresponding to the display-set structure.

Figures and tables are assigned descriptive names,
and stored in sub-directories with names constructed from
string labels of Groups and Attributes,
as defined in the PairedCompFrame object of the input PairedCompResultSet instance.

If there is more than one Group,
    one sub-directory is created for each group, and one extra for the pooled groups,
    and one sub-sub-directory for each attribute, with results within the group.
    If there is more than one attribute,
    the group sub-directory also includes tables with correlations between attributes.
    The top directory will also have one sub-directory for each attribute,
    containing files showing differences between groups, for this attribute.

*** Global module parameters that may be changed by user:

PERCENTILES
CREDIBILITY_LIMIT

*** Version History:
2018-01-08, first functional version
2018-04-02, separate analyses of range displays and attribute-correlation displays
            with range displays allowing missing subjects for some attributes, but
            correlations calculated only within identical subjects across attributes.
            Renamed some classes to reflect changed structure.
2018-04-12, use systems_alias labels in all displays
2018-04-24, display estimated group-mean credible intervals
2018-05-21, PairedCompDisplaySet.display called with selected predictive model(s) as input
"""

# ***** display response-category intervals in range plots ???

import numpy as np
from pathlib import Path
import logging
from itertools import product
import string

# from pc_model import PairedCompIndModel
from . import format_display as fmt
from samppy.credibility import cred_diff, cred_group_diff, cred_corr


PERCENTILES = [5., 50., 95.]
# MUST have exactly three values, with median in the middle
CREDIBILITY_LIMIT = 0.6

logger = logging.getLogger(__name__)


# -------------------------------- Main Module Function Interface
def display(pc_result, table_format=None):
    """Main function to display default set of paired-comparison results.
    :param: pc_result: a single PairedCompResultSet object
        with learned models saved in a nested dict as
        model = pc_result.models[group][attribute][subject]
    :param: table_format: (optional) format = 'latex' or 'tab', for all table displays
    :return: single QualityDisplaySet instance with display results
    """
    if table_format is not None:
        fmt.TABLE_FORMAT = table_format
    logger.info('Displaying default predictive_population_individual and predictive_population_mean')
    return PairedCompDisplaySet.display(pc_result.predictive_population_individual(),
                                        pc_result.predictive_population_mean())
# ------------------------------------------------------------------


# ------------------------------------------------ Elementary Display Class:
class RangeDisplay:
    """Container for system result displays for a given attribute,
    optionally sub-divided along secondary factor (test-condition or group)
    """
    def __init__(self, percentile_plot,
                 boxplot=None,
                 percentile_tab=None):
        """
        Input:
        :param percentile_plot: FigureRef with percentile plot showing
            predictive individual and population properties
        :param boxplot: (optional) FigureRef with boxplots of individual MAP estimated results
        :param percentile_tab: (optional) TableRef with percentile_plot results tabulated.
        """
        self.percentile_plot = percentile_plot
        self.boxplot = boxplot
        self.percentile_tab = percentile_tab

    def __repr__(self):
        return ('RangeDisplay(' +
                f'\n\tpercentile_plot={repr(self.percentile_plot)}, ' +
                f'\n\tboxplot= {repr(self.boxplot)}' +
                f'\n\tpercentile_tab= {repr(self.percentile_tab)}' +
                f'\n\t)')

    def save(self, dir_path, file_prefix=''):
        """Input:
        :param dir_path: path to directory for saving files
        :param file_prefix: (optional) first part of file-name
        :return:
        """
        if self.percentile_plot is not None:
            self.percentile_plot.save(dir_path, file_prefix + 'percentiles.eps')
        if self.boxplot is not None:
            self.boxplot.save(dir_path, file_prefix + 'boxplot.eps')
        if self.percentile_tab is not None:
            self.percentile_tab.save(dir_path, file_prefix + 'percentiles')


# CorrelationDisplay = fmt.TableRef

# class DiffDisplay:
#     """Graphical and tabular displays for credible differences between systems
# or between other variables.
#     """
#     pass  # **************** Currently only == a single TableRef


# ---------------------------------------------------------- Main Display Classes:

class PairedCompDisplaySet:
    """Root container for all displays
    of selected predictive quality and attribute-correlation results
    from one PairedCompResultSet object.
    All display elements can be saved as files within a selected directory three.
    The complete instance can also be serialized and dumped to a single pickle file,
    then re-loaded and re-saved, if any display object needs to be edited.
    """

    def __init__(self, quality, correlation=None):
        """
        Input:
        :param quality: single QualityDisplaySet instance with all quality estimates
        :param correlation: (optional) CorrelationDisplaySet instance with attribute correlations,
            only if there are several perceptual attributes
        """
        self.quality = quality
        self.correlation = correlation

    def __repr__(self):
        return ('PairedCompDisplaySet(' +
                f'\n\tquality= {repr(self.quality)}, ' +
                f'\n\tcorrelation= {repr(self.correlation)}' +
                '\n\t)')

    def save(self, dir_top):
        """Save all displays in a directory tree
        Input:
        :param dir_top: Path or string with top directory for all displays
        :return: None
        """
        dir_top = Path(dir_top)  # just in case
        # dir_top.mkdir(parents=True, exist_ok=True)  # just in case
        self.quality.save(dir_top)
        if self.correlation is not None:
            self.correlation.save(dir_top)

    @classmethod
    def display(cls, pred_0, pred_1=None):
        """Create displays for all results from a paired-comparison experiment,
        and store all display elements in a single structured object.
        :param pred_0: a single PredictiveResultSet instance, with
            pred_0[group][attribute] = a single predictive model
        :param pred_1: (optional) secondary PredictiveResultSet
            with another type of predictive models
        :return: a single cls instance

        Arne Leijon, 2018-05-18
        """
        logger.info(f'Creating displays for {len(pred_0.models)} group(s)')
        logger.info(fig_comments(PERCENTILES))
        logger.info(table_comments(pred_0.pcf))
        if len(pred_0.pcf.attributes) > 1:
            return cls(QualityDisplaySet.display(pred_0, pred_1),
                       CorrelationDisplaySet.display(pred_0))
        else:
            return cls(QualityDisplaySet.display(pred_0, pred_1))


class QualityDisplaySet:
    """Top container for all displays of quality results from one PairedCompResultSet object,
    sub-divided across groups, and across perceptual attributes.
    """

    def __init__(self, groups, group_effects=None):
        """Input:
        :param groups: dict with (group: GroupDisplaySet) elements,
            one for each subject group (same as overall, if only one group)
        :param group_effects: (optional) single GroupEffectSet instance,
            showing differences between groups, if there is more than one group
        """
        # self.overall = overall
        self.groups = groups
        self.group_effects = group_effects

    def __repr__(self):
        return ('QualityDisplaySet(' +
                f'\n\tgroups= {repr(self.groups)}, ' +
                f'\n\tgroup_effects= {repr(self.group_effects)}\n\t)')

    def save(self, dir_top):
        """Save all displays in a directory tree
        Input:
        :param dir_top: Path or string with top directory for all displays
        :return: None
        """
        dir_top = Path(dir_top)  # just in case
        for (g, g_display) in self.groups.items():
            g = _dir_name(g)
            if len(g) == 0 or all(s in string.whitespace for s in g):
                g_display.save(dir_top)
            else:
                g_display.save(dir_top / g)
        if self.group_effects is not None:
            self.group_effects.save(dir_top)

    @classmethod
    def display(cls, pred_0, pred_1=None):
        """Create displays for all results from a paired-comparison experiment,
        and store all display elements in a single structured object.
        :param pred_0: a single PredictiveResultSet instance, with
            pred_0[group][attribute] = a single predictive model
        :param pred_1: (optional) a secondary PredictiveResultSet
            with another type of predictive models
        :return: a single new cls instance

        Arne Leijon, 2018-05-18
        """
        # display separate results for each group
        groups = {g: GroupDisplaySet.display(g_models) if pred_1 is None
                  else GroupDisplaySet.display(g_models, pred_1.models[g])
                  for (g, g_models) in pred_0.models.items()}
        # including one extra overall group with all groups merged, if more than one

        if len(groups) > 1:
            ag_models_0 = {a: {g: g_models[a]
                               for (g, g_models) in pred_0.models.items()
                               if type(g) is not tuple}  # exclude merged overall group
                           for a in pred_0.pcf.attributes}
            if pred_1 is not None:
                ag_models_1 = {a: {g: g_models[a]
                                   for (g, g_models) in pred_1.models.items()
                                   if type(g) is not tuple}  # exclude merged overall group
                               for a in pred_0.pcf.attributes}
            else:
                ag_models_1 = None
            group_effects = GroupEffectSet.display(ag_models_0, ag_models_1)
        else:
            group_effects = None
        return cls(groups, group_effects)


class CorrelationDisplaySet:
    """Top container for all attribute correlation results.
    Used only if there is more than one attribute."""
    def __init__(self, groups):
        """
        Input
        :param groups: dict with (groups: attribute correlation table) elements
        """
        self.groups = groups

    def __repr__(self):
        return 'CorrelationDisplaySet(groups= g_dict)'

    def save(self, dir_top):
        """
        Save to given directory
        :param dir_top: Path or string with top directory for all displays
        :return: None
        """
        f_name = 'correlation'
        dir_top = Path(dir_top)  # just in case
        if len(self.groups) > 1:
            for (g, g_display) in self.groups.items():
                if g_display is not None:
                    g_display.save(dir_top / _dir_name(g), f_name)

    @classmethod
    def display(cls, pred):
        """
        Create all correlation displays for given results.
        To be called only if there are several attributes.
        Includes only subjects with complete result data for all attributes.
        :param pred: single PredictiveResultSet instance, with
            one or more groups, and more than one attribute for each group
        :return: single new cls instance with all correlation displays
        """
        # pcf = pred.pcf
        group_corr = {g: display_attribute_correlation(g_models)
                      for (g, g_models) in pred.models.items()}
        return cls(group_corr)


# ---------------------------------------------------------- Secondary Display Classes:

class GroupDisplaySet:
    """Container for all quality-range displays related to a single group,
     OR to all groups joined.
    """
    def __init__(self, attr):
        """
        :param attr: dict with elements (attribute: AttributeDisplaySet)
        """
        self.attr = attr

    def __repr__(self):
        return 'GroupDisplaySet(attr= attribute_dict)'

    def save(self, dir_path):
        """
        :param dir_path: Path instance to directory to save displays for this group
        :return: None
        """
        for (a, a_display) in self.attr.items():
            a_display.save(dir_path / a)
            # one sub-directory for each attribute

    @classmethod
    def display(cls, models_0, models_1=None):
        """Generate all displays for a given group
        :param models_0: dict with elements (attr: single predictive model)
        :param models_1: (optional) dict with elements (attr: other predictive model}
        :return: single GroupDisplaySet instance with all displays for this group
        """
        if models_1 is None:
            a_displays = {a: AttributeDisplaySet.display(a, a_model)
                          for (a, a_model) in models_0.items()}
        else:
            a_displays = {a: AttributeDisplaySet.display(a, a_model, models_1[a])
                          for (a, a_model) in models_0.items()}
        return cls(a_displays)


class AttributeDisplaySet:
    """Container for all display results for a single given attribute
    """

    def __init__(self, range,
                 diff=None,
                 test_cond_effects=None):
        """Input:
        :param range: single RangeDisplay object with results joined across test_conditions,
            or with ranges sub-divided for one secondary factor
        :param diff: (optional) TableRef with credible differences between systems,
            (or between groups).
        :param test_cond_effects: (optional) single TestCondEffectSet instance,
            showing all differences between test_factors and test_condition_tuples
        """
        self.range = range
        self.diff = diff
        self.test_cond_effects = test_cond_effects

    def __repr__(self):
        return ('AttributeDisplaySet(' +
                f'\n\trange= {repr(self.range)}' +
                f'\n\tdiff= {repr(self.diff)}' +
                f'\n\ttest_cond_effects= {repr(self.test_cond_effects)}' +
                '\n\t)')

    def save(self, path):
        """Save all stored display objects in specified (sub-)tree
        """
        # path.mkdir(parents=True, exist_ok=True)   # just in case
        self.range.save(path)
        if self.diff is not None:
            self.diff.save(path, 'cred-diff')
        if self.test_cond_effects is not None:
            self.test_cond_effects.save(path / 'test-cond-effects')

    @classmethod
    def display(cls, attr, model_0, model_1=None):
        """Create all displays for a single attribute
        :param attr: string identifying the attribute
        :param model_0: single predictive model instance for this attribute
        :param model_1: (optional) secondary type of predictive model
        :return: single cls instance with all displays
        """
        pcf = model_0.pcf
        attr_label = attr + ' (' + model_0.rv_class.unit_label + ')'
        q_samples = model_0.quality_samples.reshape((-1, pcf.n_systems))
        # = 2D array, now merged as if only a single test_condition_tuple
        q_quant = np.percentile(q_samples, PERCENTILES, axis=0)
        try:
            q_map = model_0.quality_map.reshape((-1, pcf.n_systems))
        except AttributeError:
            q_map = None

        if model_1 is None:
            q_quant_1 = None
        else:
            q_quant_1 = np.percentile(model_1.quality_samples.reshape((-1, pcf.n_systems)),
                                      PERCENTILES, axis=0)
            # logger.info(f'Ind quant =\n{q_quant}')
            # logger.info(f'Pop quant =\n{q_quant_1}')

        range_perc = fmt.fig_percentiles(q_quant, attr_label, pcf.systems_disp,
                                         perc_1=q_quant_1)
        table = fmt.tab_percentiles(q_quant, PERCENTILES, pcf.systems_disp)
        if q_map is None:
            f_box = None
        else:
            f_box = fmt.fig_indiv_boxplot(q_map, attr_label, pcf.systems_disp)
        range = RangeDisplay(percentile_plot=range_perc,
                             boxplot=f_box,
                             percentile_tab=table)

        d = cred_diff(q_samples, diff_axis=1, sample_axis=0,
                      p_lim=CREDIBILITY_LIMIT)
        diff = fmt.tab_credible_diff(d, pcf.systems_disp)
        a_set = cls(range, diff)
        if pcf.n_test_condition_tuples > 1:
            a_set.test_cond_effects = TestCondEffectSet.display(attr, model_0, model_1)
        return a_set


class TestCondEffectSet:
    """Container for all displays of differences between test_factors and test_cond_tuples
    """
    def __init__(self, test_factors,
                 range_by_test_cond=None,
                 diff_within=None,
                 diff_between=None):
        """Input:
        :param test_factors: dict with (test-factor: RangeDisplay) elements
        :param range_by_test_cond: single TableRef object with all percentiles,
            sub-specified for each test_cond_tuple
        :param diff_within: single TableRef object with credible differences between systems,
            within each test_condition_tuple
        :param diff_between: single TableRef object with credible differences between test_condition_tuples,
            within each system
        """
        self.test_factors = test_factors
        self.range_by_test_cond = range_by_test_cond
        self.diff_within = diff_within
        self.diff_between = diff_between

    def __repr__(self):
        return ('TestCondEffectSet(' +
                f'\n\ttest_factors= {repr(self.test_factors)}' +
                f'\n\trange_by_test_cond= {repr(self.range_by_test_cond)}' +
                f'\n\tdiff_within= {repr(self.diff_within)}' +
                f'\n\tdiff_between= {repr(self.diff_between)}' +
                '\n\t)')

    def save(self, path):
        for (tf, tf_range) in self.test_factors.items():
            tf_range.save(path, tf + '-')
            # same starts with test-factor label
        if self.range_by_test_cond is not None:
            self.range_by_test_cond.save(path, 'percentiles-by-test-cond')
        if self.diff_within is not None:
            self.diff_within.save(path, 'cred-diff-within-test-cond')
        if self.diff_between is not None:
            self.diff_between.save(path, 'cred-diff-between-test-cond')

    @classmethod
    def display(cls, attr, model_0, model_1=None):
        """Generate quality results for given attribute,
        sub-divided across test conditions within each Test Factor,
        separated for each test-condition combination in other Test Factors
        :param attr: string with current attribute label
        :param model_0: single predictive model for this attribute, in all test conditions
        :param model_1: (optional) secondary type of predictive model
            predictive models may or may not have quality_map method
        :return: single cls instance
        """
        pcf = model_0.pcf
        q_samples_0 = model_0.quality_samples.transpose((1, 0, 2))
        try:
            q_map = model_0.quality_map.transpose((1, 0, 2))
            # = stored as q_xx[test_cond, sample, system]
        except AttributeError:
            q_map = None
        if model_1 is None:
            q_samples_1 = q_samples_0 + 0.  # copy just to simplify code later
        else:
            q_samples_1 = model_1.quality_samples.transpose((1, 0, 2))

        # --------------------- percentile table for model_0. system by test_condition_tuple
        q_tc = np.percentile(q_samples_0, PERCENTILES, axis=1)
        perc_by_test_cond = fmt.tab_percentiles_3d(q_tc,
                                                   PERCENTILES,
                                                   pcf.systems_disp,
                                                   pcf.test_condition_tuples())
        # --------------------------------------------------------

        n_tc = pcf.n_test_conditions
        q_samples_0 = q_samples_0.reshape((*n_tc, -1, pcf.n_systems))
        # stored as q_samples_0[tc_0, tc_1,..., sample, system], i.e.,
        # one array dimension for each test factor = each key in pcf.test_conditions
        if q_map is not None:
            q_map = q_map.reshape((*n_tc, -1, pcf.n_systems))
            # stored as q_map[tc_0, tc_1,..., subject, system]
        if model_1 is not None:
            q_samples_1 = q_samples_1.reshape((*n_tc, -1, pcf.n_systems))

        test_factors = dict()
        for (tf, tf_conditions) in pcf.test_conditions.items():

            # plot quantiles by tf
            assert len(tf_conditions) == q_samples_0.shape[0], '*** error in axis permutation'  # *** TEST
            q_tf_0 = q_samples_0.reshape((len(tf_conditions), -1, pcf.n_systems))
            # q_tf_0[tc, sample, system] with samples merged for all OTHER test test_factors
            q_perc_0 = np.percentile(q_tf_0, PERCENTILES, axis=1)
            if model_1 is None:
                cred_range = fmt.fig_percentiles(q_perc_0, attr, pcf.systems_disp,
                                                 case_labels=tf_conditions)
                q_samples_0 = np.moveaxis(q_samples_0, 0, len(n_tc) - 1)
                # moved processed test-condition axis to last among test-test_factors
            else:
                q_tf_1 = q_samples_1.reshape((len(tf_conditions), -1, pcf.n_systems))
                # q_tf_1[tc, sample, system] with samples merged for all OTHER test test_factors
                q_perc_1 = np.percentile(q_tf_1, PERCENTILES, axis=1)
                cred_range = fmt.fig_percentiles(q_perc_0, attr, pcf.systems_disp,
                                                 perc_1=q_perc_1,
                                                 case_labels=tf_conditions)
                q_samples_0 = np.moveaxis(q_samples_0, 0, len(n_tc) - 1)
                q_samples_1 = np.moveaxis(q_samples_1, 0, len(n_tc) - 1)
                # moved processed test-condition axis to last among test-test_factors

            if q_map is None:
                test_factors[tf] = RangeDisplay(percentile_plot=cred_range, boxplot=None)
            else:
                # include q_map boxplots:
                assert len(tf_conditions) == q_map.shape[0], '*** error in axis permutation'
                q_map_tf = q_map.reshape((len(tf_conditions), -1, pcf.n_systems))
                # stored as q[test_cond, subject-repeated, system]
                # i.e., q_map for SAME subject may appears several times, AS IF they were independent!
                boxplot = fmt.fig_indiv_boxplot(q_map_tf, attr,
                                                pcf.systems_disp, case_labels=tf_conditions)
                test_factors[tf] = RangeDisplay(percentile_plot=cred_range,
                                                boxplot=boxplot)
                # ******* no corresponding percentile_tab ???
                q_map = np.moveaxis(q_map, 0, len(n_tc) - 1)

        q_samples_0 = q_samples_0.reshape((pcf.n_test_condition_tuples, -1, pcf.n_systems))
        # make credible-diff between systems for each test_condition_tuple
        tc_tuples = [tct if len(tct) > 1 else tct[0]
                     for tct in pcf.test_condition_tuples()]
        # len(tc_tuples) == q_samples_0.shape[0]
        d = cred_diff(q_samples_0, diff_axis=2, case_axis=0, sample_axis=1,
                      p_lim=CREDIBILITY_LIMIT)
        diff_within = fmt.tab_credible_diff_3d(d,
                                               diff_labels=pcf.systems_disp,
                                               c_labels=tc_tuples,
                                               c_head=fmt.TEST_COND)

        # make credible-diff between test_condition_tuple(s) for each system
        d = cred_diff(q_samples_0, diff_axis=0, case_axis=2, sample_axis=1,
                      p_lim=CREDIBILITY_LIMIT)
        diff_between = fmt.tab_credible_diff_3d(d,
                                              diff_labels=tc_tuples,
                                              c_labels=pcf.systems_disp,
                                              c_head=fmt.SYSTEM)
        return cls(test_factors,
                   perc_by_test_cond,
                   diff_within,
                   diff_between)


class GroupEffectSet:
    """Container for all displays illustrating differences between subject groups.
    """
    def __init__(self, attr):
        """
        :param attr: dict with (attr: AttributeDisplaySet) elements
        """
        self.attr = attr

    def __repr__(self):
        return 'GroupEffectSet(attr= attr_dict)'

    def save(self, dir_path):
        """Input:
        :param dir_path: Path instance to directory where results are saved
        :return: None
        """
        for (a, a_display) in self.attr.items():
            a_display.save(dir_path / a / 'group-effects')
            # one sub-directory for each attribute

    @classmethod
    def display(cls, ag_models_0, ag_models_1=None):
        """Create displays to show differences between groups
        Input:
        :param ag_models_0: nested dict with
            ag_models_0[attr][group] == single predictive model
        :param ag_models_0: (optional) similar nested dict with secondary predictive models
        :return: a single cls instance
        """
        first_attr = list(ag_models_0.values())[0]
        first_model = list(first_attr.values())[0]
        pcf = first_model.pcf
        attr_unit = first_model.rv_class.unit_label

        attr_displays = dict()
        for (attr, g_models_0) in ag_models_0.items():
            attr_label = attr + ' (' + attr_unit + ')'
            g_labels = list(g_models_0.keys())
            q_samples_0 = [m.quality_samples for m in g_models_0.values()]
            # stored as q_samples_0[group][sample, test-cond-tuple, system]
            q_quant_0 = np.array([np.percentile(q.reshape(-1, pcf.n_systems),
                                                PERCENTILES, axis=0)
                                  for q in q_samples_0])
            # q_quant_0[group, perc, system]
            q_quant_0 = q_quant_0.transpose((1, 0, 2))
            # q_quant_0[perc, group, system]
            if ag_models_1 is None:
                q_quant_1 = None
            else:
                q_samples_1 = [m.quality_samples for m in ag_models_1[attr].values()]
                q_quant_1 = np.array([np.percentile(q.reshape(-1, pcf.n_systems),
                                                    PERCENTILES, axis=0)
                                      for q in q_samples_1])
                q_quant_1 = q_quant_1.transpose((1, 0, 2))

            perc_by_group_fig = fmt.fig_percentiles(q_quant_0,
                                                    y_label=attr_label,
                                                    s_labels=pcf.systems_disp,
                                                    perc_1=q_quant_1,
                                                    case_labels=g_labels)
            perc_by_group_tab = fmt.tab_percentiles_3d(q_quant_0, PERCENTILES,
                                                       pcf.systems_disp, g_labels)

            try:
                q_map = [m.quality_map.reshape((-1, pcf.n_systems))
                     for m in g_models_0.values()]
                # stored as q_map[group][subject*test_cond, system]
                boxplot_by_group = fmt.fig_indiv_boxplot(q_map, attr_label,
                                                         pcf.systems_disp,
                                                         case_labels=g_labels)
            except AttributeError:
                boxplot_by_group = None

            range = RangeDisplay(percentile_plot=perc_by_group_fig,
                                 percentile_tab=perc_by_group_tab,
                                 boxplot=boxplot_by_group)

            # credible group differences, for all systems, test conditions
            tc_s_labels = [s + ' ' + str(tct)
                           for (tct, s) in product(pcf.test_condition_tuples(),
                                                   pcf.systems_disp[1:])]
            q_samples_0 = [qs[..., 1:].reshape(-1, len(tc_s_labels))
                         for qs in q_samples_0]
            d = cred_group_diff(q_samples_0, sample_axis=0, case_axis=1,
                                p_lim=CREDIBILITY_LIMIT)
            group_diff = fmt.tab_credible_diff_3d(d, g_labels, tc_s_labels)
            attr_displays[attr] = AttributeDisplaySet(range, group_diff)

        return cls(attr_displays)
        # cred diff for all combinations attr, tc, system ???  ********


# ---------------------------------- Help functions:

def _dir_name(g):
    """make sure group name is a possible directory name
    :param g: string or tuple of strings
    :return: string to be used as directory
    """
    if type(g) is tuple:  # several strings
        g = '+'.join(s for s in g)
    return g


def display_attribute_correlation(a_models):
    """Show jointly most credible correlations
    in subsets of all pairs of perceptual attributes
    Input:
    a_models = dict with (attr: PairedCompIndModel) elements,
        all with equal number of samples for matched identical subjects

    NOTE: calculation in cred_corr function is slightly different from MatLab version
    Arne Leijon, 2017-12-27
    2018-05-20, check that number of samples are mathing, i.e., RELATED across attributes
    """
    a_labels = list(a_models.keys())
    q_samples = [m.quality_samples for m in a_models.values()]
    n_samples = len(q_samples[0])
    if all(len(s) == n_samples for s in q_samples):
        q_samples = np.array(q_samples)
        # we have matching samples, can do the correlation
        # stored as q_samples[attr, sample, test_cond_tuple, system]
        (n_attr, n_samples, n_tc, n_systems) = q_samples.shape
        q_samples = q_samples.reshape((n_attr, n_samples, -1))
        # join all test_condition_tuples
        c = cred_corr(q_samples, corr_axis=0, sample_axis=1, vector_axis=2)
        # = list of tuple( ((i,j), p, median_corr_coeff )
        return fmt.tab_credible_corr(c, a_labels=a_labels)
    else:
        # cannot do correlations
        return None


def fig_comments(perc):
    """Generate figure explanations.
    Input:
    perc = vector with percentile values
    Returns: comment string
    """
    p_min = np.amin(perc)
    p_max = np.amax(perc)
    c = f"""Figure Explanations:
    
Figure files with names like
percentiles.eps or someTestFactorLabel-percentiles.eps
display medians (middle marker symbol), and credible intervals (vertical bars) 
for the primary selected type of predictive distribution.
The vertical bars show the range between {p_min:.1f}- and {p_max:.1f}- percentiles.

If a secondary type of predictive model is included for display,
two horisontal-line markers show the credible range for this predictive model.

Primary and secondary predictive models may show distribution of quality parameters
1: for a random individual in the tested subject group,
2: for a random individual in the population from which the subject group was recruited,
3: for the mean in the population.

The credible ranges include all uncertainty
caused both by real inter-individual perceptual differences
and by the limited number of judgments by each listener.

Figure files with names like boxplot.eps 
or someTestFactorLabel-boxplot.eps
show boxplots of the distribution of point-estimated individual results in the participant group.
"""
    return c


def table_comments(pcf):
    c = """Table Explanations:

*** Tables of Percentiles:
Files with names like percentiles.tex or percentiles.txt
show numerical versions of the information in percentile plots,
including only the primary predictive distribution.


*** Tables of Credible Differences:
Files with names like cred-diff.tex or cred-diff.txt 
show a list of System pairs
which are ALL JOINTLY credibly different
with the tabulated credibility.
The credibility value in each row is the JOINT probability
for the pairs in the same row and all rows above it.
"""
    if pcf.n_attributes > 1:
        c += """*** Tables of Attribute Correlations
show cosine-similarity between perceptual Attribute results
across all Systems and Test Conditions

The Credibility Table of Conditional Attribute Correlations
shows a list of Attribute Pairs, for which
the Conditional Correlations are ALL JOINTLY credibly non-zero.
Each Conditional Correlation value shows the remaining
correlation, given that all the previous correlations are truly non-zero,
"""
    return c