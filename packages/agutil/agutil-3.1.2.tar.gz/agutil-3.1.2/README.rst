agutil
======

-  Master build status: |Master Build Status| |Live Package Version|
-  Development build status: |Dev Build Status| |Dev Coverage Status|

A collection of python utilities

**Version:** 3.1.2

Tools:
      

-  search\_range (A utility for manipulating numerical ranges)
-  status\_bar (A simple progress bar indicator)
-  Logger (A class for fast, simple, logging)
-  Several standalone utility methods (See the `agutil module
   page <https://github.com/agraubert/agutil/wiki/agutil-%28main-module%29>`__
   on the wiki)

The **bio** package:

-  [STRIKEOUT:maf2bed (A command line utility for parsing a .maf file
   and converting coordinates from 1-based (maf standard) to 0-based
   (bed standard))]

**Deprecated: Will be removed in a future release**

The **io** package:

-  Socket (A low-level network IO class built on top of the standard
   socket class)
-  SocketServer (A low-level listen server to accept connections and
   return Socket classes)
-  QueuedSocket (A low-level network IO class built to manage input
   across multiple channels)

The **parallel** package:

-  parallelize (A decorator to easily convert a regular function into a
   parallelized version)
-  parallelize2 (A similar parallelization decorator with a slightly
   different flavor)
-  IterDispatcher (Logical backend for dispatching calls with
   parallelize)
-  DemandDispatcher (Logical backend for dispatching calls with
   parallelize2)
-  ThreadWorker (Task management backend for dispatching parallel calls
   to threads)
-  ProcessWorker (Task management backend for dispatching parallel calls
   to processes)

The **security** package:

-  SecureSocket (A mid-level network IO class built to manage encrypted
   network communications)
-  SecureConnection (A high-level, multithreaded class for sending and
   receiving encrypted files and messages)
-  SecureServer (A low-level listen server to accept connections and
   return SecureConnection instances)
-  encryptFile and decryptFile (Simple methods for encrypting and
   decrypting local files)
-  agutil-secure (A command line utility for encrypting and decrypting
   files)

Documentation:
--------------

Detailed documentation of these packages can be found on the `agutil
Github wiki page <https://github.com/agraubert/agutil/wiki>`__

.. |Master Build Status| image:: https://travis-ci.org/agraubert/agutil.svg?branch=master
   :target: https://travis-ci.org/agraubert/agutil
.. |Live Package Version| image:: https://img.shields.io/pypi/v/agutil.svg
   :target: https://pypi.python.org/pypi/agutil
.. |Dev Build Status| image:: https://travis-ci.org/agraubert/agutil.svg?branch=dev
   :target: https://travis-ci.org/agraubert/agutil
.. |Dev Coverage Status| image:: https://coveralls.io/repos/github/agraubert/agutil/badge.svg?branch=dev
   :target: https://coveralls.io/github/agraubert/agutil?branch=dev
