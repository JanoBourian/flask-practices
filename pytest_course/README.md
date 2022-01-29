# Course description

https://www.udemy.com/course/pytest-course/

# a overview:

- Test functions 

- Markers 

- Skip, Skiplf 

- Fixtures 

- Parametrize 

# Basics 

```
pytest . 
pytest file.py -v
```

## skip 

```
@pytest.mark.skip
@pytest.mark.skipif(4>1, reason ="Skipped because 4 > 1")
@pytest.mark.skipif(3>10, reason ="Skipped because 4 > 1")
```

# XFAIL 

I don't care if this test fails.

```
@pytest.mark.xfail # XFAIL
@pytest.mark.xfail # XPASS
```

# Marks and warnings 

```
@pytest.mark.slow 
pytest file.py -v -p no:warnings
```

# If you want run test with specific mark 

```
pytest file.py -v -p no:warnings -m slow
pytest file.py -v -p no:warnings -m skip
pytest file.py -v -p no:warnings -m skipif
pytest file.py -v -p no:warnings -m "not slow"
```