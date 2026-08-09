# Tests of the built plot, asking questions of the result rather than comparing pictures

import unittest
import plotext as plt


# Start from a plot of a known size, so that rows and columns can be counted
def prepare(width = 60, height = 20):
    fig = plt.figure
    fig.clear()
    plt.terminal.limit(False, False)
    fig.plot_size(width, height)
    return fig


# The rows of the built plot, with no colors in them
def rows_of(fig):
    return fig.build().string(colorless = True).rstrip("\n").split("\n")


# The plot is drawn where the data says, inside the size asked for
class canvas_tests(unittest.TestCase):

    # The plot is as wide and as tall as asked
    def test_size(self):
        fig = prepare(60, 20)
        fig.draw(fig.signal(plt.sin()))
        plot = fig.build()
        self.assertEqual(plot.size(), (60, 20))

    # A signal with no points leaves the canvas empty
    def test_empty_signal(self):
        fig = prepare()
        fig.draw(fig.signal([], []))
        painted = sum(row.count("█") + row.count("▚") for row in rows_of(fig))
        self.assertEqual(painted, 0)

    # The tallest bar reaches the top row of the canvas, the shortest stays at the bottom
    def test_bar_heights(self):
        fig = prepare()
        fig.draw(fig.bar(["a", "b"], [1, 10]))
        rows = rows_of(fig)
        short_column, tall_column = rows[-1].index("a"), rows[-1].index("b")
        highest_painted_row = min(index for index, row in enumerate(rows) if "█" in row)
        self.assertIn("█", rows[highest_painted_row][tall_column - 1 : tall_column + 2])
        self.assertNotIn("█", rows[highest_painted_row][short_column - 1 : short_column + 2])

    # Nothing is painted outside the limits asked for, once they are pinned to the plot edge
    def test_limits_hold(self):
        fig = prepare()
        fig.draw(fig.signal([1] * 20))
        fig.ruler("y").lim(10, 190).alignment(lim = "edge")
        fig.ruler("x").lim(1, 20)
        painted = sum(row.count("▚") + row.count("█") + row.count("▄") for row in rows_of(fig))
        self.assertEqual(painted, 0)

    # A colorless build carries no color codes
    def test_colorless_build(self):
        fig = prepare()
        fig.draw(fig.signal(plt.sin()))
        self.assertEqual(fig.build().string(colorless = True).count("\033"), 0)


# The legend appears by itself and lists only what carries a label
class legend_tests(unittest.TestCase):

    # A labelled signal puts its label on the plot
    def test_label_shows(self):
        fig = prepare()
        fig.draw(fig.signal(plt.sin()).label("wave"))
        self.assertTrue(any("wave" in row for row in rows_of(fig)))

    # A signal left unlabelled brings no legend with it
    def test_no_label_no_legend(self):
        fig = prepare()
        fig.draw(fig.signal(plt.sin()))
        self.assertFalse(any("┌─" in row[1:] for row in rows_of(fig)[1:-1]))

    # Of two signals only the labelled one is listed
    def test_only_labelled_listed(self):
        fig = prepare()
        fig.draw(fig.signal(plt.sin()).label("named"))
        fig.draw(fig.signal(plt.sin(phase = 1)))
        rows = rows_of(fig)
        self.assertTrue(any("named" in row for row in rows))

    # The legend switched off stays hidden even with labels around
    def test_legend_off(self):
        fig = prepare()
        fig.draw(fig.signal(plt.sin()).label("wave"))
        fig.legend(False)
        self.assertFalse(any("wave" in row for row in rows_of(fig)))


# A grid of subplots fills the size of the figure
class subplot_tests(unittest.TestCase):

    # Four panels build together at the size of the figure
    def test_grid_size(self):
        fig = prepare(80, 24)
        fig.subplots(2, 2)
        for row in [1, 2]:
            for col in [1, 2]:
                panel = fig.subplot(row, col)
                panel.draw(panel.signal(plt.sin()))
        self.assertEqual(fig.build().size(), (80, 24))

    # Each panel takes its share of the figure width
    def test_panel_share(self):
        fig = prepare(80, 24)
        fig.subplots(1, 2)
        for col in [1, 2]:
            panel = fig.subplot(1, col)
            panel.draw(panel.signal(plt.sin()))
        fig.build()
        self.assertEqual(fig.subplot(1, 1).size()[0], 40)
