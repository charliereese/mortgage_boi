# Description

mortgage-boi is a python package for calculating mortgage data and cash flows.

# Creating a build

First, update the version number in setup.py.

Then, in the root folder:

`python setup.py sdist bdist_wheel`

In the root folder:

# Uploading a build

Prod:
`python -m twine upload dist/*`

Test:
`python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

# Installing the package

See https://packaging.python.org/tutorials/packaging-projects/

# Useful information for building packages:

- [what is __init__.py for](https://stackoverflow.com/questions/448271/what-is-init-py-for)
