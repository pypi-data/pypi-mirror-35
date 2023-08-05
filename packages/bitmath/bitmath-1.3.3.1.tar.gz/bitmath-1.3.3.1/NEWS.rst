NEWS
####

.. contents::
   :depth: 1
   :local:


.. _bitmath-1.3.3-1:

bitmath-1.3.3-1
***************

`bitmath-1.3.3-1
<https://github.com/tbielawa/bitmath/releases/tag/1.3.3.1>`__ was
published on 2018-08-23.


Project
=======

Version 1.3.3 is a minor update primarily released to synchronize
versions across platforms. Additionally there are small packaging
updates to keep up with changing standards.

Minor bug fixes and documentation tweaks are included as well.

The project now has an official `Code of Conduct
<https://github.com/tbielawa/bitmath/blob/master/CODE_OF_CONDUCT.md>`_,
as well as issue and pull request templates.


What happened to bitmath 1.3.2? It only ever existed as an idea in
source control.


Changes
=======

**Bug Fixes**

`Alexander Kapshuna <https://github.com/kapsh>`_ has submitted
`several fixes
<https://github.com/tbielawa/bitmath/pulls?q=is%3Apr+author%3Akapsh>`_
since the last release. Thanks!

* Packaging requirements fixes
* Python 3 compatibility
* Subclassing and Type checking fixes/improvements

`Marcus Kazmierczak <https://github.com/mkaz>`_ submitted `a fix
<https://github.com/tbielawa/bitmath/pull/75>`_ for some broken
documentation links.

And `Dawid Gosławski <https://github.com/alkuzad>`_ make sure our
`documentation <https://github.com/tbielawa/bitmath/pull/62/files>`_
is accurate.


Thanks to all the bitmath contributors over the years!


.. _bitmath-1.3.1-1:

bitmath-1.3.1-1
***************

`bitmath-1.3.1-1
<https://github.com/tbielawa/bitmath/releases/tag/1.3.1.1>`__ was
published on 2016-07-17.

Changes
=======

**Added Functionality**

* New function: :func:`bitmath.parse_string_unsafe`, a less strict
  version of :func:`bitmath.parse_string`. Accepts inputs using
  *non-standard* prefix units (such as single-letter, or
  mis-capitalized units).

* Inspired by `@darkblaze69 <https://github.com/darkblaze69>`_'s
  request in `#60 "Problems in parse_string"
  <https://github.com/tbielawa/bitmath/issues/60>`_.


Project
=======

**Ubuntu**

* Bitmath is now available for installation via Ubuntu Xenial, Wily,
  Vivid, Trusty, and Precise PPAs.

* Ubuntu builds inspired by `@hkraal <https://github.com/hkraal>`_
  reporting an `installation issue
  <https://github.com/tbielawa/bitmath/issues/57>`_ on Ubuntu systems.


**Documentation**

* `Cleaned up a lot <https://github.com/tbielawa/bitmath/issues/59>`_
  of broken or re-directing links using output from the Sphinx ``make
  linkcheck`` command.


.. _bitmath-1.3.0-1:

bitmath-1.3.0-1
***************

`bitmath-1.3.0-1
<https://github.com/tbielawa/bitmath/releases/tag/1.3.0.1>`__ was
published on 2016-01-08.

Changes
=======

**Bug Fixes**

* Closed `GitHub Issue #55
  <https://github.com/tbielawa/bitmath/issues/55>`_ "best_prefix for
  negative values". Now :func:`bitmath.best_prefix` returns correct
  prefix units for negative values. Thanks `mbdm
  <https://github.com/mbdm>`_!


.. _bitmath-1.2.4-1:

bitmath-1.2.4-1
***************

`bitmath-1.2.4-1
<https://github.com/tbielawa/bitmath/releases/tag/1.2.4-1>`__ was
published on 2015-11-30.

Changes
=======

**Added Functionality**

* New bitmath module function: :func:`bitmath.query_device_capacity`. Create
  :class:`bitmath.Byte` instances representing the capacity of a block
  device. Support is presently limited to Linux and Mac.

