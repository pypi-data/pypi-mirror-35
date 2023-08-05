cfme_testcases
==============

* import requirements missing in Polarion
* import test cases missing in Polarion
* update existing test cases, link missing requirements
* create new test run in Polarion or update an existing test run with newly imported test cases

All this with single command, using just the Polarion Importers. The legacy webservices API is not used at all.

Usage
-----

Run in the ManageIQ ``integration_tests`` directory in your usual virtual environment.

.. code-block::

    cfme_testcases_upload.py -t {testrun id}

Install
-------

You don't need to install the package, you can use the scripts directly from the cloned repository.

To install the package to your virtualenv, run

.. code-block::

    pip install cfme_testcases
    # or
    pip install -e .

Requirements
------------

You need `dump2polarion <https://github.com/mkoura/dump2polarion>`_:

.. code-block::

    pip install dump2polarion
    # or
    pip install -r requirements.txt
