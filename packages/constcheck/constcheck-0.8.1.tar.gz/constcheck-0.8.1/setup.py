# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['constcheck']

package_data = \
{'': ['*']}

install_requires = \
['arcon>=0,<1', 'object-colors>=2.0.1,<3.0.0', 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['constcheck = constcheck.__main__:main']}

setup_kwargs = {
    'name': 'constcheck',
    'version': '0.8.1',
    'description': 'Check Python files for repeat use of strings',
    'long_description': 'constcheck\n==========\n.. image:: https://img.shields.io/badge/License-MIT-yellow.svg\n    :target: https://opensource.org/licenses/MIT\n    :alt: License\n.. image:: https://img.shields.io/pypi/v/constcheck\n    :target: https://pypi.org/project/constcheck/\n    :alt: PyPI\n.. image:: https://github.com/jshwi/constcheck/actions/workflows/ci.yml/badge.svg\n    :target: https://github.com/jshwi/constcheck/actions/workflows/ci.yml\n    :alt: CI\n.. image:: https://results.pre-commit.ci/badge/github/jshwi/constcheck/master.svg\n   :target: https://results.pre-commit.ci/latest/github/jshwi/constcheck/master\n   :alt: pre-commit.ci status\n.. image:: https://github.com/jshwi/constcheck/actions/workflows/codeql-analysis.yml/badge.svg\n    :target: https://github.com/jshwi/constcheck/actions/workflows/codeql-analysis.yml\n    :alt: CodeQL\n.. image:: https://codecov.io/gh/jshwi/constcheck/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/jshwi/constcheck\n    :alt: codecov.io\n.. image:: https://readthedocs.org/projects/constcheck/badge/?version=latest\n    :target: https://constcheck.readthedocs.io/en/latest/?badge=latest\n    :alt: readthedocs.org\n.. image:: https://img.shields.io/badge/python-3.8-blue.svg\n    :target: https://www.python.org/downloads/release/python-380\n    :alt: python3.8\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n    :alt: Black\n.. image:: https://img.shields.io/badge/linting-pylint-yellowgreen\n    :target: https://github.com/PyCQA/pylint\n    :alt: pylint\n\nCheck Python files for repeat use of strings\n--------------------------------------------\n\nEscape commas with \\\\\\\\ (\\\\ when enclosed in single quotes)\n\nDefaults can be configured in your pyproject.toml file\n\nInstallation\n------------\n\n.. code-block:: console\n\n    $ pip install constcheck\n\nUsage\n-----\n\nCommandline\n***********\n\n.. code-block:: console\n\n    usage: constcheck [-h] [-v] [-n] [-c INT] [-l INT] [-s STR] [-i LIST] [-I LIST]\n                                 [--ignore-from [FILE=LIST [FILE=LIST ...]]]\n                                 [path [path ...]]\n\n    positional arguments:\n      path                                       path(s) to check files for (default: .)\n\n    optional arguments:\n      -h, --help                                 show this help message and exit\n      -v, --version                              show version and exit\n      -n, --no-ansi                              disable ansi output\n      -c INT, --count INT                        minimum number of repeat strings (default: 3)\n      -l INT, --length INT                       minimum length of repeat strings (default: 3)\n      -s STR, --string STR                       parse a string instead of a file\n      -i LIST, --ignore-strings LIST             comma separated list of strings to exclude\n      -I LIST, --ignore-files LIST               comma separated list of files to exclude\n      --ignore-from [FILE=LIST [FILE=LIST ...]]  comma separated list of strings to exclude from file\n\nAPI\n***\n\n.. code-block:: python\n\n    >>> from constcheck import constcheck\n\n.. code-block:: python\n\n    >>> EXAMPLE = """\n    ... STRING_1 = "Hey"\n    ... STRING_2 = "Hey"\n    ... STRING_3 = "Hey"\n    ... STRING_4 = "Hello"\n    ... STRING_5 = "Hello"\n    ... STRING_6 = "Hello"\n    ... STRING_7 = "Hello"\n    ... STRING_8 = "Hello, world"\n    ... STRING_9 = "Hello, world"\n    ... STRING_10 = "Hello, world"\n    ... STRING_11 = "Hello, world"\n    ... STRING_12 = "Hello, world"\n    ... """\n\n.. code-block:: python\n\n    >>> constcheck(string=EXAMPLE)\n    3   | Hey\n    4   | Hello\n    5   | Hello, world\n    <BLANKLINE>\n    1\n\nWith the ``count`` argument\n\n.. code-block:: python\n\n    >>> constcheck(string=EXAMPLE, count=4)\n    4   | Hello\n    5   | Hello, world\n    <BLANKLINE>\n    1\n\nWith the ``length`` argument\n\n.. code-block:: python\n\n    >>> constcheck(string=EXAMPLE, length=6)\n    5   | Hello, world\n    <BLANKLINE>\n    1\n\nWith the ``ignore_strings`` argument which accepts ``list`` of ``str`` objects\n\n.. code-block:: python\n\n    >>> constcheck(string=EXAMPLE, ignore_strings=["Hello, world", "Hello"])\n    3   | Hey\n    <BLANKLINE>\n    1\n\nConfig\n******\n\nAll keyword arguments available to ``constcheck()`` can be configured in the pyproject.toml file\n\n.. code-block:: toml\n\n    [tool.constcheck]\n    path = "."\n    count = 3\n    length = 3\n    ignore_strings = ["Hello", "Hello, world"]\n    ignore_files = ["tests/__init__.py"]\n    filter = false\n    no_color = false\n\n    [tool.constcheck.ignore_from]\n    "tests/__init__.py" = ["Hello, world"]\n\npre-commit\n##########\n\n`constcheck` can be used as a `pre-commit <https://pre-commit.com>`_ hook\n\nIt can be added to your .pre-commit-config.yaml as follows:\n\n.. code-block:: yaml\n\n    repos:\n      - repo: https://github.com/jshwi/constcheck\n        rev: v0.7.0\n        hooks:\n          - id: constcheck\n            args:\n              - "--count"\n              - "3"\n              - "--length"\n              - "3"\n',
    'author': 'jshwi',
    'author_email': 'stephen@jshwisolutions.com',
    'maintainer': 'jshwi',
    'maintainer_email': 'stephen@jshwisolutions.com',
    'url': 'https://pypi.org/project/constcheck/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