* The :func:`bitmath.parse_string` function now can parse 'octet'
  based units. Enhancement requested in `#53 parse french unit names
  <https://github.com/tbielawa/bitmath/issues/53>`_ by `walidsa3d
  <https://github.com/walidsa3d>`_.

**Bug Fixes**

* `#49 <https://github.com/tbielawa/bitmath/pull/49>`_ - Fix handling
  unicode input in the `bitmath.parse_string
  <https://bitmath.readthedocs.io/en/latest/module.html#bitmath-parse-string>`__
  function. Thanks `drewbrew <https://github.com/drewbrew>`_!

* `#50 <https://github.com/tbielawa/bitmath/pull/50>`_ - Update the
  ``setup.py`` script to be python3.x compat. Thanks `ssut
  <https://github.com/ssut>`_!


Documentation
=============

* The project documentation is now installed along with the bitmath
  library in RPM packages.


Project
=======

**Fedora/EPEL**

Look for separate python3.x and python2.x packages coming soon to
`Fedora <https://getfedora.org/>`_ and `EPEL
<https://fedoraproject.org/wiki/EPEL>`_. This is happening because of
the `initiative
<https://fedoraproject.org/wiki/FAD_Python_3_Porting_2015>`_ to update
the base Python implementation on Fedora to Python 3.x

* `BZ1282560 <https://bugzilla.redhat.com/show_bug.cgi?id=1282560>`_



.. _bitmath-1.2.3-1:

bitmath-1.2.3-1
***************

`bitmath-1.2.3-1
<https://github.com/tbielawa/bitmath/releases/tag/1.2.3-1>`__ was
published on 2015-01-03.

Changes
=======

**Added Functionality**

* New utility: ``progressbar`` integration:
  `bitmath.integrations.BitmathFileTransferSpeed
  <http://bitmath.readthedocs.io/en/latest/module.html#progressbar>`_.
  A more functional file transfer speed widget.


Documentation
=============

* The command-line ``bitmath`` tool now has `online documentation
  <http://bitmath.readthedocs.io/en/latest/commandline.html>`_
* A full demo of the ``argparse`` and ``progressbar`` integrations has
  been written. Additionally, it includes a comprehensive
  demonstration of the full capabilities of the bitmath library. View
  it in the *Real Life Demos* `Creating Download Progress Bars
  <http://bitmath.readthedocs.io/en/latest/real_life_examples.html#real-life-examples-download-progress-bars>`_
  example.


Project
=======

**Tests**

* Travis-CI had some issues with installing dependencies for the 3.x
  build unittests. These were fixed and the build status has returned
  back to normal.


.. _bitmath-1.2.0-1:

bitmath-1.2.0-1
***************

`bitmath-1.2.0-1
<https://github.com/tbielawa/bitmath/releases/tag/1.2.0-1>`__ was
published on 2014-12-29.

Changes
=======

**Added Functionality**

* New utility: ``argparse`` integration: `bitmath.BitmathType
  <https://bitmath.readthedocs.io/en/latest/module.html#argparse>`_.
  Allows you to specify arguments as bitmath types.

Documentation
=============

* The command-line ``bitmath`` tool now has a `proper manpage
  <https://github.com/tbielawa/bitmath/blob/master/bitmath.1.asciidoc.in>`_

Project
=======

**Tests**

* The command-line ``bitmath`` tool is now properly unittested. Code
  coverage back to ~100%.


.. _bitmath-1.1.0-0:

bitmath-1.1.0-1
***************

`bitmath-1.1.0-1
<https://github.com/tbielawa/bitmath/releases/tag/1.1.0-1>`_ was
published on 2014-12-20.

* `GitHub Milestone Tracker for 1.1.0 <https://github.com/tbielawa/bitmath/milestones/1.1.0>`_

Changes
=======

**Added Functionality**

* New ``bitmath`` `command-line tool
  <https://github.com/tbielawa/bitmath/issues/35>`_ added. Provides
  CLI access to basic unit conversion functions
* New utility function `bitmath.parse_string
  <http://bitmath.readthedocs.io/en/latest//module.html#bitmath-parse-string>`_
  for parsing a human-readable string into a bitmath object. `Patch
  submitted <https://github.com/tbielawa/bitmath/pull/42>`_ by new
  contributor `tonycpsu <https://github.com/tonycpsu>`_.

