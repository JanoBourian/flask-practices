import pytest
from Company import Company

def test_our_first_test() -> None:
    assert 1 == 2

@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 3 != 2

@pytest.mark.skipif(4>1, reason ="Skipped because 4 > 1")
def test_should_be_skipped_if() -> None: 
    assert 1 == 2
    
@pytest.mark.skipif(3>10, reason ="Skipped because 4 > 1")
def test_should_be_skipped_if_second() -> None: 
    assert 1 == 2

@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1 == 2
    
@pytest.mark.xfail
def test_dont_care_if_fails_but_not_fail() -> None:
    assert 1 == 1

@pytest.mark.slow 
def test_slow() -> None:
    assert 1 ==2
    
def test_correct_assert() -> None:
    assert 1 == 1

