Basic Plots
===========

.. _scatter:

Scatter Plot
------------

Here is a simple scatter plot:

.. code-block:: python

    import plotext as plt
    y = plt.sin()  # sinusoidal test signal
    plt.scatter(y)
    plt.title("Scatter Plot")  # to apply a title
    plt.show()  # to finally plot

Or directly on terminal:

.. code-block:: console

    python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Scatter Plot'); plt.show()"

.. image:: https://raw.githubusercontent.com/piccolomo/plotext/master/data/scatter.png
    :alt: scatter

More documentation can be accessed with ``plotext.doc.scatter()``.