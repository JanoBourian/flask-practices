import pytest 

def raise_covid19_exception() -> None:
    raise ValueError("Coronavirus Exception")

def test_raise_covid19_exception_should_pass() -> None: 
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "Coronavirus Exception" == str(e.value)