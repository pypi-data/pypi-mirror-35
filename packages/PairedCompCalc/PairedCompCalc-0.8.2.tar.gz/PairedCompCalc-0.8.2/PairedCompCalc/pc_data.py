"""This module defines classes to hold paired-comparison experimental data,
and methods and functions to read and write such data.

*** Class Overview:

PairedCompFrame: defines layout of a paired-comparison experiment.

PairedCompRecord: defines all results from tests with ONE subject, ONE attribute,
    and one or more combination(s) of test conditions,
    defined by one category label for each Test Factor.

StimRespItem: a container for a single stimulus and response pair

PairedCompDataSet: all data for selected group(s), subjects, attributes, and test conditions,
    to be used as input for statistical analysis.
    Each subject must be tested in ALL test conditions,
    but not necessarily for all perceptual attributes.

*** Input Data Files:

All input files with data from an experiment must be stored in one directory tree.
If results are to be analyzed for more than one Group of test subjects,
the data files for each group must be stored in
separate sub-directory trees starting on the first level just below the top directory.
All sub-directories in the tree are searched for data files.

Each data file contains paired-comparison results
for ONE test subject judging ONE perceptual attribute.
File names are arbitrary, although they may be somehow associated with
the encoded name of the participant, to facilitate data organisation.

Several files may be used for the same test subject, e.g.,
for results obtained for different attributes or different test conditions,
or simply for replicated test sessions with the same subject.

Each file is a text file containing a representation of a PairedCompRecord object.

The simplest file format is a json-serialized version of a PairedCompRecord object.
See class PairedCompRecord for details.
Files in this format should be saved with extension 'json'.

The easiest way to create data files in a user program
is to import class PairedCompRecord,
create instances of that class by setting the required property values,
and then call the save method of the instance.

For backward compatibility,
PairedCompRecord data files may also be stored in an older text format,
used by Dahlquist and Leijon (2003).
Files in this format are saved with extension 'res'.

All input data are collected by a single function call, as
ds = PairedCompDataSet.load(pcf, dir, groups, fmt='json')

If fmt='json' is specified, the load method reads only files with the 'json' extension
in the top directory defined by the path-string in parameter dir.
Files are similarly selected for fmt='res'.

If the fmt argument is left unspecified, or if fmt=None, or fmt='',
PairedCompDataSet.load will attempt to read ALL files in the designated directory tree,
and use the files that seem to contain paired-comparison data.

The parameter groups is an optional list of sub-directory names,
one for each participant group.

The parameter pcf is a PairedCompFrame object that defines the experimental layout.
Some properties of this object can define selection criteria
for a subset of data to be included for analysis.

*** Example Directory Tree:

Assume we have data files in the following directory structure:
~/sessions / NH / Low,   containing files Subject0.json, ..., Subject20.json
~/sessions / NH / High,  containing files Subject0.json, ..., Subject20.json
~/sessions / HI / Low,  containing files test0.json, ..., test10.json
~/sessions / HI / High, containing files test0.json, ..., test10.json

Directories 'NH' and 'HI' may contain data for different groups of test participants,
e.g, individuals with normal hearing (NH) or with impaired hearing (HI).

Sub-directories named 'Low' and 'High' may include data files collected
in two different noise conditions, with 'Low' or 'High' signal-to-noise ratio.
Data for the SAME subjects should then be found in BOTH sub-directories 'Low' and 'High'.
because each subject should be tested in all test conditions.

If tests have been done for different perceptual Attributes,
there should be data files for each subject with each Attribute.
Each subject should ideally be tested with all Attributes,
to allow the most accurate estimation of correlations between Attributes.

** Accessing Input Data för Analysis:

*1: Create a PairedCompFrame object defining the experimental layout, e.g., as:
pcf = PairedCompFrame(systems = ['testA', 'testB', 'testC'],  # three sound processors
        attributes = ['Preference'],  # only a single perceptual attribute in this case
        test_conditions = {'stim': ['speech', 'music'],  # test factor 'stim' with two categories
                            'SNR': ['Low', 'High']}  #  test factor 'SNR' with two categories
        )
NOTE: attribute labels must be strings that can be used as directory names.
NOTE: Letter CASE is distinctive, i.e., 'Low' and 'low' are different categories.

*2: Load all test results into a PairedCompDataSet object:

ds = PairedCompDataSet.load(pcf, dir='~/sessions', groups=['NH', 'HI'], fmt='json')

The loaded data structure ds can then be used as input for analysis.

With data files saved in the 'json' format, the test conditions are defined in the file.
Therefore, the sub-directory names 'Low' and 'High' are not significant,
and need not agree with any test-condition labels in the PairedCompFrame object.
The directory names are then used only to facilitate the user's overview of files.

However, files in the older 'res' format do NOT define test conditions.
The test conditions are instead deduced from labels 'High' and 'Low',
one of which MUST be found as a sub-string in the full path-string identifying each file.

Therefore, in this case the category labels defined for test-factor 'SNR'
MUST be UNIQUE in the file paths.
For example, test_conditions = {'SNR': 'High' and 'Higher'}
can NOT be used with files saved in the 'res' format.
Test-condition labels can not be sub-strings of a group name,
because the group directory name is also included in the path-string.

*** Selecting Subsets of Data for Analysis:

It is possible to define a data set including only a subset of experimental data.
For example, assume we want to analyse only group 'HI':

ds_HI = PairedCompDataSet.load(pcf, groups=['HI'])

Or perhaps we want to look at results for only one test condition,
and only two of the three sound systems that have been tested.
Then we must define a new PairedCompFrame object before loading the data:

small_pcf = PairedCompFrame(systems = ['testA', 'testB'],  # only two of the sound processors
        attributes = ['Preference'],  # same single perceptual attribute
        test_conditions = {'SNR': ['High']}  # test factor SNR, now with only ONE category
        )
ds_AB_HI_High = PairedCompDataSet.load(small_pcf, groups =  ['HI'])

This will include all data with 'SNR' 'High', regardless of 'stim' category.

If there are files for other perceptual attributes in addition to 'Preference',
the analysis is restricted to the specified subset of attributes.

Any paired-comparisons for OTHER SYSTEMS, not explicitly named in small_pcf, will be DISREGARDED.
Any results for OTHER ATTRIBUTES, not explicitly listed here, will be DISREGARDED.
Any results having a desired test-factor category will be INCLUDED,
regardless of the category within any other test factor.

*** Version History:

2018-03-30, changed nesting structure to PairedCompDataSet.pcd[group][attribute][subject]
    because we learn one separate PairedCompGroupModel for each group and attribute.
    Allow missing subjects for some attributes;
    identical subjects needed only for attribute correlations.
2018-04-12, Allow systems_alias labels in PairedCompFrame
2018-08-10, renamed classes PairedCompRecord and new class StimRespItem
2018-08-10, include test condition in each StimRespItem, to facilitate EMA data input
2018-08-12, simplified PairedCompRecord structure: no redundant data,
    all general experimental info given only in PairedCompFrame
2018-08-13, simplified PairedCompDataSet structure
"""

