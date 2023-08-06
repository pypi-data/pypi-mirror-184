# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tests', 'tripser']

package_data = \
{'': ['*'], 'tests': ['test_data/*']}

install_requires = \
['click==8.0.1']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'test': ['black>=21.5b2,<22.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

entry_points = \
{'console_scripts': ['pytripalserializer = tripser.cli:cli']}

setup_kwargs = {
    'name': 'pytripalserializer',
    'version': '0.0.2',
    'description': "Serialize Tripal's JSON-LD API into RDF..",
    'long_description': "# PyTripalSerializer\n[![Documentation Status](https://readthedocs.org/projects/pytripalserializer/badge/?version=latest)](https://pytripalserializer.readthedocs.io/en/latest/?badge=latest)\n\nSerialize Tripal's JSON-LD API into RDF format\n",
    'author': 'Carsten Fortmann-Grote',
    'author_email': 'carsten.fortmann-grote@evolbio.mpg.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/CFGrote/PyTripalSerializer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0',
}


setup(**setup_kwargs)
