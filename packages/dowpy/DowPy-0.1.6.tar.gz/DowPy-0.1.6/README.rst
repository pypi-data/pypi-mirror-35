DowPy: An efficient way to download files via HTTP
==================================================

.. image:: logo.jpg
    :width: 257px
    :align: center
    :height: 84px
    :alt: logo

|PyPI version| |License: MIT|

.. |PyPI version| image:: https://badge.fury.io/py/dowpy.svg
   :target: https://badge.fury.io/py/dowpy
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT



Features
--------
* Ability to download any file type
* Multi-threading to run parallel downloads, if supported
* Resumable downloads on connection loss
* Cross-platform support
* Timed bench marks of each individual chunk/overall file
* File verification, via hash check


Installation
------------

To install DowPy, Use pip:

.. code-block::

    $ pip install dowpy


Usage
-----

.. code-block:: python

   url = "https://gph.to/2BTy5xU"

   # To create a single thread download
   dow1 = SingleDow(url)

   # To create a multi threaded download with 3 parallel downloads
   dow2 = MultiDow(url, 3)

   # To start the download
   dow1.start()

Documentation
-------------
The following properties can be set BEFORE the download has started:

+----------------+--------+---------------------------------------------------------------------------------+
| prop           | type   | Desc                                                                            |
+================+========+=================================================================================+
| .url           | string | The direct url to the file to request                                           |
+----------------+--------+---------------------------------------------------------------------------------+
| .chunks        | int    | The # of parallel threads to download the file with (MultiDow only)             |
+----------------+--------+---------------------------------------------------------------------------------+
| .writeLocation | string | File location to download the file                                              |
+----------------+--------+---------------------------------------------------------------------------------+
| .fileName      | string | Name of the downloaded file                                                     |
+----------------+--------+---------------------------------------------------------------------------------+
| .hash          | string | Known hash to test the file with                                                |
+----------------+--------+---------------------------------------------------------------------------------+



The following properties return information about the download:

+----------------+--------+---------------------------------------------------------------------------------+
| prop           | type   | Desc                                                                            |
+================+========+=================================================================================+
| .status        | string | Returns the current status of the download (initialized, downloading, complete) |
+----------------+--------+---------------------------------------------------------------------------------+
| .sizeInBytes   | string | Returns the size of the file in bytes                                           |
+----------------+--------+---------------------------------------------------------------------------------+
| .startTime     | string | Start time of the download                                                      |
+----------------+--------+---------------------------------------------------------------------------------+
| .endTime       | string | End time of the download                                                        |
+----------------+--------+---------------------------------------------------------------------------------+
| .elapsedTime   | String | Total time of download                                                          |
+----------------+--------+---------------------------------------------------------------------------------+