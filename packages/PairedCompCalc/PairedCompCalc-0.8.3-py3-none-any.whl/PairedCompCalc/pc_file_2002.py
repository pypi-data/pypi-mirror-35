"""Functions to load / dump Paired-comparison test results,
stored in serialized text form,
using file format defined by Martin Dahlquist, 2002

Data for one session are represented by a dict = { 'PairedCompRecord': data },
where data is a dict with (key, value) pairs representing
a PairedCompRecord object, as defined in module pc_data.

Functions load, dump are analogous to corresponding json functions

*** Version History:
2018-02-18, allow test-condition code to be tuple of strings OR a single string
2018-08-12, fix  for simplified PairedCompRecord structure
"""

from pathlib import Path
import datetime as dt


# ------------------------------------------ Exception:
class FileFormatError(RuntimeError):
    """Signal any form of file format error when reading
    """


class PairedCompRecord2002:
    """PairedCompRecord variant with default values for all required fields
    which are not present in general PairedCompRecord
    NOTE: could not subclass pc_data.PairedCompRecord because of circular import problem
    """
    def __init__(self,
                 subject,
                 attribute,
                 systems,
                 result,
                 # forced_choice,
                 comment='No comment',
                 response_labels=None,
                 time_stamp=None,
                 **skip  # any other data just disregarded
                 ):
        self.subject = subject
        self.attribute = attribute
        self.systems = systems
        self.result = result
        self.comment = comment
        self.response_labels = response_labels
        self.time_stamp = time_stamp
        if self.response_labels is None:
            r_min = min(abs(r_i[1]) for r_i in self.result)
            r_max = max(abs(r_i[1]) for r_i in self.result)
            self.response_labels = [f'Diff{i}' for i in range(r_min, r_max+1)]
        if self.time_stamp is None or self.time_stamp == '':
            t = dt.datetime.now()
            self.time_stamp = f'{t.year}-{t.month:02d}-{t.day:02d} {t.hour:02d}:{t.minute:02d}'

    def __repr__(self):
        return (f'PairedCompRecord2002(\n\t' +
                ',\n\t'.join(f'{key}={repr(v)}'
                            for (key, v) in vars(self).items()) +
                '\n\t)')


def save(pcr, f, pcf):
    """Save a pc_data.PairedCompRecord instance in old 2002 format
    :param pcr: one pc_data.PairedCompRecord instance
    :param f: open file object for writing
    :return: None
    NOTE: this does not handle test_conditions !
    """
    # convert it to old-class object
    pcr2002 = PairedCompRecord2002(subject=pcr.subject,
                                   systems=pcr.systems,
                                   attribute=pcr.attribute,
                                   result=pcr.result,
                                   **pcr.othr)

    pcr_dict = {'PairedCompRecord': pcr2002.__dict__}
    dump(pcr_dict, f, pcf.forced_choice)


