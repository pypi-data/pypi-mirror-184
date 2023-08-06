# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neuropull', 'neuropull.graph', 'neuropull.load', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'beartype>=0.11.0,<0.12.0',
 'mkdocs-material-extensions>=1.1.1,<2.0.0',
 'networkx>=2.8.6,<3.0.0',
 'numpy>=1.23.3,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'scipy>=1.9.2,<2.0.0']

extras_require = \
{':extra == "doc"': ['mkdocs>=1.4.2,<2.0.0',
                     'mkdocs-include-markdown-plugin>=4.0.0,<5.0.0',
                     'mkdocs-material>=8.5.11,<9.0.0',
                     'mkdocstrings[python]>=0.19.0,<0.20.0',
                     'mkdocs-autorefs>=0.4.1,<0.5.0'],
 'data': ['python-catmaid>=2.1.1,<3.0.0',
          'ipykernel>=6.15.3,<7.0.0',
          'graspologic>=2.0.0,<3.0.0'],
 'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'test': ['black>=22.3.0,<23.0.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.900,<0.901',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

setup_kwargs = {
    'name': 'neuropull',
    'version': '0.1.1',
    'description': 'A lightweight tool for pulling connectome networks and metadata.',
    'long_description': '# neuropull\n\n\n[![pypi](https://img.shields.io/pypi/v/neuropull.svg)](https://pypi.org/project/neuropull/)\n[![python](https://img.shields.io/pypi/pyversions/neuropull.svg)](https://pypi.org/project/neuropull/)\n[![Build Status](https://github.com/neurodata/neuropull/actions/workflows/dev.yml/badge.svg)](https://github.com/neurodata/neuropull/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/neurodata/neuropull/branch/main/graphs/badge.svg)](https://codecov.io/github/neurodata/neuropull)\n\n\n\nA lightweight tool for pulling connectome networks and metadata\n\n\n* Documentation: <https://neurodata.github.io/neuropull>\n* GitHub: <https://github.com/neurodata/neuropull>\n* PyPI: <https://pypi.org/project/neuropull/>\n* Free software: MIT\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n',
    'author': 'Benjamin D. Pedigo',
    'author_email': 'bpedigo@jhu.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/neurodata/neuropull',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.0,<3.10',
}


setup(**setup_kwargs)
