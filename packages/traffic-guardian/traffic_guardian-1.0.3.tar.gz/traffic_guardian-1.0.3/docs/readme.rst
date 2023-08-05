.. _readme:

================
traffic_guardian
================


    Proxy server for intercepting HTTP traffic with python library to dynamically manage the proxy rules

Solution consists of two main components that are implemented inside `traffic_guardian_core` package:
 1. Proxy server based on `twisted` networking engine running by default on port 8080
 2. REST API to govern the proxy rules used for intercepting and mocking responses by default on port 9090

Based on REST API for governing the proxy rules python library has been developed inside `traffic_guardian` package.

Usage
=====
To install `traffic_guardian` use following command (assuming that you have `pip` installed):

.. code-block:: bash

    $ pip install traffic_guardian

To run the proxy server on default port (8080 for proxy server, 9090 for REST API to govern the proxy rules) use the following command:

.. code-block:: bash

    $ traffic_guardian

To check more help with the CLI tool use the following command

.. code-block:: bash

    $ traffic_guardian -h

Docs
====
Documentation to project is hosted on readthedocs.org under following link https://traffic-guardian.readthedocs.io/en/latest/



.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
