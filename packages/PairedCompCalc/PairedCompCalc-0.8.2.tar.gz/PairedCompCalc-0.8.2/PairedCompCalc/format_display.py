"""This module includes functions to format output displays of
PairedCompResultSet data,
in either graphic or textual form.

Some formatting details are defined by module global variables,
which can be easily changed by users.

*** Version History:

2018-02-06, simplified table generation, generate only one selected table type
2018-02-18, use module variable TABLE_FORMAT where needed
2018-04-19, minor changes to include population quality params
2018-08-11, minor cleanup
"""
import numpy as np
from itertools import cycle

import matplotlib.pyplot as plt

# --------------------------- module plot constants:
COLORS = 'rbgk'
# = default plot colors, may be changed by user
MARKERS = 'oxs*_'
# = default markers for medians in plots, may be changed by users
X_LABEL = 'Tested Systems'
# = label for horizontal axis in percentile plots and boxplots

# SHOW_FIGURE = False  # *********** skip this
# = if True: display each figure on screen and wait until user closes the window

# ---------------------------- select table format
TABLE_FORMAT = 'latex'
# generate tables as LaTeX tabular files
# TABLE_FORMAT = 'tab'
# generate plain text files with tab-delimited columns

table_file_suffix = {'latex': '.tex', 'tab': '.txt'}

# ---------------------------- table heading labels:
CREDIBILITY = 'Credibility'
CRED_DIFF = 'Cred. Differences'
SYSTEM = 'System'
TEST_COND = 'Condition'
ATTRIBUTES = 'Attributes'
CORRELATION = 'Corr.'


# ---------------------------- Main Result Classes
class FigureRef():
    """Reference to a single graph instance
    """
    def __init__(self, ax, path=None, name=None):
        """
        :param ax: Axes instance containing the graph
        """
        self.ax = ax
        self.path = path
        self.name = name

    def __repr__(self):
        return (f'FigureRef(ax= {repr(self.ax)}, ' +
                f'path= {repr(self.path)}, name= {repr(self.name)})')

    @property
    def fig(self):
        return self.ax.figure

    def save(self, path, name):
        """Save figure to given path
        Input:
        path = Path to directory where figure is saved
        name = file name for the figure, incl. suffix (usually .eps)
        Result: updated properties path, name
        """
        path.mkdir(parents=True, exist_ok=True)
        self.fig.savefig(str(path / name))
        self.path = path
        self.name = name


class TableRef():
    """Reference to a single table instance,
    formatted in LaTeX OR plain txt versions
    """
    def __init__(self, text=None, fmt=TABLE_FORMAT, path=None, name=None):
        """
        :param text: single string with all table text
        :param fmt: string key for selected format
        """
        # store table parts instead *****???
        self.text = text
        self.fmt = fmt
        self.path = path
        self.name = name

    def __repr__(self):
        return (f'TableRef(text= text, fmt= {repr(self.fmt)}, ' +
                f'path= {repr(self.path)}, name= {repr(self.name)})')

    def save(self, path, file_name):
        """Save table to file.
        Input
        :param path: Path to directory where tables are saved
        :param file_name: file name, EXCLUDING suffix.
            suffix is determined by self.fmt
        :return: None
        Result: updated properties path, name
        """
        path.mkdir(parents=True, exist_ok=True)   # just in case
        f = (path / file_name).with_suffix(table_file_suffix[self.fmt])
        if self.text is not None and len(self.text) > 0:
            f.write_text(self.text, encoding='utf-8')
        self.path = path
        self.name = file_name


