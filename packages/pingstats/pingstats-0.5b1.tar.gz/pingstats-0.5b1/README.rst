Pingstats, a simple CLI based ping visualization script
=======================================================

This script provides a very simple CLI based ping visualization script by utilizing `hipster plot`_.

This project is a much simplified version of PingStats_, a project of mine that went from being useful (i.e, the functionality of this script) to an over complicated mess of spaghetti code. That software provides GUI based plotting, as well as CSV based logging of ping data over time.

INSTALLATION
============

Installation has been made easy on any Unix based system that implements ``pip3``.
::

  $ pip3 install pingstats

.. note:: For versions previous to V0.4.3, manual install must be used. All versions aside from V0.1 can be installed by cloning the repository and recreating the install script manually.

USAGE
=====

This software was implemented with simplicity in mind, and only provides one point of access:
::
   
   $ pingstats google.ca

EXAMPLES OF SOFTWARE IN USE
===========================

.. image:: https://i.imgur.com/pU02xj2.png

In this image, we can see a ping readout from google.ca. The Y axis is mapped to packet return time, and the X axis is mapped to the ICMP sequence number.

This display automatically scales to whatever window you have open, adding more lines and columns as necessary.


.. _`hipster plot`: https://github.com/imh/hipsterplot
.. _PingStats: https://github.com/eclectickmedia/pingstats
