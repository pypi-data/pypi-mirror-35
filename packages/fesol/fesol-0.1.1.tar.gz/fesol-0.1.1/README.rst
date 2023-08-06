Simple Finite Element Solvers
=============================

.. image:: https://img.shields.io/pypi/v/fesol.svg?branch=master
    :target: https://pypi.org/project/fesol/

.. _FEniCS: https://fenicsproject.org/

This repository contains a simple heat equation solver that is built on top of
`FEniCS`_ framework.

Notice that this solver has been tested on `FEniCS`_ 2017.1 and 2018.1. Direct
installation from Ubuntu PPA should work.

Installation and Requirements
-----------------------------

First install FEniCS, the simplest way is to use a Ubuntu environment (you
can use Ubuntu through Docker).

.. code:: console

    $ sudo add-apt-repository ppa:fenics-packages/fenics
    $ sudo apt-get update && sudo apt-get install fenics

If this is not feasible, please refer to `FEniCS`_ website for other options.

Once you have `FEniCS`_ installed, ``fesol`` can be installed through ``pip``.

.. code:: console

    $ pip3 install fesol --user

Or you can directly install from the repository.

.. code:: console

    $ git clone https://QiaoC@bitbucket.org/QiaoC/fesol.git
    $ python3 setup.py install --user

# License

MIT License, Copyright (c) 2018 Qiao Chen
