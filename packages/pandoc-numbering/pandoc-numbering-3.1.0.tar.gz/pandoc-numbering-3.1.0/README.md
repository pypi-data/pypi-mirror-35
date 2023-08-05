# pandoc-numbering
[![Build Status](https://img.shields.io/travis/chdemko/pandoc-numbering/3.1.0.svg)](https://travis-ci.org/chdemko/pandoc-numbering/branches)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-numbering/3.1.0.svg)](https://coveralls.io/github/chdemko/pandoc-numbering?branch=3.1.0)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-numbering.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-numbering/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-numbering.svg)](https://pypi.org/project/pandoc-numbering/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-numbering/3.1.0.svg)](https://pypi.org/project/pandoc-numbering/3.1.0/)
[![License](https://img.shields.io/pypi/l/pandoc-numbering/3.1.0.svg)](https://raw.githubusercontent.com/chdemko/pandoc-numbering/3.1.0/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-numbering.svg)](https://pypi.org/project/pandoc-numbering/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-numbering.svg)](https://pypi.org/project/pandoc-numbering/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-numbering.svg)](https://pypi.org/project/pandoc-numbering/)

*pandoc-numbering* is a [pandoc] filter for numbering all kinds of things.

[pandoc]: http://pandoc.org/

Documentation
-------------

See the [wiki pages](https://github.com/chdemko/pandoc-numbering/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    --filter pandoc-numbering

Installation
------------

*pandoc-numbering* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]. Either python 2.7 or 3.x will do.

Install *pandoc-numbering* as root using the bash command

    pip install pandoc-numbering

To upgrade to the most recent release, use

    pip install --upgrade pandoc-numbering

To upgrade to the current code, use

    pip install --upgrade --force --no-cache git+https://github.com/chdemko/pandoc-numbering

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python-pip

[python]: https://www.python.org/
[on Windows]: https://www.python.org/downloads/windows/
[PyPI]: https://pypi.python.org/pypi


Getting Help
------------

If you have any difficulties with *pandoc-numbering*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-numbering/issues
