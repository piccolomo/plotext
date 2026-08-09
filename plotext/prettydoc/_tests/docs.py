# Tests of the docstring builder, asking what the built text says

import unittest
import re
from plotext.prettydoc._primitives.docs import docs
from plotext._methods import object as object_methods


# The text of a built docstring, with no colors in it
def text_of(built):
    return re.sub(r'\033\[[0-9;]*m', '', built.string())


# What goes into a docstring comes out of it
class docs_tests(unittest.TestCase):

    # Build the same docstring used across these tests
    def build(self):
        built = docs()
        built.function(object_methods.hash)
        built.description("This string describes my mean() function in general", alias = "average")
        built.parameter("par1", "the first parameter", 'float', 1)
        built.parameter("par2", "the second parameter", 'float', 2)
        built.output('the mean of the input parameters', 'float')
        return built

    # The description given is the description written
    def test_description(self):
        self.assertIn("This string describes my mean() function in general", text_of(self.build()))

    # Every parameter is named, with its own explanation
    def test_parameters(self):
        text = text_of(self.build())
        self.assertIn("par1", text)
        self.assertIn("par2", text)
        self.assertIn("the second parameter", text)

    # A parameter carries its type and the value it takes when left out
    def test_parameter_type_and_default(self):
        text = text_of(self.build())
        self.assertIn("float", text)
        self.assertIn("1", text)

    # The output line says what comes back
    def test_output(self):
        self.assertIn("the mean of the input parameters", text_of(self.build()))

    # A docstring with nothing in it builds all the same
    def test_empty_docstring(self):
        self.assertEqual(type(text_of(docs())), str)
