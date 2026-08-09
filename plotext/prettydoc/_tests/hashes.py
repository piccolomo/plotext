# A whole docstring frozen by its hash, to catch a change nobody meant to make
# A failure here is not a bug by itself: read the docstring, and when it is right, write the new hash in

import unittest
from plotext.prettydoc._primitives.docs import docs
from plotext._methods import object as object_methods


# The docstring of a function with two parameters and one output
class hash_tests(unittest.TestCase):

    # Description, parameters and output together
    def test_full_docstring(self):
        built = docs()
        built.function(object_methods.hash)
        built.description("This string describes my mean() function in general", alias = "average")
        built.parameter("par1", "the first parameter", 'float', 1)
        built.parameter("par2", "the second parameter", 'float', 2)
        built.output('the mean of the input parameters', 'float')
        self.assertEqual(built._hash(), 'df6d64bbcc75016b782f9fb8daa6718c9b791b5ae81e97d26f771a12ed93733e')
