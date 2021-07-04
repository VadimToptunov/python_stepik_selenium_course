import pytest

"""
 pytest.mark.xfail(condition=None, *, reason=None, raises=None, run=True, strict=False)

 Parameters:

 - condition (bool or str) – Condition for marking the test function as xfail (True/False 
 or a condition string). If a bool, you also have to specify reason (see condition string).

 - reason (str) – Reason why the test function is marked as xfail.

 - raises (Type[Exception]) – Exception subclass expected to be raised by the test function; 
 other exceptions will fail the test.

 - run (bool) – If the test function should actually be executed. If False, the function will 
 always xfail and will not be executed (useful if a function is segfaulting).

 - strict (bool) – If False (the default) the function will be shown in the terminal output as xfailed 
 if it fails and as xpass if it passes. In both cases this will not cause the test suite to fail as a whole. 
 This is particularly useful to mark flaky tests (tests that fail at random) to be tackled later.

 If True, the function will be shown in the terminal output as xfailed if it fails, but if it unexpectedly passes 
 then it will fail the test suite. This is particularly useful to mark functions that are always failing and there 
 should be a clear indication if they unexpectedly start to pass (for example a new release of a library fixes a 
 known bug).
"""

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False