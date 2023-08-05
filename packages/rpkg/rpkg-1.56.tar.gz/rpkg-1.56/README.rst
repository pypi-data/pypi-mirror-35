Introduction
============

This is the rpkg project, which mostly is a python library for dealing with
rpm packaging in a git source control.  pyrpkg is the base library that sites
can subclass to create useful tools.

rpkg works with Python 2.6, 2.7, 3.5, 3.6 and 3.7.

License
=======

Unless otherwise specified, all files are licensed under GPLv2+.

Installation
============

Install from distribution packages
----------------------------------

rpkg is available in Fedora and EPEL repositories. It can be installed with
package manager command. There are Python 2 and 3 package for Fedora and only
Python 2 package in EPEL.

Install in a Fedora system::

    sudo dnf install python2-rpkg

If Python 3 package is needed, install ``python3-rpkg``.

Install in EL6 or EL7::

    sudo yum install python2-rpkg

Install in a Python virtual environment
---------------------------------------

Both Python 2 and 3 packages are published in PyPI. Install rpkg in a Python 3
virtual environment in these steps::

    python3 -m venv env
    source env/bin/activate
    pip install rpkg rpm-py-installer

You are free to create a virtual environment with option ``--system-site-packages``.

Please note that, rpkg depends on some other utilities to build packages. These
packages are required to be installed as well.

* ``mock``: for local mockbuild.
* ``rpm-build``:  for local RPM build, which provides the command line ``rpm``.
* ``rpmlint``: check SPEC.
* ``copr-cli``: for building package in `Fedora Copr`_.
* ``module-build-service``: for building modules.

.. _`Fedora Copr`: https://copr.fedorainfracloud.org/

Contribution
============

You are welcome to write patches to fix or improve rpkg. All code should work
with Python 2.6, 2.7, and 3. Before you create a PR to propose your changes,
make sure

Sign-off commit
---------------

Make sure to sign-off your commits by ``git commit -s``. This serves as a
confirmation that you have the right to submit your changes. See `Developer
Certificate of Origin`_ for details.

.. _Developer Certificate of Origin: https://developercertificate.org/

Run Tests
---------

Before make a pull request, ensure local changes pass all test cases. There
are two choices to run tests.

* Run tests in parallel with ``detox``. Newer version of ``detox`` does not
  support ``py26``. You can run rest of test environments::

    detox -e py27,py36,py37,flake8

* Run tests inside a Python environment with ``tox``::

    python3 -m venv env
    source env/bin/activate
    pip install tox
    tox

More Information
================

See https://pagure.io/rpkg for more information, bug tracking, etc.
