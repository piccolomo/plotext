# Test suite: exercises the public plotext API with deterministic build hashes

import unittest
import plotext as plt
from plotext import colorize, matrix, pixel
from plotext._methods import object as object_methods


# Reset the active plot to a known size before each plot-building test
def prepare_plot_size():
    plt.clf()
    plt.terminal.limit(0, 0)
    plt.plot_size(248, 59)


# Basic plot build tests
class basic_plots_tests(unittest.TestCase):

    # Scatter plot with default marker
    def test_scatter(self):
        expected = '1ad1b0a4b983ef3b9e10ea7d64d104f5ccaae97f4560d1e48be1d6567c9e8809'
        prepare_plot_size()
        y = plt.sin()
        plt.draw(y)
        plt.title("Scatter Plot")
        out = plt.build()
        self.assertEqual(out._hash(), expected)

    # Line plot (lines = True)
    def test_plot(self):
        expected = 'bdeb83974094091757bbccd6839a2e596f7b199a773e15e920f5c219b83acbd0'
        prepare_plot_size()
        y = plt.sin()
        plt.draw(y, lines = True)
        plt.title("Scatter Plot")
        out = plt.build()
        self.assertEqual(out._hash(), expected)

    # Logarithmic x / linear y plot with grid and axis labels
    def test_log_plot(self):
        expected = '97dea7b14cd1769a30f45063a308ca3df3bc163f26492863c7dd99df0ec8ecd0'
        prepare_plot_size()
        l = 10 ** 4
        y = plt.sin(periods = 2, length = l)
        plt.draw(y, lines = True)
        plt.scale("log", axis = "x"); plt.frequency(5, axis = "x")
        plt.scale("linear", axis = "y"); plt.frequency(7, axis = "y")
        plt.grid(True, axis = "x")
        plt.title("Logarithmic Plot")
        plt.label("logarithmic scale", axis = "x")
        plt.label("linear scale", axis = "y")
        out = plt.build()
        self.assertEqual(out._hash(), expected)


# Sinusoidal signal generator tests
class sin_tests(unittest.TestCase):

    # Deterministic sin output for a set of parameters
    def test1(self):
        expected = 'fdeed1bbd0757e2a7345b3d12533ce3334e4444fe4f90832713cb70885b980c0'
        result = plt.sin(periods = 3, length = 100, amplitude = 1, phase = 0.1, decay = 1)
        self.assertEqual(object_methods.hash_floats(result), expected)


# Colorize primitive tests
class colorize_tests(unittest.TestCase):

    # Colorize construction with all style attributes
    def test_get_string(self):
        result = colorize("text", "magenta", (101, 200, 30), "underline bold italic")
        expected = 'c1105bc0e1a1afedc37fea7276096d0b7fb821aaeb86afd2e7b3d65371349b68'
        self.assertEqual(result._hash(), expected)

    # Vertical stacking of two colorized strings
    def test_vstack(self):
        c1 = colorize("text1", "magenta", (101, 200, 30), "underline bold italic")
        c2 = colorize("text2", "red+", 101, "flash")
        result = c1._vstack(c2)
        expected = 'd44e58181e05e39c7ecfd1e436dc8e16f9b4d442b3c9e87c682efd3057e8cb3f'
        self.assertEqual(result._hash(), expected)

    # Horizontal stacking of two colorized strings
    def test_hstack(self):
        c1 = colorize("text1\ntest2", "magenta", (101, 200, 30), "underline bold italic")
        c2 = colorize("text3\ntest4", "red+", 101, "flash")
        result = c1._hstack(c2)
        expected = 'a7f0cba452dcc19486c84c1f695c8c7de24afce6e0eca09f69f204d3a2fc2b00'
        self.assertEqual(result._hash(), expected)


# Matrix primitive tests
class matrix_tests(unittest.TestCase):

    # Default-filled matrix of given size
    def test_get_string(self):
        result = matrix(100, 30)
        expected = 'fb9fa144fd10685dc273f5198ef32aa88685e2956fc4134de5f1561d41446189'
        self.assertEqual(result._hash(), expected)

    # Horizontal stacking of two colored matrices
    def test_hstack(self):
        result = matrix(10, 5, pixel("", "red")).hstack(matrix(20, 5))
        expected = '3ae4e161e54a788941f4d9cd3499b1d5c9a72fc095fa7cfe2b2bf748641e1c85'
        self.assertEqual(result._hash(), expected)


# Discover and run every test in this module
def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(plt._examples.test)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run_tests()
