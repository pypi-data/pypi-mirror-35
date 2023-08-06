SCGI implementation for Trio
============================

This library implements the SCGI protocol (https://www.python.ca/scgi/protocol.txt).
It bases on Trio (https://trio.readthedocs.io/).

SCGI is a very simple and lowlevel way to interface with HTTP servers to implement web application servers.

In a typical setup, multiple web servers accept HTTP requests from clients and proxy those requests through
SCGI to multiple SCGI application servers.

See ``example/echo`` for a demo SCGI server.


