# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oracle_of_ammon',
 'oracle_of_ammon.api',
 'oracle_of_ammon.cli',
 'oracle_of_ammon.common',
 'oracle_of_ammon.tests']

package_data = \
{'': ['*'], 'oracle_of_ammon': ['data/*']}

install_requires = \
['aiofiles>=22.1.0,<23.0.0',
 'farm-haystack>=1.12.2,<2.0.0',
 'fastapi>=0.88.0,<0.89.0',
 'pandas>=1.5.2,<2.0.0',
 'pynvml>=11.4.1,<12.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.7.0,<0.8.0',
 'uvicorn>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['oracle-of-ammon = oracle_of_ammon.cli.main:app']}

setup_kwargs = {
    'name': 'oracle-of-ammon',
    'version': '0.1.2',
    'description': 'CLI tool for creating Search APIs.',
    'long_description': '# Oracle of Ammon\n\nA simple CLI tool for creating Search APIs.\n',
    'author': 'Kyle McLester',
    'author_email': 'kyle.mclester@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kmcleste/oracle-of-ammon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
