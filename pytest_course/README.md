# Course description

https://www.udemy.com/course/pytest-course/

# a overview:

- Test functions 
- Markers 
- Skip, Skiplf 
- Fixtures 
- Parametrize 

# Basics 

```python:
pytest . 
pytest file.py -v
``` 

## skip 

```python:
@pytest.mark.skip
@pytest.mark.skipif(4>1, reason ="Skipped because 4 > 1")
@pytest.mark.skipif(3>10, reason ="Skipped because 4 > 1")
```

# XFAIL 

I don't care if this test fails.

```python:
@pytest.mark.xfail # XFAIL
@pytest.mark.xfail # XPASS
```

# Marks and warnings 

```python:
@pytest.mark.slow 
pytest file.py -v -p no:warnings
```

# If you want run test with specific mark 

```python:
pytest file.py -v -p no:warnings -m slow
pytest file.py -v -p no:warnings -m skip
pytest file.py -v -p no:warnings -m skipif
pytest file.py -v -p no:warnings -m "not slow"
```

# If you need previous configurations

```python:
@pytest.fixture
```

# If you want send more test with parameters 

```python:
@pytest.mark.parametrize(
    "company_name",
    ["Tik Tok", "Instagram", "Twitch"],
    ids = ["TIKTOKTEST", "INSTAGRAMTEST", "TWITCHTEST"],
    )

@pytest.mark.parametrize(
    "company_object",
    [
        {"name": "Twitter", "stock_symbol":"TWT"},
        {"name": "Facebook", "stock_symbol":"FB"},
        {"name": "Coca cola", "stock_symbol":"CCL"},
        {"name": "Moderna" , "stock_symbol": "MDN"},
        {"name": "Pepsi", "stock_symbol": "PPS"},
    ],
    ids=["TW", "FB", "CC", "MD", "PS"],
)
def test_objects(company_object:list)->None:
    company = Company(company_object['name'], company_object['stock_symbol'])
    assert str(company) == f"{company.name}:{company.stock_symbol}"
```

# The new way to test

```
pytest -v -s --durations=0
pytest -v -s -k test_raise_covid19_exception_should_pass
pytest -v -s -k "logged"
pytest -v -s --durations=0 -k "create"
pytest -v -s --durations=0 -k "test and not zero"
pytests path::TestClass::TestMethod
pytest -v -s --durations=0 -m xfail
```