# ****** assert UNIQUE systems, attributes, and test condition labels ??

import numpy as np
from pathlib import Path
from collections import OrderedDict, namedtuple
from itertools import product
import json
import logging

from PairedCompCalc import __version__
from . import pc_file_2002 as res


SESSION_FILE_FORMATS = ['res', 'json']  # 'pkl', 'xml' #?]
# accepted file-name suffixes for session data import


logger = logging.getLogger(__name__)


# ------------------------------------------------------ Exceptions:
class FileFormatError(RuntimeError):
    """Signal any form of file format error
    """


# ----------------------------------------------------------------------
StimRespItem = namedtuple('StimRespItem', 'S R T')
# S = a tuple of two strings identifying the test systems compared.
# R = an integer in  (-M, ..., 0, ..., +M), except that
#     R = 0 is allowed only in experiments with property forced_choice == False.
# T = a dict defining a Test Condition,
#     with zero or more elements (test_factor, tf_category),
#     where test_factor is a string label, and
#     tf_category is a string label identifying one category within test_factor.
# in python v 3.7: T may be omitted, using arg default=dict()


# ------------------------------------------------------------------
class PairedCompFrame:
    """Defines structure of one complete Paired-Comparison experiment.
    Data about test participants are NOT included.
    """
    def __init__(self,
                 attributes,
                 response_labels,
                 forced_choice=False,
                 systems=list(),
                 systems_alias=None,
                 test_conditions=list()
                 ):
        """Input:
        :param attributes: list of string labels for selected perceptual attributes
            Attribute labels must be strings that can be used as directory names.
        :param response_labels: (optional) list with ordinal difference-magnitude rating labels
            mainly informational, but the number of labels is needed for model learning
        :param forced_choice: (optional) boolean indicator that response NO Difference is not allowed.
        :param systems: (optional) list with unique string labels of systems being evaluated
            initialized from the first encountered data file, if not specified here
        :param systems_alias: (optional) sequence of systems labels used for displays
        :param test_conditions: (optional) iterable with elements (test_factor, category_list),
            where
            test_factor is a string,
            category_list is a list of labels for allowed categories within test_factor.
            A category label is normally just a single string,
                but may be a tuple of strings, for use by pc_file_2002.
            May be left empty, if only one test condition is used.

        NOTE: systems, attributes, and test_conditions may define a subset of
            data present in input data files.
        """
        self.systems = systems
        self.systems_alias = systems_alias
        assert len(set(attributes)) == len(attributes), 'Attribute labels must be unique'
        self.attributes = attributes
        self.response_labels = response_labels
        self.forced_choice = forced_choice
        self.test_conditions = OrderedDict(test_conditions)

    def __repr__(self):
        return (f'PairedCompFrame(\n\t' +
                ',\n\t'.join(f'{key}={repr(v)}'
                            for (key, v) in vars(self).items()) +
                '\n\t)')

    @property
    def n_systems(self):
        return len(self.systems)

    @property
    def systems_disp(self):
        """Systems labels for display"""
        if self.systems_alias is None:
            return self.systems
        else:
            return self.systems_alias[:self.n_systems]

    @property
    def n_attributes(self):
        return len(self.attributes)

    @property
    def n_response_labels(self):
        return len(self.response_labels)

    @property
    def n_test_factors(self):
        return len(self.test_conditions)

    @property
    def n_test_conditions(self):
        """1D list with number of test-condition alternatives in each test factor"""
        return [len(v) for v in self.test_conditions.values()]

    @property
    def n_test_condition_tuples(self):
        return np.prod(self.n_test_conditions, dtype=int)

    def test_condition_tuples(self):
        """generator of all combinations of one test_condition from each test_factor
        """
        # *********** property ? include key ?
        return product(*self.test_conditions.values())

    def gen_test_factor_category_tuples(self):
        """generator of dicts, with one dict for
        every combination of one category from each test_factor,
        needed by pc_simulator
        """
        tc_pairs = ([(tf, tf_c) for tf_c in tf_cats]
                    for (tf, tf_cats) in self.test_conditions.items())
        return product(*tc_pairs)

    @classmethod
    def load(cls, p):
        """Try to create instance from file saved earlier
        :param p: string file-path or Path instance, identifying a pre-saved json file
        :return: one new PairedCompFrame instance, if successful
        """
        try:
            with open(p, 'rt') as f:
                d = json.load(f)
            return cls(**d['PairedCompFrame'])
        except KeyError:
            raise FileFormatError(p + 'is not a saved PairedCompFrame object')

    def save(self, dir, file_name='pcf.json'):
        """dump self to a json serialized file dir ( file_name
        """
        dir = Path(dir)
        dir.mkdir(parents=True, exist_ok=True)
        p = (dir / file_name).with_suffix('.json')
        with p.open('wt') as f:
            json.dump({'PairedCompFrame': self.__dict__}, f,
                      indent=1, ensure_ascii=False)

    def accept(self, s):
        """Check that s properties agree with self properties,
        such that s should be included in desired PairedCompDataSet object.
        :param s: one PairedCompRecord instance
        :return: boolean True if s is accepted
        Result: self property systems updated, if not defined earlier.
        """
        # Update undefined fields from first encountered s:
        if len(self.systems) == 0 and len(s.result) > 0:
            self.systems = s.systems
        return (len(s.result) > 0 and
                set(self.systems) <= set(s.systems) and
                s.attribute in self.attributes
                )


