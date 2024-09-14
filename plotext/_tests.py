import unittest
from plotext._core import *

class Test(unittest.TestCase):
    equal = unittest.TestCase.assertEqual

    def equal_floats(self, a, b, decimals = 5):
        self.assertAlmostEqual(a, b)
        return self

    def equal_float_lists(self, list1, list2, decimals = 5):
        self.equal(len(list1), len(list2))
        [self.equal_floats(a, b, decimals = decimals) for a, b in zip(list1, list2)]
        return self
             

class sin_tests(Test):
    def test1(self):
        expected = [0.3090169943749474, -0.22142035196905407, 0.1586546149840967]
        result = sin(periods = 3, length = 3, amplitude = 1, phase = 0.1, decay = 1)
        self.equal_float_lists(result, expected)

    def test2(self):
        expected = [1.902113032590307, 0.9765773932668622, 0.501391551763431]
        result = sin(periods = 2, length = 3, amplitude = 2, phase = 0.4, decay = 2)
        self.equal_float_lists(result, expected)


def run_tests():
    import plotext
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(plotext._tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run_tests()