# ---------------------------------------- Formatting functions:
def fig_percentiles(perc_0,
                    y_label, s_labels,
                    perc_1=None,
                    case_labels=None,
                    x_label=X_LABEL,
                    x_offset=0.1,
                    x_space=0.5,
                    **kwargs):
    """create a figure with quality percentile results
    Input;
    perc_0 = primary percentile data,
        2D or 3D array with three (min, median, max) quality percentiles, arranged as
        perc_0[i, c, s] = i-th percentile for s_labels[..., s] result, c-th case variant, OR
        perc_0[i, s] if no case variants are included
    y_label = string for y-axis label
    s_labels = list of strings with labels for x_ticks, one for each value in rows perc_0[..., :]
        len(s_labels) == perc_0.shape[-1]
    perc_1 = (optional) 2D or 3D array with quantiles for population mean
    x_label = (optional) string for x-axis label
    case_labels = (optional) list of strings for case variants
        len(case_labels) == perc_0.shape[-2] if perc_0.ndim == 3 else case_labels not used
    x_offset = (optional) space between case-variants of plots for each x_tick
    x_space = (optional) min space outside min and max x_tick values
    kwargs = (optional) dict with any additional keyword arguments for plot commands.

    Returns: fig object with single plot axis with all results
    Arne Leijon, 2018-04-19, allow perc_1 input
    """
    if perc_1 is None:
        pop_y = perc_0 + 0.  # must have a copy for easier code
    else:
        pop_y = perc_1
    fig, ax = plt.subplots()
    if perc_0.ndim == 2:
        perc_0 = perc_0[np.newaxis, ...]
        pop_y = pop_y[np.newaxis, ...]
    else:
        perc_0 = perc_0.transpose((1, 0, 2))
        pop_y = pop_y.transpose((1, 0, 2))
    # now indexed as perc_0[case, quantile, system]
    if case_labels is None:
        case_labels = ['']
    assert perc_0.shape[2] == len(s_labels), 'mismatching system labels'
    assert perc_0.shape[0] == len(case_labels), 'mismatching case labels'
    x = np.arange(0., len(s_labels)) - x_offset * (len(case_labels) - 1) / 2
    for (y, y_p, c_label, c, m) in zip(perc_0, pop_y, case_labels,
                                       cycle(COLORS), cycle(MARKERS)):
        ax.plot(np.tile(x, (2, 1)),
                y[[0, 2], :],
                linestyle='solid', color=c, **kwargs)
        ax.plot(x, y[1,:], linestyle='',
                marker=m, markeredgecolor=c, markerfacecolor='w',
                label=c_label, **kwargs)
        if perc_1 is not None:
            # ax.plot(np.tile(x, (2, 1)),  # *** population range with thicker line
            #         y_p[[0, 2], :],
            #         linestyle='solid', linewidth=2, color=c, **kwargs)
            ax.plot(np.tile(x, (2, 1)),  # *** only markers for population credible range
                    y_p[[0, 2], :],
                    linestyle='',
                    marker='_', markeredgecolor=c, markerfacecolor='w', markersize=20,
                    # *** or marker = m ???
                    **kwargs)
        x += x_offset
    (x_min, x_max) = ax.get_xlim()
    x_min = min(x_min, -x_space)
    x_max = max(x_max, len(s_labels) - 1 + x_space)
    ax.set_xlim(x_min, x_max)
    ax.set_xticks(np.arange(len(s_labels)))
    ax.set_xticklabels(s_labels)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    if np.any([len(l) > 0 for l in case_labels]):
        ax.legend(loc='best')
    # if SHOW_FIGURE:
    #     plt.show()
    return FigureRef(ax)


def fig_indiv_boxplot(q,
                      y_label, s_labels, case_labels=None,
                      x_label=X_LABEL,
                      x_space=0.5,
                      **kwargs):
    """create a figure with boxplot of individual results
    Input;
    q = 2D array or list of 2D arrays,
        with individual quality estimates, arranged as
        q[c][i, s] = i-th individual result for s_labels[s], in c-th case variant, OR
        q[i, s] if no case variants
    y_label = string for y-axis label
    x_label = string for x-axis label
    s_labels = list of strings with labels for x_ticks, one for each value in rows q[..., :]
        len(s_labels) == q.shape[-1]
    case_labels = (optional) list of strings for case variants
        len(case_labels) == len(q) if case_labels is not None
    x_offset = (optional) space between case-variants of plots for each x_tick
    x_space = (optional) min space outside min and max x_tick values
    kwargs = (optional) dict with any additional keyword arguments for boxplot command.

    Returns: fig object with single plot axis with all results
    """
    if len(q) <= 1:
        return None  # boxplot does not work
    fig, ax = plt.subplots()
    if case_labels is None:
        assert q.ndim == 2, 'Input must be 2D if no case variants'
        case_labels = ['']
        q = [q]
        # make it a list of 2D arrays
    x_offset = min(0.2, 0.8 / len(case_labels))
    if len(case_labels) > 1:
        box_width = 0.8 * x_offset
    else:
        box_width = 0.5
    x_pos = np.arange(len(s_labels)) - x_offset * (len(case_labels) - 1) / 2
    for (y, c_label, c, m) in zip(q, case_labels, cycle(COLORS), cycle(MARKERS)):
        boxprops = dict(linestyle='-', color=c)
        # flierprops = dict(marker=m, markeredgecolor=c, markerfacecolor='w', # *** markersize=12,
        #                   linestyle='none')
        whiskerprops = dict(marker='', linestyle='-', color=c)
        capprops = dict(marker='', linestyle='-', color=c)
        medianprops = dict(linestyle='-', color=c)
        ax.boxplot(y, positions=x_pos,
                   widths=box_width,
                   sym='',  # ******** no fliers
                   boxprops=boxprops,
                   medianprops=medianprops,
                   whiskerprops=whiskerprops,
                   capprops=capprops,
                   **kwargs)
        median = np.median(y, axis=0)
        ax.plot(x_pos, median, linestyle='',
                marker=m, markeredgecolor=c, markerfacecolor='w',
                label=c_label)
        x_pos += x_offset

    (x_min, x_max) = ax.get_xlim()
    x_min = min(x_min, -x_space)
    x_max = max(x_max, len(s_labels) -1 + x_space)
    ax.set_xlim(x_min, x_max)
    ax.set_xticks(np.arange(len(s_labels)))
    ax.set_xticklabels(s_labels)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    if np.any([len(l) > 0 for l in case_labels]):
        ax.legend(loc='best')
    # if SHOW_FIGURE:
    #     plt.show()
    return FigureRef(ax)


