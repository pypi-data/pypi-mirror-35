# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['extractini']

package_data = \
{'': ['*']}

install_requires = \
['click>=6.7,<7.0']

entry_points = \
{'console_scripts': ['extractini = extractini.console:extract_from_inifile']}

setup_kwargs = {
    'name': 'extractini',
    'version': '1.0.0',
    'description': 'extractini is a command-line application to extract a single option from an INI file',
    'long_description': None,
    'author': 'Matt Magin',
    'author_email': 'matt.magin@cmv.com.au',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
