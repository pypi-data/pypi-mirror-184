Light Progress
==============

This is a progress reporting tool for Python.

.. code:: python

   ProgressBar.iteration(range(42), lambda item: sleep(0.01))

.. code:: python

   # [▉..............................] 1% (1/42)
   # [███████████████▉...............] 50% (21/42)
   # [███████████████████████████████] 100% (42/42)

Installation
------------

.. code:: sh

   pip install light-progress

Examples
--------

Import
~~~~~~

.. code:: python

   from time import sleep
   from light_progress import ProgressBar

Pattern 1
~~~~~~~~~

Call ``start()`` ``forward()`` and ``finish()`` yourself.

.. code:: python

   n = 42
   progress_bar = ProgressBar(n)
   progress_bar.start()

   for item in range(n):
       sleep(0.01)
       progress_bar.forward()

   progress_bar.finish()

Pattern 2
~~~~~~~~~

You can execute a iteration within ``with`` statement. You don’t have to
call ``start()`` and ``finish()`` explicitly.

.. code:: python

   n = 42
   with ProgressBar(n) as progress_bar:
       for item in range(n):
           sleep(0.01)
           progress_bar.forward()

Pattern 3
~~~~~~~~~

Transfer iteration. You don’t have to call any ``ProgressBar`` methods
yourself.

.. code:: python

   ProgressBar.iteration(range(42), lambda item: sleep(0.01))

Pattern 4
~~~~~~~~~

Transfer generation. You don’t have to call any ``ProgressBar`` methods
yourself.

.. code:: python

   for item in ProgressBar.generation(range(42)):
       sleep(0.01)

Colors
------

=========== =====
status      color
=========== =====
In progress Blue
Success     Green
Failure     Red
=========== =====

Customize
~~~~~~~~~

.. code:: python

   from light_progress import Colors, MessageType

.. code:: python

   colors = {
       MessageType.COURSE: Colors.YELLOW,
       MessageType.COMPLETE: Colors.BLUE,
   }
   ProgressBar.iteration(range(100), lambda item: sleep(0.01), colors=colors)

Widgets
-------

``ProgressBar`` can change its display format using ``widget``.

.. code:: python

   from light_progress import widget

.. code:: python

   widgets = [widget.Bar(bar='=', tip='-'),
              widget.Percentage(),
              widget.Num()]

   ProgressBar.iteration(
       range(42), lambda item: sleep(0.01), widgets=widgets)

   # [===============-...............] 50% (21/42)

.. code:: python

   widgets = [widget.Percentage(),
              widget.Num(),
              'loading...',
              widget.Bar(bar='#', tip='>')]

   ProgressBar.iteration(
       range(42), lambda item: sleep(0.01), widgets=widgets)

   # 50% (21/42) loading... [###############>...............]

Formats
-------

.. code:: python

   format_str = '{} {} ({})'

   widgets = [widget.Bar(), widget.Percentage(), widget.Num()]
   ProgressBar.iteration(
       range(100),
       lambda item: sleep(0.01),
       widgets=widgets,
       format_str=format_str)

   # [███████████████████████████████] 100% (100/100)

.. code:: python

   format_str = '{} *** {} *** ({})'

   widgets = [widget.Bar(), widget.Percentage(), widget.Num()]
   ProgressBar.iteration(
       range(100),
       lambda item: sleep(0.01),
       widgets=widgets,
       format_str=format_str)

   # [███████████████████████████████] *** 100% *** (100/100)

Print text
----------

.. code:: python

   from light_progress import puts

.. code:: python

   for item in ProgressBar.generation(range(42)):
       sleep(0.01)
       puts('item {}'.format(item))

   # ...
   # item 17
   # item 18
   # item 19
   # [███████████████▉...............] 50% (21/42)
