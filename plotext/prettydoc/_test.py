import unittest
from ._docs import docs
from .._utility import hash


class prettydoc_test(unittest.TestCase):
    def test_get_string(self):
        pd = docs() 
        pd.add_function(hash) 
        pd.add_doc("This string describes my mean() function in general") 
        pd.add_alias("average") 
        pd.add_parameter("par1", "the first parameter")
        pd.add_parameter_spec('float', 1)
        pd.add_parameter("par2", "the second parameter")
        pd.add_parameter_spec('float', 2)
        pd.add_output('the mean of the input parameters', 'float')
        expected = '8a1aafee3f3c1ad9c2635e7267cdb5d492fa11a8a906e6293ec25602cf7cc20f'
        self.assertEqual(pd._hash(), expected)


def run_tests():
    import plotext
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(plotext.prettydoc._test)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run_tests()

