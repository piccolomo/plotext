:orphan:

.. _showcase_code:

Showcase Code
=============

| The picture on the front page is a single plot divided in **five panels**, all moving at once, drawn straight in the :doc:`terminal <terminal>`.
| On the left, two waves slide past each other, a group of :ref:`bars <stacked_bar>` rises and falls, and three :ref:`histograms <histogram>` drift apart and back together.
| On the right, the bundled :ref:`picture <image>` of a puppy sits above the |plotext| logo scrolling by, drawn as a :ref:`heatmap <heatmap>` of its own colors.
| Every panel title is written with a different :ref:`effect <effects>`, its colors moving from one frame to the next.

The whole thing is the loop below, which redraws the plot in place until ``q`` is pressed, as the :doc:`streaming <stream>` page describes.

.. literalinclude:: code/showcase.py
   :language: python

.. image:: images/showcase.webp
   :alt: signals, stacked bars, histograms, a picture and the scrolling logo, all moving at once


.. important:: This is a **taste**, not a tour: it uses a handful of what |plotext| offers, leaving out :doc:`dates <date>` and :ref:`candlesticks <candlestick>`, :ref:`error bars <error>` and :ref:`event plots <event>`, :ref:`shapes <rectangle>` and text on the plot, :ref:`gifs <gif>` and :ref:`video <video>`, :doc:`themes <theme>` and much else. The :doc:`front page <index>` list and the :ref:`user guide <user_guide>` name the rest.

.. tip:: The picture is read and resampled **once**, before the loop, and simply redrawn on each frame: doing it inside the loop costs ten times the whole rest of the plot.
