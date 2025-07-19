import unittest

from plotext.prettydoc._docs import docs
from plotext._methods import *


# Test class for prettydoc module
class test_class(unittest.TestCase):

    def test_get_string(self):
        pd = docs()
        pd.add_function(object_methods.hash)
        pd.add_doc("This string describes my mean() function in general")
        pd.add_alias("average")

        pd.add_parameter("par1", "the first parameter")
        pd.add_parameter_spec('float', 1)

        pd.add_parameter("par2", "the second parameter")
        pd.add_parameter_spec('float', 2) 

        pd.add_output('the mean of the input parameters', 'float')

        # pd.show()

        expected = 'f7e6019335cece650fdbf7290ba80b9c5abea715dafd6383d0ee2d12282c1a84'
        self.assertEqual(pd._hash(), expected)


# Function to run the test suite
def run_tests():
    import plotext

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(plotext.prettydoc._test)

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run_tests()