.. _bitmath-1.0.8-1:

bitmath-1.0.5-1 through 1.0.8-1
*******************************

`bitmath-1.0.8-1
<https://github.com/tbielawa/bitmath/releases/tag/1.0.8-1>`__ was
published on 2014-08-14.

* `GitHub Milestone Tracker for 1.0.8 <https://github.com/tbielawa/bitmath/issues?q=milestone%3A1.0.8>`_

Major Updates
=============

* bitmath has a proper documentation website up now on Read the Docs,
  check it out: `bitmath.readthedocs.io
  <http://bitmath.readthedocs.io/en/latest/>`_
* bitmath is now Python 3.x compatible
* bitmath is now included in the `Extra Packages for Enterprise Linux
  <https://fedoraproject.org/wiki/EPEL>`_ EPEL6 and EPEL7 repositories
  (`pkg info
  <https://admin.fedoraproject.org/pkgdb/package/rpms/python-bitmath/>`_)
* merged 6 `pull requests
  <https://github.com/tbielawa/bitmath/pulls?q=is%3Apr+closed%3A%3C2014-08-28>`_
  from 3 `contributors
  <https://github.com/tbielawa/bitmath/graphs/contributors>`_

Bug Fixes
=========

* fixed some math implementation bugs

  * `commutative multiplication <https://github.com/tbielawa/bitmath/issues/18>`_
  * `true division <https://github.com/tbielawa/bitmath/issues/2>`_

Changes
=======

**Added Functionality**

* `best-prefix
  <http://bitmath.readthedocs.io/en/latest/instances.html#best-prefix>`_
  guessing: automatic best human-readable unit selection
* support for `bitwise operations
  <http://bitmath.readthedocs.io/en/latest/simple_examples.html#bitwise-operations>`_
* `formatting customization
  <http://bitmath.readthedocs.io/en/latest/instances.html#format>`_
  methods (including plural/singular selection)
* exposed many more `instance attributes
  <http://bitmath.readthedocs.io/en/latest/instances.html#instances-attributes>`_
  (all instance attributes are usable in custom formatting)
* a `context manager
  <http://bitmath.readthedocs.io/en/latest/module.html#bitmath-format>`_
  for applying formatting to an entire block of code
* utility functions for sizing `files
  <http://bitmath.readthedocs.io/en/latest/module.html#bitmath-getsize>`_
  and `directories
  <http://bitmath.readthedocs.io/en/latest/module.html#bitmath-listdir>`_
* add `instance properties
  <http://bitmath.readthedocs.io/en/latest/instances.html#instance-properties>`_
  equivalent to ``instance.to_THING()`` methods

Project
=======

**Tests**

* Test suite is now implemented using `Python virtualenv's
  <https://github.com/tbielawa/bitmath/blob/master/Makefile#L177>`_
  for consistency across across platforms
* Test suite now contains 150 unit tests. This is **110** more tests
  than the previous major release (`1.0.4-1 <bitmath-1.0.4-1>`__)
* Test suite now runs on EPEL6 and EPEL7
* `Code coverage
  <https://coveralls.io/github/tbielawa/bitmath>`_ is stable
  around 95-100%


.. _bitmath-1.0.4-1:

bitmath-1.0.4-1
***************

This is the first release of **bitmath**. `bitmath-1.0.4-1
<https://github.com/tbielawa/bitmath/releases/tag/1.0.4-1>`__ was
published on 2014-03-20.

Project
=======

Available via:

* `PyPi <https://pypi.python.org/pypi/bitmath/>`_
* Fedora 19
* Fedora 20

bitmath had been under development for 12 days when the 1.0.4-1
release was made available.

Debut Functionality
===================

* Converting between **SI** and **NIST** prefix units (``GiB`` to ``kB``)
* Converting between units of the same type (SI to SI, or NIST to NIST)
* Basic arithmetic operations (subtracting 42KiB from 50GiB)
* Rich comparison operations (``1024 Bytes == 1KiB``)
* Sorting
* Useful *console* and *print* representations