# ------------------------------------------------------------
class PairedCompDataSet:
    """All result data for one complete paired-comparison experiment.
    Includes two properties:
    pcf = a PairedCompFrame instance, defining the experimental layout,
    pcd = a nested dict containing result data for all participants.
    """
    def __init__(self, pcf, pcd):
        """
        :param pcf: a single PairedCompFrame instance,
        :param pcd: nested dict with elements (group_id: group_data), where
            group_id s a group-name string equal to a directory name, and
            group_data is a dict with elements {attribute: attr_results}, where
            attribute is one of the string labels specified in pcf,
            attr_results is a dict with elements (subject_id: res), where
            subject_id is a string, and
            res is a list of StimRespItem objects, one for each presentation

        Thus, a single result list may be extracted from the pcd by nested dict indexing, e.g.,
        result = self.pcd[group][attr][subject]
        2018-08-14, simplified pcd nested dict structure; test-cond now inside StimRespItem
        """
        self.pcf = pcf
        self.pcd = pcd

    def __repr__(self):
        return 'PairedCompDataSet(pcf=pcf, pcd=pcd)'

    def __str__(self):
        n_subjects = {g: {a: sum(len(r) > 0 for (s, r) in a_subjects.items())
                          for (a, a_subjects) in g_attr.items()}
                      for (g, g_attr) in self.pcd.items()}
        # = subjects with non-empty pc result lists
        n_g = len(self.pcd)
        return ('PairedCompDataSet with ' + f'{n_g} '
                + ('groups' if n_g > 1 else 'group')
                + ' with data from \n'
                + '\n'.join([f' {n_s} subjects for attribute {repr(a)}'
                             + (f' in group {repr(g)}' if n_g > 1 else '')
                             for (g, g_attributes) in n_subjects.items()
                             for (a, n_s) in g_attributes.items()
                             ])
                + '\n')

    @classmethod
    def load(cls, pcf, dir, groups=None, fmt=None):
        """Create one class instance from selected session results.
        :param pcf: PairedCompFrame instance
        :param dir: string or Path defining top of directory tree with all data files.
        :param groups: (optional) list of group names,
            each element MUST be name of one immediate sub-directory of dir
        :param fmt: (optional) string with file suffix for data files.
            If undefined, all files are tried, so mixed file formats can be used as input.
        :return: a single cls object

        Arne Leijon, 2018-03-29, changed pcd nesting order
        2018-08-14, using simplified PairedCompRecord structure
        """
        def gen_records(dir, group):
            """generator of records to be included.
            :param dir: Path to directory containing session files
            :param group: sub-directory name in dir, OR None
            :return: iterator of PairedCompRecord instances,
                yielding only records accepted by pcf

            2018-08-12, pc_file_2002 does all job for res format
            """
            for f in _gen_file_paths(dir, group, fmt):
                try:
                    s = PairedCompRecord.load(f, pcf)
                    if s is not None and pcf.accept(s):
                        yield s
                except FileFormatError:
                    pass  # no problem, just try next file

        def gen_sr_items(s_record):
            """
            Generator of acceptable StimRespItem objects with properties matching pcf, and with
            T recoded to ensure it is an element of pcf.test_condition_tuples()
            :param s_record: a PairedCompRecord instance
            :return: generator yielding accepted StimRespItem objects, such that
                both elements in pair S are in pcf.systems, and
                T is a test-condition tuple which is an element of pcf.test_condition_tuples()
            """
            for r in s_record.result:
                tct = _matching_test_cond_tuple(r.T, pcf)
                if ((r.S[0] in pcf.systems and r.S[1] in pcf.systems)
                        and not response_outside_range(r.R)
                        and tct is not None):
                    # no warning here, might be filtered on purpose
                    yield StimRespItem(tuple(r.S), r.R, tct)

        def response_outside_range(r):
            """Check if a response is unacceptable, with the given pcf
            :param r: scalar integer response value
            :return: boolean True if r is NOT acceptable
            """
            if pcf.forced_choice:
                return r == 0 or abs(r) > pcf.n_response_labels
            else:
                return abs(r) >= pcf.n_response_labels

        # ----------------------------------------------------------
        assert (fmt in SESSION_FILE_FORMATS or
                fmt in ['', None]), 'Unknown session file format: ' + fmt
        dir = Path(dir)
        assert dir.exists(), f'{dir} does not exist'
        assert dir.is_dir(), f'{dir} is not a directory'
        if groups is None or len(groups) == 0:
            groups = ['']  # must be a list with at least one group label
        pcd = OrderedDict()
        # = space for all record results
        for g in groups:
            pcd[g] = {a: dict()
                      for a in pcf.attributes}
            for s in gen_records(dir, g):
                if any(response_outside_range(r.R) for r in s.result):
                    w = (f'Some Response(s) out of range for subject {repr(s.subject)}, ' +
                         f'attribute {repr(s.attribute)}')
                    logger.warning(w)
                try:
                    pcd[g][s.attribute][s.subject].extend(gen_sr_items(s))
                    # if several records have the same subject and attribute,
                    # results are concatenated, as if obtained from a single record
                except KeyError:
                    pcd[g][s.attribute][s.subject] = list(gen_sr_items(s))
                    # first record for this subject

        for (g, g_attributes) in pcd.items():
            for (a, a_subjects) in g_attributes.items():
                n_items = np.mean([len(s_res)
                                  for s_res in a_subjects.values()])
                log_str = (f'Collected group {repr(g)}, ' +
                           f'attribute {repr(a)}, ' +
                           f'with {len(a_subjects)} subjects, ' +
                           f'mean {n_items:.1f} items per subject')
                logger.info(log_str)
        return PairedCompDataSet(pcf, pcd)

    # def save(self, dir):  # ********** pickle ?
    #     """
    #     Save all PairedCompRecord objects in a directory tree with sub-trees for groups and attributes.
    #     :param dir: Path or string defining the top directory where files are saved
    #     :param fmt: string defining session format
    #     :return: None
    #     """
    #     raise NotImplementedError

    def ensure_complete(self):
        """Check that every subject has data for at least SOME test_conditions.
        NOTE: This condition has been relaxed with new hierarchical population prior.
        Parameters for missing data are influenced only by the population prior.
        Non-matching subject sets are allowed for different attributes.
        :return: None

        Result:
        self.pcd reduced: subjects with empty results deleted
        logger warnings for missing data.

        Arne Leijon, 2018-04-12
        2018-08-14, simplified test with simplified nested dict pcd
        """
        # *** check responses against pcf.response_labels and forced_choice, and log warning !

        for (g, g_attributes) in self.pcd.items():
            for (a, ga_subjects) in g_attributes.items():
                incomplete_subjects = set(s for (s, item_list) in ga_subjects.items()
                                          if len(item_list) == 0)
                for s in incomplete_subjects:
                    del self.pcd[g][a][s]
                    logger.warning(f'Subject {s} in group {repr(g)} excluded for attribute {repr(a)}; no data')
            # check if all attributes include the same subjects
            all_subjects = set.union(*(set(ss)
                                       for ss in g_attributes.values()))
            for (a, ga_subjects) in g_attributes.items():
                if len(ga_subjects) == 0:
                    raise RuntimeError(f'No subjects remaining in group {repr(g)} for attribute {repr(a)}')
                missing_subjects = all_subjects - set(ga_subjects)
                if len(missing_subjects) > 0:
                    logger.warning(f'{missing_subjects} missing for attribute {repr(a)} in group {repr(g)}')
                # ***** delete all missing subjects ???
                # ***** NO, we need matching subjects only for attribute correlations


