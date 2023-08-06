`pymcmcstat`
============

|docs| |build| |coverage| |license| |codacy| |zenodo| |pypi| |pyversion|

The `pymcmcstat <https://prmiles.wordpress.ncsu.edu/codes/python-packages/pymcmcstat/>`__ package is a Python program for running Markov Chain Monte Carlo (MCMC) simulations.
Included in this package is the ability to use different Metropolis based sampling techniques:

* Metropolis-Hastings (MH): Primary sampling method.
* Adaptive-Metropolis (AM): Adapts covariance matrix at specified intervals.
* Delayed-Rejection (DR): Delays rejection by sampling from a narrower distribution.  Capable of `n`-stage delayed rejection.
* Delayed Rejection Adaptive Metropolis (DRAM): DR + AM

This package is an adaptation of the MATLAB toolbox `mcmcstat <http://helios.fmi.fi/~lainema/mcmc/>`_.  The user interface is designed to be as similar to the MATLAB version as possible, but this implementation has taken advantage of certain data structure concepts more amenable to Python.  

Note, advanced plotting routines are available in the `mcmcplot <https://prmiles.wordpress.ncsu.edu/codes/python-packages/mcmcplot/>`__ package.  Many plotting features are directly available within `pymcmcstat <https://prmiles.wordpress.ncsu.edu/codes/python-packages/pymcmcstat/>`__, but some user's may find `mcmcplot <https://prmiles.wordpress.ncsu.edu/codes/python-packages/mcmcplot/>`__ useful.

Installation
============

This code can be found on the `Github project page <https://github.com/prmiles/pymcmcstat>`_.  This package is available on the PyPI distribution site and the latest version can be installed via

::

    pip install pymcmcstat
    
The master branch on Github typically matches the latest version on the PyPI distribution site.  To install the master branch directly from Github,

::

    pip install git+https://github.com/prmiles/pymcmcstat.git

You can also clone the repository and run ``python  setup.py install``.

Getting Started
===============

- Tutorial `notebooks <https://nbviewer.jupyter.org/github/prmiles/notebooks/tree/master/pymcmcstat/index.ipynb>`_
- `Documentation <http://pymcmcstat.readthedocs.io/>`_

License
=======

`MIT <https://github.com/prmiles/pymcmcstat/blob/master/LICENSE.txt>`_

Contributors
============

See the `GitHub contributor page <https://github.com/prmiles/pymcmcstat/graphs/contributors>`_

Citing pymcmcstat
=================

Please see the `pymcmcstat homepage <https://prmiles.wordpress.ncsu.edu/codes/python-packages/pymcmcstat/>`__ or follow the DOI badge above to find the appropriate citation information.

Feedback
========

- `Feature Request <https://github.com/prmiles/pymcmcstat/issues/new?template=feature_request.md>`_
- `Bug Report <https://github.com/prmiles/pymcmcstat/issues/new?template=bug_report.md>`_

   
.. |docs| image:: https://readthedocs.org/projects/pymcmcstat/badge/?version=latest
    :target: https://pymcmcstat.readthedocs.io/en/latest/?badge=latest
    
.. |build| image:: https://travis-ci.org/prmiles/pymcmcstat.svg?branch=master
    :target: https://travis-ci.org/prmiles/pymcmcstat
    
.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://github.com/prmiles/pymcmcstat/blob/master/LICENSE.txt

.. |coverage| image:: https://coveralls.io/repos/github/prmiles/pymcmcstat/badge.svg
    :target: https://coveralls.io/github/prmiles/pymcmcstat

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/b1a33340c57a47648f993e124c75e93a    
    :target: https://www.codacy.com/app/prmiles/pymcmcstat?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prmiles/pymcmcstat&amp;utm_campaign=Badge_Grade

.. |zenodo| image:: https://zenodo.org/badge/107596954.svg
    :target: https://zenodo.org/badge/latestdoi/107596954
    
.. |pypi| image:: https://img.shields.io/pypi/v/pymcmcstat.svg
    :target: https://pypi.org/project/pymcmcstat/
    
.. |pyversion| image:: https://img.shields.io/pypi/pyversions/pymcmcstat.svg
    :target: https://pypi.org/project/pymcmcstat/