# Tests of the primitives, on exact values: pixel colors, matrix positions and sizes, colorize widths

import unittest
import plotext as plt


# A color given to a pixel is the color read back from it
class pixel_tests(unittest.TestCase):

    # Red, green and blue values given are returned unchanged
    def test_rgb_color(self):
        px = plt.pixel(foreground = (10, 123, 200), background = (1, 2, 3))
        self.assertEqual(px.foreground(), (10, 123, 200))
        self.assertEqual(px.background(), (1, 2, 3))

    # A color left out is no color at all
    def test_missing_color(self):
        px = plt.pixel(foreground = "red")
        self.assertEqual(px.background(), None)

    # The code default means no color, so whatever the terminal shows stays there
    def test_default_color(self):
        px = plt.pixel(foreground = "default", background = "default")
        self.assertEqual(px.foreground(), None)
        self.assertEqual(px.background(), None)

    # A name and the integer it stands for give the same color
    def test_name_and_integer_agree(self):
        self.assertEqual(plt.pixel(foreground = "red").foreground(), plt.pixel(foreground = 1).foreground())


# A matrix holds its pixels at the positions they were given
class matrix_tests(unittest.TestCase):

    # The size asked for is the size obtained
    def test_size(self):
        m = plt.matrix(20, 7)
        self.assertEqual(m.size(), (20, 7))

    # A pixel inserted at a row and column is the pixel read back from there
    def test_insert_and_get(self):
        m = plt.matrix(10, 4, plt.pixel(background = "white"))
        m.insert(3, 2, plt.colorize("x", pixel = plt.pixel(foreground = (5, 6, 7))))
        self.assertEqual(m.get(2, 3).foreground(), (5, 6, 7))

    # A negative index counts from the end
    def test_negative_index(self):
        m = plt.matrix(10, 4)
        m.insert(9, 3, plt.colorize("x", pixel = plt.pixel(foreground = (9, 9, 9))))
        self.assertEqual(m.get(-1, -1).foreground(), (9, 9, 9))

    # Two matrices side by side add their widths and keep their height
    def test_hstack_size(self):
        m = plt.matrix(10, 4).hstack(plt.matrix(6, 4))
        self.assertEqual(m.size(), (16, 4))

    # Two matrices one above the other add their heights and keep their width
    def test_vstack_size(self):
        m = plt.matrix(10, 4).vstack(plt.matrix(10, 3))
        self.assertEqual(m.size(), (10, 7))

    # A colorless string carries no color codes and as many rows as the matrix
    def test_colorless_string(self):
        m = plt.matrix(10, 4, plt.pixel(background = "red"))
        plain = m.string(colorless = True)
        self.assertEqual(plain.count("\033"), 0)
        self.assertEqual(len(plain.rstrip("\n").split("\n")), 4)


# A colorized string counts its characters and the columns they take on screen
class colorize_tests(unittest.TestCase):

    # The text given is the text printed, colors aside
    def test_string(self):
        self.assertEqual(plt.colorize("Colorless", pixel = plt.pixel(foreground = "red")).string(colorless = True), "Colorless")

    # A character counts once, while on screen a Chinese one takes two columns
    def test_wide_characters(self):
        wide = plt.colorize("温度")
        self.assertEqual(wide.length(), 2)
        self.assertEqual(wide.matrix().width(), 4)

    # Two colorized strings side by side give a matrix as wide as both of them
    def test_hstack_width(self):
        self.assertEqual(plt.colorize("abc").hstack(plt.colorize("de")).width(), 5)