# ------------------------------------------------------------
class PairedCompRecord:
    """Data structure for all results of one subject for one perceptual attribute.
    Only data needed for analysis are kept in explicitly named properties.
    Other values load-ed from a file are kept only to allow all to be saved if needed.
    """
    def __init__(self,
                 subject='',
                 attribute='',
                 result=list(),
                 **othr):
        """Input:
        :param subject: string with participant code id
        :param attribute: string describing tested perceptual attribute
        :param result: list of tuples like StimRespItem(S=[a, b], R=response, T=tc_dict(...)), where
            (a, b) are labels of presented pair
            response = integer in ( -n_response_labels,...,-1, +1, ...,  +n_response_labels
                if forced_choice.
                Here, response_label[abs(response)-1] is the chosen response.
            response = integer in ( -n_response_labels+1,...,0, ...,  +n_response_labels-1
                if not forced_choice.
                Here, response_label[abs(response)] is the chosen response.
            tc_dict = a dict with zero or more (test_factor, tf_category) elements
        :param othr: any data fields not used for analysis, but kept and saved
        """
        self.attribute = attribute
        self.subject = subject
        self.result = [StimRespItem(*r) for r in result]
        self.othr = othr

    def __repr__(self):
        return (f'PairedCompRecord(\n\t' +
                ',\n\t'.join(f'{key}={repr(v)}'
                            for (key, v) in vars(self).items()) +
                '\n\t)')

    @property
    def systems(self):
        """sorted list of system labels from all result elements
        """
        if len(self.result) == 0:
            return list()
        s_labels = set.union(*(set(r.S) for r in self.result))
        return sorted(list(s_labels))

    # @property
    # def n_systems(self):
    #     return len(self.systems)

    @classmethod
    def load(cls, p, pcf=None):
        """Create a PairedCompRecord instance by reading data from a file.
        :param p: string or Path instance for reading
        :param pcf: (optional) PairedCompFrame object, required only for .res format decoding
        :return: new cls instance, if file data was OK,

        Exception: FileFormatError, if any error occurred
        """
        p = Path(p)
        try:
            if p.suffix == '.res':
                with res.open_encoded_txt(p) as f:
                    p_dict = res.load(f, pcf)
            elif p.suffix == '.json':
                with p.open() as f:
                    p_dict = json.load(f)
            else:
                raise FileFormatError(p + ' file suffix unknown for PairedCompRecord data')
            p_dict = p_dict['PairedCompRecord']
            if '__version__' in p_dict.keys() and p_dict['__version__'] < __version__:
                _update_version_format(p_dict)
            return cls(**p_dict)
        except (KeyError, json.decoder.JSONDecodeError):
            # raise FileFormatError(p + ' does not contain PairedCompRecord data')
            logger.warning(f'File {str(p)} does not contain PairedCompRecord data')

    def save(self, dir, fmt='json', pcf=None):
        """Save session data to file for this subject
        :param dir: string or Path, identifying directory where new file is written
        :param fmt: suffix code for saved file format
            = 'res', Dahlqvist text file format from 2002
            = 'json', python json serial format
        :param pcf: (optional) PairedCompFrame object, required only for .res format encoding
        :return: None
        2018-08-12, include self.othr
        """
        #  ******** optional file path, in case subject id string cannot be used ???
        dir = Path(dir)
        dir.mkdir(parents=True, exist_ok=True)
        # make sure it exists, create new hierarchy if needed
        file_path = Path(dir) / (self.subject + '.' + fmt)
        with open(file_path, 'wt') as f:
            if fmt == 'res':
                res.save(self, f, pcf)
            elif fmt == 'json':
                self_dict = dict(((k, v) for (k, v) in self.__dict__.items() if k != 'othr'),
                                 **self.othr)
                self_dict['__version__'] = __version__
                self_dict = {'PairedCompRecord': self_dict}
                json.dump(self_dict, f)
            # elif fmt == 'ema':  #perhaps needed in the future
            #     ema.save(self,f)
            else:
                raise FileFormatError(f'Format {repr(fmt)} unknown for PairedCompRecord data')


