docubox
=======

.. image:: https://readthedocs.org/projects/docubox/badge/?version=latest
    :target: https://docubox.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. _ReadTheDocs.org: https://docubox.readthedocs.io/en/latest/

DocuBox is a swiss army knife for document solution.
It is a single binary that has multiple document solution commands internally.
The project name is borrowed from a famous BusyBox.

BusyBox combines many tiny unix commands into single binary,
and installed with many names by symbolic links. It run for its name,

DocuBox combines several python document solution commands into single binary,
When rename or link the binary as ``sphinx-build``, it behave ``sphinx-build`` command.
When rename or link the binary sa ``mkdocs``, it behave ``mkdocs`` command.
It runs document solution commands on Windows, Linux and OS X with a single-file standalone binary.


DocuBox is also a docubox binary generator.
It can generate ducubox binary for the platform built on.
We build it with PyInstaller , a user can run commands without installing a Python interpreter or any dependencies.

* Document:  `ReadTheDocs.org`_
* Download binary: https://codeberg.org/miurahr/docubox/releases

License
-------

Sphinx-standalone is licensed under the 2-clauses BSD license.
See ``LICENSE`` file for details.