def tab_percentiles(q, perc, s_labels, head=SYSTEM):
    """create table with quality percentile results,
    in LaTeX tabular and in simple tab-separated text format
    Input:
    q = 2D array with three (min, median, max) quality percentiles, arranged as
        q[p, s] = p-th percentile for s_label[i]
    perc = list of three (min, median, max) percentage values in range 0-100.
    s_labels = list of strings with labels corresponding to q[..., :]
        len(s_labels) == q.shape[-1]
    head = (optional) single string printed over column with s_labels

    Returns: t = string with header lines + one line for each s_labels element,
    """
    align = ['l', 'r', 'r', 'r']
    h = [head] + [f'{p:.0f}\%' for p in perc]
    rows = [ [s] + [f'{p:.2f}' for p in p_s]
            for (s, p_s) in zip(s_labels, q.T)]
    return TableRef(_make_table(h, rows, align))


def tab_percentiles_3d(q, perc, s_labels, case_labels,
                       head=SYSTEM,
                       case_head=TEST_COND):
    """create table with quality percentile results,
    in LaTeX tabular and in simple tab-separated text format

    Input:
    q = 3D array with three (min, median, max) quality percentiles, arranged as
        q[p, c, s] = p-th percentile for s_label[s] in c-th test-condition tuple
    perc = list of three (min, max, median) percentage values in range 0-100.
    s_labels = list of strings with labels corresponding to q[..., :]
        len(s_labels) == q.shape[2]
    case_labels = list of strings with labels corresponding to q[p, :, s]
        len(case_lanbels) == q.shape[1]
    head = (optional) single string printed over column with s_labels

    Returns: table string with header lines + one line for each s_labels element,
    """
    align = ['l', 'l', 'r', 'r', 'r']
    h = [head, case_head] + [f'{p:.0f}\%' for p in perc]
    q = q[:,:,1:].transpose((1, 2, 0))
    # indexed as q[case, system, percentile], excluding system[0]
    rows = []
    for (c, q_c) in zip(case_labels, q):
        if type(c) is tuple and len(c) == 1:
            c = c[0]
        for (s, q_s) in zip(s_labels[1:], q_c):
            rows.append( [s, f'{c}'] + [f'{p:.2f}' for p in q_s])
    return TableRef(_make_table(h, rows, align))


def tab_credible_diff(diff, s_labels, diff_head=CRED_DIFF):
    """create table with credible differences among quality results
    in LaTeX tabular and in simple tab-separated text format
    Input:
    diff = list of tuples ((i,j), p) defining jointly credible differences, indicating that
        prob{ quality of s_labels[i] > quality of s_labels[j] } AND all previous pairs } == p
    diff_head = single string printed over column with pairs of s_labels
    s_labels = list of strings with labels of compared random-vector elements,
        OR, if case_tuples is True: list of tuples (s_label, case_label) ***********'
        len(s_labels) == diff.shape[-1]

    Returns: tuple (tex, txt) strings with header lines + one line for each credible difference,
    tex = a complete tabular version of the table
    txt = a tex-separated ordinary text table
    """
    if len(diff) == 0:
        return None
    align = ['l', 'l', 'c', 'l', 'r']
    h = [_make_cell(diff_head, 4, TABLE_FORMAT), CREDIBILITY]
    rows = []
    col_0 = ''
    # ((i,j), p) = diff[0]  # separate format for first line
    for ((i, j), p) in diff:
        rows.append([col_0, s_labels[i], '>', s_labels[j], f'{100*p:.1f}'])
        col_0 = 'AND' # for all except first row
    return TableRef(_make_table(h, rows, align))


