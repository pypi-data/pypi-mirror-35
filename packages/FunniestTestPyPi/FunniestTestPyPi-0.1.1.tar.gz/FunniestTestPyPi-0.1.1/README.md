# FunniestTestPyPi [![PyPI](https://img.shields.io/pypi/pyversions/fire.svg?style=plastic)](https://github.com/MaxMifkovic/FunniestTestPyPi)
Practice creating a Python package and adding it to PyPi

## Instructions for adding future packages

## File contents

This portion of instructions is taken from [here](https://gist.github.com/gboeing/dcfaf5e13fad16fc500717a3a324ec17).

### /project/package/\_\_init\_\_.py

```python
from .module import *
__version__ = '0.1'
```

### /project/package/module.py

```python
# this file just contains your module's code
```

### /project/setup.py

```python
from setuptools import setup
setup(name='module',
      version='0.1',
      description='What the module does',
      url='https://github.com/username/repo',
      author='Your Name',
      author_email='email@domain.net',
      license='MIT',
      packages=['module'],
      install_requires=['numpy>=1.11',
                        'matplotlib>=1.5'])
```

#### .pypirc

If this is the first time adding a package to the Python Package Index (PyPI), then it is necessary to create a `.pypirc` file. This is located at `%HOMEPATH%\.pypirc` for Windows users and `~/.pypirc` for Mac and \*nix users. An example `.pypirc` file (found [here](https://stackoverflow.com/questions/40022710/how-am-i-supposed-to-register-a-package-to-pypi)) is

```python
[distutils]
index-servers =
    pypi
    pypitest

[pypi]
repository=https://pypi.org
username=[your username]
password=[your password]

[pypitest]
repository=https://test.pypi.org
username=[your username]
password=[your password]

## Temp Header
