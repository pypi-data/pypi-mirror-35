Introduction
============

The is a simplification and redesign of the orderedbunch package from tinytools.
The package ontains an OrderedBunch object class with associated
bunchify/unbunchify methods, similar to other bunch implementations but
built off an OrderedDict with ipython table-complete overloaded to the
data memebers.  It removes the ``ordered_dictionarify`` function that is in
tinytools and and leaves the development of the nested dictionaries to
external code.  The motivation is that it is quite complicated to infer what
the user is wanting - and therefore error prone.

IPython has also recently changed its handling of the ``__dir__`` method and it
is unclear under which cases it is respected for tab completion or not.  It
seems, though, that for ipython 6, it is possible to remove mothods from
the tab completion through the ``IPCompleter.*`` configuration options.

Installing
==========

.. code:: python 

    pip install orderedbunch

Import
=======

.. code:: python 

    import orderedbunch

Quick Start
===========
.. code:: python

    from orderedbunch import OrderedBunch

    ## OrderedBunch
    from collections import OrderedDict

    # Create an OrderedBunch from and return it to an OrderedDict
    od = OrderedDict({'a':1,'b':2,'c':{'aa':1.23,'bb':'string'}})
    ob = orderedbunch.ordered_bunchify(od)
    ob.a          # Explore the OrderdBunch with tab complete
    ob['a']       # Equivalent to above
    ob.c.bb       # orderd_bunchify is recursive on nested Dict objects
    ob['c']['bb'] # Equivalent to above
    od2 = tt.bunch.ordered_unbunchify(ob)
