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
    'version': '1.0.1',
    'description': 'extractini is a command-line application to extract a single option from an INI file',
    'long_description': 'extractini\n==========\n\n``extractini`` is a command-line application to extract a single option from an INI file with a structure \nas described in the `python documentation`__.\n\n.. _INIDocs: https://docs.python.org/3/library/configparser.html#supported-ini-file-structure\n\n__ INIDocs_\n\nInstall\n-------\n\nInstall with ``pip``.\n\n::\n\n    pip install extractini\n\nUsage\n-----\n\nRun ``extractini`` with positional arguments for the path to the ini-file, the name of the ini file section, and the name of the ini file option.\n\n::\n\n    extractini [OPTIONS] CONFIGFILE SECTION OPTION\n\nFor example, extracting ``type`` from ``chiliconfig.ini`` prints ``capsicum``:\n\n::\n\n    $ cat chiliconfig.ini\n    [habanero]\n    type=capsicum\n    heat=very hot\n    scovilles=100,000 - 350,000\n\n    $ extractini chiliconfig.ini habanero type\n    capsicum\n\nTesting\n-------\n\n``extractini`` comes with a few unit tests which can be run with ``pytest``.\n\nContributing\n------------\n\nIf you find something wrong feel free to submit a PR or raise an Issue on Github.\n\nLicense\n-------\n\nCopyright 2018 Matt Magin\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n',
    'author': 'Matt Magin',
    'author_email': 'matt.magin@cmv.com.au',
    'url': 'https://github.com/AzMoo/extractini/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
