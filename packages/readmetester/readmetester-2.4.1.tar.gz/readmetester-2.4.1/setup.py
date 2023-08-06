# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['readmetester']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2.8.1,<3.0.0',
 'object-colors>=2.0.0,<3.0.0',
 'pyproject-parser>=0.4.3,<0.8.0',
 'restructuredtext-lint>=1.4.0,<2.0.0']

entry_points = \
{'console_scripts': ['readmetester = readmetester.__main__:main']}

setup_kwargs = {
    'name': 'readmetester',
    'version': '2.4.1',
    'description': 'Parse, test, and assert RST code-blocks',
    'long_description': 'readmetester\n============\n.. image:: https://img.shields.io/badge/License-MIT-yellow.svg\n    :target: https://opensource.org/licenses/MIT\n    :alt: License\n.. image:: https://img.shields.io/pypi/v/readmetester\n    :target: https://pypi.org/project/readmetester/\n    :alt: PyPI\n.. image:: https://github.com/jshwi/readmetester/actions/workflows/ci.yml/badge.svg\n    :target: https://github.com/jshwi/readmetester/actions/workflows/ci.yml\n    :alt: CI\n.. image:: https://results.pre-commit.ci/badge/github/jshwi/readmetester/master.svg\n   :target: https://results.pre-commit.ci/latest/github/jshwi/readmetester/master\n   :alt: pre-commit.ci status\n.. image:: https://github.com/jshwi/readmetester/actions/workflows/codeql-analysis.yml/badge.svg\n    :target: https://github.com/jshwi/readmetester/actions/workflows/codeql-analysis.yml\n    :alt: CodeQL\n.. image:: https://codecov.io/gh/jshwi/readmetester/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/jshwi/readmetester\n    :alt: codecov.io\n.. image:: https://readthedocs.org/projects/readmetester/badge/?version=latest\n    :target: https://readmetester.readthedocs.io/en/latest/?badge=latest\n    :alt: readthedocs.org\n.. image:: https://img.shields.io/badge/python-3.8-blue.svg\n    :target: https://www.python.org/downloads/release/python-380\n    :alt: python3.8\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n    :alt: Black\n.. image:: https://img.shields.io/badge/linting-pylint-yellowgreen\n    :target: https://github.com/PyCQA/pylint\n    :alt: pylint\n\nParse, test, and assert RST code-blocks\n---------------------------------------\n\n**Installation**\n\n.. code-block:: console\n\n    $ pip install readmetester\n..\n\n**Usage**\n\n``readmetester [-h] [--version] [README.rst]``\n\nIf a README.rst file is present in the current working directory it will be used if no arguments are provided\n\n.. code-block:: console\n\n    $ readmetester README.rst\n..\n\n**Documenting**\n\nPython code begins with ``">>> "``\n\nContinuation lines begin with ``"... "``\n\n.. note::\n\n    The length of these strings is 4 including the whitespace at the end\n..\n\nExpected output can be quoted or unquoted\n\n.. code-block:: RST\n\n    .. code-block:: python\n\n        >>> n = [\n        ...     "zero",\n        ...     "one",\n        ...     "two",\n        ... ]\n        >>> for c, i in enumerate(n):\n        ...     print(c, i)\n        0 zero\n        1 one\n        2 two\n\n\nStyles can be configured in a pyproject.toml file\n\n.. code-block:: toml\n\n    [tool.readmetester]\n    style = "monokai"\n',
    'author': 'jshwi',
    'author_email': 'stephen@jshwisolutions.com',
    'maintainer': 'jshwi',
    'maintainer_email': 'stephen@jshwisolutions.com',
    'url': 'https://pypi.org/project/readmetester/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