def dump(session_dict, f, forced_choice):
    """write a complete result for one PairedCompRecord2002
    in ORCA text format, as defined by Dahlquist, 2002
    :param session_dict: { 'PairedCompRecord': s }, where
        s includes properties for one PairedCompRecord2002 object,
        obtained, e.g., as s.__dict__
    :param f: file-like object, allowing f.write() operations
        If already existing, the f is over-written without warning
    :param forced_choice: boolean = pc_data.PairedCompFrame.forced_choice
    :return: None
    Exceptions: KeyError is raised if session_dict does not include required data.
    """
    s = session_dict['PairedCompRecord']
    with f:
        f.write(s['comment'] + '\n')
        f.write(s['subject'] + '\n')
        # t = s.time_stamp
        f.write(s['time_stamp'] + '\n')
        f.write(s['attribute'] + '\n')
        response_labels = s['response_labels']
        f.write(''.join('\"' + m + '\"\n' for m in response_labels))
        systems = s['systems']
        n_systems = len(systems)
        f.write(f'{n_systems},{len(response_labels)},2\n')
        f.write(''.join(sys +'\n' for sys in systems))
        f.write('\"matris\"\n')
        # ***** calculate summary matrix ********************
        for n in range(n_systems):
            f.write(','.join(['0' for m in range(n_systems)]) + '\n')
            # *** just a zero matrix, not used for analysis anyway
        result = s['result']
        f.write('\"antal stimuli\"\n' +
                f'{len(result)}\n')
        f.write('\"Stim1\",\"Stim1\",\"Resp\",\"Rate\",\"Rep\"\n')
        for sr in result:
            ((a, b), r) = sr[0:2]
            (i, j) = (systems.index(a), systems.index(b))
            choice = (0 if r == 0 else 2 if r > 0 else 1)
            # magn = abs(r) if s['forced_choice'] else 1 + abs(r)
            magn = abs(r) if forced_choice else 1 + abs(r)
            # NOTE: for historical reasons, magn must be
            # index into response_labels, using MatLab:s origin-one indexing.
            # Therefore, magn must always be 1, 2, etc. never = 0.
            f.write(f'{1+i},{1+j},{choice},{magn},0\n')


def load(f, pcf):
    """Read one session from file saved in old res format
    as defined by Martin Dahlquist, 2002
    :param f: open file object, allowing r.readline() operations
    :param pcf: pc_data.PairedCompFrame object, must be supplied by caller
    :return: dict with PairedCompRecord attributes from file,
        OR None, if any error encountered
    2018-08-12, new argument pcf
    """
    def clean(s):
        """strip away unwanted characters from a string
        :param s: string
        :return: cleaned string
        """
        clean_s = s.strip('\n\"')
        if len(clean_s) == 0:
            raise FileFormatError(f'Unexpected empty line in {f_name}')
        else:
            return clean_s

    def decode_res(r, systems, tc):
        """recode response item from res format to PairedCompRecord standards
        :param r: one paired-comparison result line (stim_1, stim_2, choice, magn)
        :param systems: list of string labels, corresponding to system indices in r
        :param tc: dict with (test_factor, tf_category) elements
        :return: tuple (pair, response) in PairedCompRecord format, where
            pair = tuple of system string labels (A, B) for presented pair
            response = integer in {- max_difference,..., + max_difference}
        """
        (i,j, choice, m) = r[:4]
        pair = (systems[i-1], systems[j-1])  # index origin 1 in res file
        # m = (0 if choice == 0 else m-1 if forced_choice else m)
        if choice == 0:
            m = 0
        elif not pcf.forced_choice:
            m -= 1  # invert the change in function dump
        if choice == 1:
            m = - m
        elif choice < 0 or choice > 2:
            raise FileFormatError(f'Illegal choice value in result in {f_name}')
        return (pair, m, tc)
    # -----------------------------------------
    f_name = f.name
    test_cond = decode_test_condition(f_name, pcf.test_conditions)
    s = dict()  # dict for result
    with f:
        # s['forced_choice'] = pcf.forced_choice
        # not saved in 2002 file format
        s['comment'] = clean(f.readline())
        s['subject'] = clean(f.readline())
        s['time_stamp'] = clean(f.readline())
        a = clean(f.readline())
        a = a.replace('\"', '')
        a = a.replace(',', ' ')
        s['attribute'] = a.split(sep=' ')[0]
        s['response_labels'] = r_labels = []
        while True:
            l = f.readline()
            if 0 == l.find('\"'):
                r_labels.append(clean(l))
            else:
                nsr = [int(n) for n in l.split(sep=',')]
                (n_systems, n_resp) = nsr[:2]
                break
        if n_resp != len(r_labels):
            raise FileFormatError(f'Inconsistent number of response labels in {f_name}')
            # ******* logger.warning is enough ?
        s['systems'] = systems = [clean(f.readline())
                                  for n in range(n_systems)]
        if 0 != (f.readline()).find('\"matr'):
            raise FileFormatError(f'matrix label not found in {f_name}')
        s['summary'] = [[int(n) for n in f.readline().split(sep=',')]
                        for n in range(n_systems)]
        l = f.readline()
        if (0 != l.find('\"num') and
            0 != l.find('\"ant')):
            raise FileFormatError(f'Number of results not found in {f_name}')
        n_pres = int(f.readline())
        s['result'] = result = []
        l = f.readline()
        if 0 != l.find('\"Stim'):
            raise FileFormatError(f'Unexpected result header in {f_name}')
        l = f.readline()
        while 0 < len(l):  # read until EOF
            r = [int(n) for n in l.split(sep=',')]
            result.append(decode_res(r, systems, test_cond))
            l = f.readline()
        if n_pres != len(result):
            raise FileFormatError(f'Inconsistent number of results in {f_name}')
        # if any(abs(r[1]) >= len(r_labels) for r in result):
        #     raise FileFormatError(f'Response outside response_labels in {f_name}')
        # ****** this check must consider forced_choice *******
        if pcf.forced_choice and any(r[1] == 0 for r in result):
            raise FileFormatError(f'Expected forced_choice, but found zero response in {f_name}')
        return {'PairedCompRecord': s}
        # --------------------- OK: whole file has been read without problem


