EQI Data Loader and Exporter
============================

Features:
---------

-  Download DataFrame from data vendors via S3
-  Manage and store analysis views locally or remotely on S3
-  Download DataFrame from RESLIVE DB

Key Concept:
------------

-  Bundle: a group of data files from a specific vendor, e.g. linkup
-  DataFile: a file which contains data, e.g. Company\_Daily within
   linkup bundle
-  View: a DataFrame serialized into a parquet file, can be stored
   locally, or remotely on S3
-  DBView: a DataFrame which contains the result of a SQL query

How to install:
===============

-  Install this package using pip

   .. code:: bash

       pip install eqi-utilities

Getting started:
================

-  Create EQI home folder

   -  Create a folder named '.eqi' in your home folder, on Windows,
      create a folder named as '.eqi.'

-  Go to examples/config.ini, set all the fields, and copy the
   config.ini file to EQI home folder created in the above step
-  Go to examples/load\_export\_example.html, see how to use the
   utilities

Known Issues:
=============

-  Failed at downloading large parquet datafile
    Please install fastparquet using conda:
    .. code:: bash

        conda install -c conda-forge fastparquet


Please feel free to create an issue in case of any problems.
