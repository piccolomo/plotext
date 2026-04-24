Pretty Docstrings
=================

You can create colorful and elegant docstrings using the `prettydoc` module within `plotext`. Below is an example of how to utilize this feature on two dummy functions ``mean()`` and ``harmonic_mean()``.

.. literalinclude:: code/prettydoc.py
   :class: code-block
   :language: python3

And here are the resulting docstrings:

.. image:: images/prettydoc.png
   :alt: Prettydoc Example
   :width: 650

.. note:: 

    * All **plotext documentation** is written using `prettydoc`. The ``plotext.doc`` container holds all basic `plotext` docstrings, while ``plotext.prettydoc.doc`` holds all `prettydoc` related docstrings.

    * This feature is currently **under active development**. We welcome feedback and suggestions! If you encounter any issues or have feature requests, please open `a new issue <https://github.com/piccolomo/plotext/issues/new>`_ on GitHub.

The following sections comment and explain the previous code.


Initialize
----------

- **initialize the container**: in the example above, we instantiate a new ``prettydoc.docs()`` container and define two dummy functions, ``mean()`` and ``harmonic_mean()``.

- **add a function**: the ``add_function()`` method is used to add a function to the ``docs()`` container. Once a function is added, all subsequent methods will apply to the most recently added function. It requires the actual function as parameter. 

.. note:: 

    `prettydoc` can handle functions as well as **class methods**.


.. _document:

Document
--------

The following points outline the key methods and procedures for documenting functions using the `prettydoc` module:


#. **add main description**: the ``docs.add_doc()`` method is used to add the main function documentation. It requires a string as parameter.

#. **add alias**: if the function has an alternative name, the ``docs.add_alias()`` method is available to document it. It requires a string as parameter.

#. **add parameters**: for detailing a function parameter use the ``add_parameter()`` which requires the parameter ``name`` and main ``doc`` description as string parameters.

#. **add parameter details**: to add a parameter ``type`` and ``default`` values use the ``add_parameter_specs(type, default)`` method. 

#. **reuse past parameters**: to avoid redundancy, if the current function shares parameters with a previously documented function, the ``add_past_parameter()`` method allows you to reuse already described parameters. It requires the parameter and function names as string parameters. 

   .. note:: 

    You can still modify the details of a previously documented parameter in the same way as for a new parameter: using the ``add_parameter_specs()`` method, previously presented. 

#. **add output details**: to add the details of a function output (basic ``doc`` and ``type``) use the ``add_output(doc, type)`` method. 

#. **reuse past output**: use the ``add_past_output()`` to reuse an already described function output. It requires the function name as its string parameter. 


Process and Display
-------------------

- **process the docstrings**: once all functions have been added, use the ``docs.update()`` method to finalize and add the docstrings to the corresponding functions.

- **displays all docstrings**: to displays all generated docstrings use the ``docs.show()`` method.

- **displays a specific docstring**: The `docs()` container holds methods, named after the functions, that display the corresponding function's docstring. Therefore to view a specific docstring, you can either use the usual ``print(mean.__doc__)`` or the simplified ``docs.mean()`` access point.
   
.. note:: 

    * Additional technical details can be found in the :ref:`prettydoc_api` API.


.. _doc_color:

Change Coloring
---------------
The coloring of each element in the documentation can be customized in the following two ways.

.. rubric:: Change Specific Element Coloring

The first method involves selecting your preferred coloring using the :ref:`colorize <colorize>` tool, then passing this object to any of the methods described in the :ref:`document` section. For example, to add a colored alias, use:

.. code-block:: python

   add_alias(colorize('average', fullground = 'blue+', style = 'italic bold'))


.. rubric:: Change Default Component Coloring

The second method allows you to change the default coloring of a specific docstring component. The ``set_default_pixel()`` method requires a ``component`` string name and a :ref:`pixel <pixel>` representing the desired coloring. For example:

.. code-block:: python

   set_default_pixel('alias', pixel('blue+', style='italic bold'))

sets the alias *component* (when present) of all generated docstrings to the specific coloring. By calling this code at the beginning, all subsequent alias components will adopt the chosen color settings.


.. rubric:: Docstring Components

The available docstring components can be accessed using the ``plotext.prettydoc.components()`` method, shown in the image below:

.. image:: images/components.png

Use these codes to customize the default coloring for each *component* of the docstring.


Shortcuts
---------

Using one-word shortcuts can be advantageous when documenting many functions. Using these shortcuts the initial example looks like:


.. literalinclude:: code/prettydoc_short.py
	:language: python