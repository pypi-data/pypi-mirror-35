# ERIPY

This package contains commonly useful functions and modules for data science purposes at Elder Research, Inc.


## Submodules

What is provided here is simply a high-level discussion of what is avilable in `eri`. For detailed instructions, please refer to the sub-module-level `README` files, and, of course, the function documentation. If any of the above does not exist, please seek out the author and shame them mercilessly


### `eri.clean`

Useful functions for cleaning your data (usually assumes `pandas` data frames).


### `eri.config`

Shared configuration details.


### `eri.html`

HTML parsing and munging utilities.


### `eri.validate`

Useful functions for validating the data we have (often just logging useful facts about a particular dataframe).


## Testing

to test, install `pytest` and `coverage` and then run the following:

``` python
# run all tests
coverage run -m pytest
```

``` python
# print coverage statistics
coverage report -m
```

## Deploying to `PyPi`

I'm using `twine`. Instructions are [here](https://github.com/pypa/twine). to summarize, though:

``` bash
python setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload --skip-existing dist/*
twine upload --skip-existing -r eri dist/*
```