def decode_test_condition(path, test_conditions):
    """Find test-condition labels as sub-strings of the path string.
    This is needed because session data in 2002 format do not define
    the test condition.

    :param path: Path instance, or path string, for file with saved session data
    :param test_conditions: dict with (test_factor: tc_alternatives) pairs, where
        test_factor is a string label for one desired factor
        tc_alternatives is a list with possible categories within this factor.

    :return: test_cond = dict with (test_factor: tf_category) pairs, where
        test_factor is one of the test-factor keys in test_conditions, and
        tf_category is the first string element in tc_alternatives for which
        a matching sub-string was found in path.

    Arne Leijon, 2017-12-01
    """
    def test_cond_in_file(tc, path):
        """Check if tc agrees with file path string
        :param tc: test-condition code, string or tuple of strings
        :param path: string path
        :return: boolean True if a match was found
        """
        if isinstance(tc, str):
            return tc in path
        elif type(tc) is tuple:
            return all(tc_i in path for tc_i in tc)
        else:
            return False
        # ----------------------------------------

    test_cond = dict()  # collector for found results
    for tf in test_conditions:
        for tc in test_conditions[tf]:
            # if tc in str(path):
            # **************** allow tc to be a tuple of strings ******************
            if test_cond_in_file(tc, str(path)):
                test_cond[tf] = tc
                break
    return test_cond


def open_encoded_txt(path):
    """Try to open a text file with a working encoding
    :param path: Path object or path string identifying a file
    :return: open file object
        OR None, if no working encoding was found

    Method: just try some encodings until a working one is found
    """
    encodings = ['utf-8', 'ISO-8859-1']
    for enc in encodings:
        try:
            with open(path, mode='rt', encoding=enc) as f:
                l = f.read()
            # No error: OK
            return open(path, mode='rt', encoding=enc)
            # open it again with right encoding
        except ValueError as e:
            pass  # try next encoding instead
    raise FileFormatError(f'Unknown text encoding in {path}')


# ------------------------------------------- TEST:

if __name__ == '__main__':

    print('\n*** Test decode_test_condition\n')
    top_dir = '../pc_sim'
    p = Path(top_dir) / 'Bradley' / 'Higher' / 'Subject0.res'
    pcf_tc = {'Model': ['Bradley', 'Thurstone', 'Real'],
              'SNR': ['Low', 'High']}

    tc = decode_test_condition(p, pcf_tc)
    print('pcf.test_conditions: ', pcf_tc)
    print('file: ',p )
    print('test_condition: ', tc)
