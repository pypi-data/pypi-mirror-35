Rundeck Resources
=================

Python tool to query resources from different sources and export them into a data structure that ``Rundeck`` can consume.

Installation
------------

::

    pip install rundeck-resources
      
Usage
-----

::

    $ rundeck-resources -h
    usage: rundeck-resources [-h] -c  [-V]

    Generates rundeck resources file from different API sources

    optional arguments:
    -h, --help      show this help message and exit
    -c , --config   Configuration file
    -V, --version   Prints version


The ``rundeck-resources`` requires an INI configuration file.
You can see the example configuration in the `example.ini <https://gitlab.com/elazkani/rundeck-resources/blob/master/config/example.ini>`_.

Importers
---------

``rundeck-resources`` currently offer the following **importers**:

* Chef: ``ChefImporter``


Exporters
---------

``rundeck-resources`` currently offers the following **expoters**:

* YAML: ``YAMLExporter``