# ---------------------------------------- module help functions
def _update_version_format(p_dict):
    """Update contents from an input json file to fit current PairedCompRecord version
    :param p_dict: a PairedCompRecord dict saved with an old package version
    :return: None
    """
    pass  # nothing to update


def _gen_file_paths(p, sub_dir=None, suffix=None):
    """generator of all file Paths in directory tree p, recursively, with desired name pattern
    :param p: Path instance defining top directory to be searched
    :param sub_dir: (optional) sub-directory name
    :param suffix: (optional) file suffix of desired files
    :return: iterator of Path objects, each defining one existing data file

    Arne Leijon, 2017-11-29
    """
    if sub_dir is not None and len(sub_dir) > 0:
        p = p / sub_dir  # search only in sub_dir
    if suffix is None or suffix == '':
        glob_pattern = '*.*'  # read any file types
    else:
        glob_pattern = '*.' + suffix  # require suffix
    return (f for f in p.rglob(glob_pattern) if f.is_file())


def _matching_test_cond_tuple(tcd, pcf):
    """Create a test_conc_tuple from a given test-condition dict from PairedCompRecord result,
    that matches a required test-condition dict defined in a PairedCompFrame object
    :param tcd: dict with elements (test_factor, tf_cat), where
        test_factor is a string, tf_cat is a string or tuple
    :param pcf: a PairedCompFrame object, with
        pcf.test_conditions = an OrderedDict with elements (test_factor, list of tf_cat items)
    :return: tct = tuple (tf_cat_0, tf_cat_1, ...),
        where tf_cat_n is the tf_cat from tcd matching one of the n-th test_factor categories
        len(tct) == len(pcf_tc)
        All test-factors required in pcf must be defined in tcd,
        but the tcd may include additional (test_factor, value) pairs.
        tct = None if not all required test-factors were found.
    NOTE: this implies that tct is guaranteed to be one element of pcf.test_cond_tuples()
    """
    try:
        tct = [tf_cats[tf_cats.index(tcd[tf])]
               for (tf, tf_cats) in pcf.test_conditions.items()]
        # tcd[tf] raises KeyError if tf is not present in tcd
        # tf_cats.index(...) raises ValueError if tcd[tf] does not match
        return tuple(tct)
    except (KeyError, ValueError):
        return None
