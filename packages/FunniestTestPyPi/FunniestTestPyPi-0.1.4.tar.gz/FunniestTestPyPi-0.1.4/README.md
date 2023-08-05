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
```

## Register and upload to PyPI

Within the top level project directory run

```
python setup.py register sdist bdist_wininst upload
```

More information can be found [here](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html). Alternatively, the package can be registered to PyPI with [twine](https://github.com/pypa/twine) by following these [instructions](https://gist.github.com/gboeing/dcfaf5e13fad16fc500717a3a324ec17).

```
pip install twine
twine register dist/project-x.y.z.tar.gz
twine register dist/mypkg-0.1-py2.py3-none-any.whl
twine upload dist/*
```

## Useful sites

* https://stackoverflow.com/questions/4249974/personal-git-repository#
* https://www.wired.com/2010/02/set_up_a_home_server/
* https://python-packaging.readthedocs.io/en/latest/minimal.html
* https://packaging.python.org/guides/migrating-to-pypi-org/
* https://stackoverflow.com/questions/40022710/how-am-i-supposed-to-register-a-package-to-pypi
* https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html
* https://gist.github.com/gboeing/dcfaf5e13fad16fc500717a3a324ec17
* https://stackoverflow.com/questions/16403229/how-do-you-configure-pypi-under-windows
* https://docs.python.org/3/distutils/packageindex.html#package-index
* https://gist.github.com/ibrahim12/c6a296c1e8f409dbed2f
* https://github.com/pypa/twine
* https://stackoverflow.com/questions/18216991/create-a-tag-in-github-repository
* https://github.com/fhamborg/news-please/wiki/PyPI---How-to-upload-a-new-version

## Future Work

Focus on building *good* projects by using [repository badges](https://github.com/dwyl/repo-badges), especially those focused on documentation, build, and coverage. Follow the [chempy](https://github.com/bjodah/chempy) Python project as a good guide.
