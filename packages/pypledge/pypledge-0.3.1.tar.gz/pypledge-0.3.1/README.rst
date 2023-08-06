========
PyPledge
========

.. code-block:: python

   def pledge(promises: Optional[Iterable[str]] = None,
              execpromises: Optional[Iterable[str]] = None) -> None: ...

Throws ``OSError`` if the platform does not support ``pledge(2)`` or
if the pledge fails.

Example
-------

The following will restrict the current process to only the ``stdio`` and ``tty`` promises, and then attempt to violate that restriction:

.. code-block:: python

  import pypledge
  pypledge.pledge(['stdio', 'tty'])
  f = open('foo.txt')

On OpenBSD 5.9, this will terminate with SIGABRT because the ``rpath``
promise was required.

On other platforms, this will throw OSError.
