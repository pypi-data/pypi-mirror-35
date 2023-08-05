.. _known-issues:

==============
 Known issues
==============

- Nested conditional expressions like::

    (a if x else y) if (b if z else c) else (d if o else p)

  fail to be recognized.

- Pypy support is not complete.  Expressions like ``(x for x in this if not
  p(x) or z(x) or not h(x))`` fail to be recognized.


- `~xotl.ql.core.this`:data: may be hidden from the `xotl.ql.revenge`:mod:
  machinery by 'enclosing' it inside a function::

    ((i, obj) for i, obj in enumerate(this))

  This is because the generator only 'sees' the result of calling
  ``enumerate(this)`` and cannot reach the ``this`` within.

  Our current solution path is to enclose the entire query inside a
  ``lambda``::

    lambda: ((i, obj) for i, obj in enumerate(this))


  Alternatively we may choose to explicitly make the universe an argument::

    lambda this: ((i, obj) for i, obj in enumerate(this))


  The second approach will make our query testable in pure Python code, and if
  we succeed in translation, it will also work in production.  However, it
  will require annotations of the arguments.
