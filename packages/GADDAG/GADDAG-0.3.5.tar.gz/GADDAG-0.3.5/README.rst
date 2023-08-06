======
GADDAG
======

GADDAG is a Python wrapper around cGADDAG_.

A GADDAG data structure provides rapid word lookups for prefixes, suffixes and
substrings, making it ideal for use in applications such as move generation in
word games such as Scrabble_.

Basic usage::

   >>> import gaddag
   >>> words = ["foo", "bar", "foobar", "baz"]
   >>> gdg = gaddag.GADDAG(words)
   >>> "foo" in gdg
   True
   >>> "bor" in gdg
   False
   >>> gdg.contains("ba")
   ['bar', 'foobar', 'baz']

GADDAG currently only supports the ASCII alphabet.

Installation
------------

From PyPI_:

``pip install gaddag``

Documentation
-------------

Documentaion is available at http://gaddag.readthedocs.io.

License
-------

Licensed under the MIT License, see LICENSE_.

.. _cGADDAG: https://github.com/jorbas/cGADDAG
.. _Scrabble: https://en.wikipedia.org/wiki/Scrabble
.. _PyPI: https://pypi.python.org/pypi/GADDAG
.. _LICENSE: https://github.com/jorbas/GADDAG/blob/master/LICENSE

