.. xotl.ql documentation master file, created by
   sphinx-quickstart on Fri Jun 29 12:53:45 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

A pythonic query language
=========================

This package provides *tools* to implement query languages in python.  The
query language is based on Python's generator expression.  A query in this
language looks like this::

    >>> from xotl.ql.core import get_query_object, this

    >>> query = get_query_object(
    ...    child
    ...    for parent in this
    ...    if parent.children and parent.age > 32
    ...    for child in parent.children
    ...    if child.age < 6
    ... )

The result of the :class:`~xotl.ql.core.get_query_object` callable is a
:term:`query object` that "describes" at the syntactical level the
:term:`query expression` above.



What's new in |release|?
------------------------

.. include:: history/changes-0.6.0.rst


Core Contents:
--------------

.. toctree::
   :glob:
   :maxdepth: 1

   overview
   translation
   api/*
   terms
   HISTORY
   credits
   license
   known-issues

Additional documents:
---------------------

.. toctree::
   :maxdepth: 1

   ponyorm
   thoughts
   _revenge/index
   monads
   scratch
   references
   changes/index

What does xotl mean?
--------------------

The word "xotl" is a Nahuatl word that means foundation, base.  The `xotl`
package comprises the foundation for building reliable systems, frameworks,
and libraries.  It also provides an object model that allows to build complex
systems.

It is expected that `xotl` will use `xotl.ql` to:

- Express predicates defining object relationships
- Query the object store (of course!)
- Update the object store.