def tab_credible_diff_3d(diff, diff_labels, c_labels,
                         diff_head=CRED_DIFF,
                         c_head=TEST_COND):
    """create table with credible differences among quality results
    in LaTeX tabular and in simple tab-separated text format
    Input:
    diff = list of tuples ((i, j, c), p) defining jointly credible differences, indicating that
        prob{ quality of diff_labels[i] > quality of diff_labels[j]  in case_label[c]
            AND same for all previous tuples in the lise } = p
    diff_head = single string printed over column with pairs of diff_labels
    diff_labels = list of strings with labels of compared random-vector elements,
    c_labels = list of strings with labels of cases within which difference was found.

    Returns: tuple (tex, txt) strings with header lines + one line for each credible difference,
    tex = a complete tabular version of the table
    txt = a tex-separated ordinary text table
    """
    if len(diff) == 0:
        return None
    align = ['l', 'l', 'c', 'l', 'l', 'r']
    h = [_make_cell(diff_head, 4, TABLE_FORMAT), c_head, CREDIBILITY]
    rows = []
    col_0 = ''
    for ((i, j, c), p) in diff:
        rows.append([col_0, diff_labels[i], '>', diff_labels[j], c_labels[c], f'{100*p:.1f}'])
        col_0 = 'AND'  # for all except first row
    return TableRef(_make_table(h, rows, align))


def tab_credible_corr(c, a_labels):
    """create table of credible correlations
    in LaTeX tabular and in simple tab-separated text format.

    Input:
    c = list of tuple((i, j), p, md_corr), where
        (i, j) are indices into a_labels,
        p is joint credibility,
        md_corr = median conditional correlation value, given all previous
    a_labels = list with string labels for correlated attributes
    """
    if len(c) == 0:
        return None
    align = ['l', 'l', 'c', 'l', 'r', 'r']
    h = [_make_cell(ATTRIBUTES, 4, TABLE_FORMAT), CORRELATION, CREDIBILITY]
    rows = []
    col_0 = ''
    for ((i, j), p, mdc) in c:
        rows.append([col_0, a_labels[i], '*', a_labels[j], f'{mdc:.2f}', f'{100*p:.1f}'])
        col_0 = 'AND'
    return TableRef(_make_table(h, rows, align))


# ------------------------------------------ internal help functions:
# more variants may be added for other table formats

table_begin = {'latex': lambda align: '\\begin{tabular}{' + ' '.join(c for c in align) + '}\n',
               'tab': lambda align: ''}
table_head_sep = {'latex':'\hline\n',
                  'tab':''}
table_cell_sep = {'latex': ' & ',
                  'tab':' \t '}
table_row_sep = {'latex': '\\\\ \n',
                 'tab': '\n'}
table_end = {'latex':'\hline\n\end{tabular}',
             'tab': ''}


def _make_cell(text, col_span, fmt):
    """Format multi-column table cell, usually only for header line
    :param text: cell contents
    :param col_span: number of columns to span
    :param fmt: str key for table format
    :return: string with latex or plain cell contents
    """
    if fmt == 'latex' and col_span > 1:
        return '\multicolumn{' + f'{col_span}' + '}{c}' + '{' + text + '}'
    else:
        return text


def _make_table(header, rows, col_alignment):
    """Generate a string with table text.
    Input:
    :param header: list with one string for each table column
    :param rows: list of rows, ehere
        each row is a list of string objects for each column in this row
    :param col_alignment: list of alignment symbols, l, r, or c
        len(col_alignment) == len(header) == len(row), for every row in rows

    :return: single string with complete table
    """
    def make_row(cells, fmt):
        return table_cell_sep[fmt].join(f'{c}' for c in cells) + table_row_sep[fmt]
    # ------------------------------------------------------------------------

    fmt = TABLE_FORMAT  # module global constant
    t = table_begin[fmt](col_alignment)
    t += table_head_sep[fmt]
    t += make_row(header, fmt)
    t += table_head_sep[fmt]
    t += ''.join((make_row(r, fmt) for r in rows))
    t += table_end[fmt]
    return t