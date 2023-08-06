__version__ = '0.0.1'

import sys
import traceback

GLOBAL_FLAGS = set()
TEST_ALL = False
TEST_LOG = {}

class TestResult(object):
    def __init__(self, name, passed, message=""):
        self.name = name
        self.passed = passed
        self.message = message

    def flush(self, index):
        return "TEST #{} - {}: {}\n{}".format(index, self.name, "PASS" if self.passed else "FAIL", \
            "\n".join(["  " + _ for _ in self.message.split("\n")]))

class ETestException(BaseException):
    pass

def expect_true(x):
    if not x:
        raise ETestException("expected to be True but get False")
    return x

def expect_false(x):
    if x:
        raise ETestException("expected to be False but get True")
    return x

def expect_equal(x, y):
    if x != y:
        raise ETestException("expected to be equal but get {} and {}".format(x, y))

def set_etest_flags(flags=set(), test_all=False):
    global GLOBAL_FLAGS, TEST_ALL
    GLOBAL_FLAGS = flags.copy()
    TEST_ALL = test_all

def get_etest_results():
    global GLOBAL_FLAGS, TEST_ALL, TEST_LOG
    if TEST_ALL:
        keys = {_[0] for _ in TEST_LOG}
    else:
        keys = GLOBAL_FLAGS.copy()

    print("ETEST RESULT: {}/{}\n".format( \
        len(list(filter(lambda x: TEST_LOG[x].passed, TEST_LOG))), len(TEST_LOG)) + "=" * 60)
    for key in keys:
        test_keys = list(filter(lambda x: x[0] == key, TEST_LOG))
        n_success = len(list(filter(lambda x: TEST_LOG[x].passed, test_keys)))
        n_total = len(test_keys)
        print("({}): {}/{}\n{}\n".format(key, n_success, n_total,
            "\n".join(["  " + TEST_LOG[test_key].flush(index) for index, test_key in enumerate(test_keys)])))

def etest(_flag, *args, **kwargs):
    def core(test):
        global GLOBAL_FLAGS, TEST_LOG, TEST_ALL
        if _flag in GLOBAL_FLAGS or TEST_ALL:
            try:
                test(*args, **kwargs)
            except ETestException as e:
                _, _, tb = sys.exc_info()
                tb_info = traceback.extract_tb(tb)
                filename, line, func, text = tb_info[-2]
                message = '  => {} - line {} <{}>: {}\n  =>   \"{}\"'.format(filename, line, func, text, e.args[0])
                passed = False
            else:
                message = ""
                passed = True
            name = test.__name__
            TEST_LOG[(_flag, name)] = TestResult(name, passed, message)
    return core

