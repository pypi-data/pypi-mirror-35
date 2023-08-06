extractini
==========

``extractini`` is a command-line application to extract a single option from an INI file with a structure 
as described in the `python documentation`__.

.. _INIDocs: https://docs.python.org/3/library/configparser.html#supported-ini-file-structure

__ INIDocs_

Install
-------

Install with ``pip``.

::

    pip install extractini

Usage
-----

Run ``extractini`` with positional arguments for the path to the ini-file, the name of the ini file section, and the name of the ini file option.

::

    extractini [OPTIONS] CONFIGFILE SECTION OPTION

For example, extracting ``type`` from ``chiliconfig.ini`` prints ``capsicum``:

::

    $ cat chiliconfig.ini
    [habanero]
    type=capsicum
    heat=very hot
    scovilles=100,000 - 350,000

    $ extractini chiliconfig.ini habanero type
    capsicum

Testing
-------

``extractini`` comes with a few unit tests which can be run with ``pytest``.

Contributing
------------

If you find something wrong feel free to submit a PR or raise an Issue on Github.

License
-------

Copyright 2018 Matt Magin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
