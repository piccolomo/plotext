import unittest
from plotext._core import *
from plotext._utility import hash, hash_floats


class sin_tests(unittest.TestCase):
    def test1(self):
        expected = 'fdeed1bbd0757e2a7345b3d12533ce3334e4444fe4f90832713cb70885b980c0'
        result = sin(periods = 3, length = 100, amplitude = 1, phase = 0.1, decay = 1)
        self.assertEqual(hash_floats(result), expected)


class colorize_tests(unittest.TestCase):
    def test_get_string(self):
        result = colorize("text", "magenta", (101, 200, 30) , "underline bold italic")
        expected = 'c1105bc0e1a1afedc37fea7276096d0b7fb821aaeb86afd2e7b3d65371349b68'
        self.assertEqual(result._hash(), expected)

    def test_vstack(self):
        c1 = colorize("text1", "magenta", (101, 200, 30) , "underline bold italic")
        c2 = colorize("text2", "red+", 101, "flash")
        result = c1.vstack(c2)
        expected = 'd44e58181e05e39c7ecfd1e436dc8e16f9b4d442b3c9e87c682efd3057e8cb3f'
        self.assertEqual(result._hash(), expected)

    def test_hstack(self):
        c1 = colorize("text1\ntest2", "magenta", (101, 200, 30) , "underline bold italic")
        c2 = colorize("text3\ntest4", "red+", 101, "flash")
        result = c1.hstack(c2)
        expected = 'a7f0cba452dcc19486c84c1f695c8c7de24afce6e0eca09f69f204d3a2fc2b00'
        self.assertEqual(result._hash(), expected)


class matrix_tests(unittest.TestCase):
    def test_get_string(self):
        result = matrix(100, 30)
        expected = 'fb9fa144fd10685dc273f5198ef32aa88685e2956fc4134de5f1561d41446189'
        self.assertEqual(result._hash(), expected)

    def test_hstack(self):
        result = matrix(10, 5, pixel("", "red")).hstack(matrix(20, 5))
        expected = '3ae4e161e54a788941f4d9cd3499b1d5c9a72fc095fa7cfe2b2bf748641e1c85'
        self.assertEqual(result._hash(), expected)   


def run_tests():
    import plotext
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(plotext._test)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run_tests()

