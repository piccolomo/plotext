# Six whole plots frozen by their hash, to catch a change nobody meant to make
# A failure here is not a bug by itself: read the two plots, and when the new one is right, write the new hash in

import unittest
import plotext as plt


# Start from a plot of a known size, with the marker named, since the default one differs between systems
def prepare(width = 70, height = 18):
    fig = plt.figure
    fig.clear()
    plt.terminal.limit(False, False)
    fig.plot_size(width, height)
    return fig


# Every plot below is built the same way and compared with the hash recorded beside it
class hash_tests(unittest.TestCase):

    # Points alone
    def test_scatter(self):
        fig = prepare()
        fig.draw(fig.signal(plt.sin(length = 100), marker = "hd"))
        fig.title("scatter")
        self.assertEqual(fig.build()._hash(), "fb22721a8a4dfc0c6cf3a450e7dda2b4e73f384a9e7a978edd59ae1c73419c38")

    # Points joined by lines
    def test_line(self):
        fig = prepare()
        fig.draw(fig.signal(plt.sin(length = 100), marker = "hd").lines())
        fig.title("line")
        self.assertEqual(fig.build()._hash(), "455f74db3ca0ee40f65e5551f89f44825c2fb7f0ab2aeb4f8e0fbedc6de18d29")

    # Three bars
    def test_bar(self):
        fig = prepare()
        fig.draw(fig.bar(["a", "b", "c"], [3, 5, 2], marker = "full"))
        fig.title("bar")
        self.assertEqual(fig.build()._hash(), "5b2b72722594497cee4d0fc5bdf9f8cae14577679140bbcc5aef743e3cd7f1f8")

    # Two panels side by side
    def test_subplots(self):
        fig = prepare()
        fig.subplots(1, 2)
        for col in [1, 2]:
            panel = fig.subplot(1, col)
            panel.draw(panel.signal(plt.sin(length = 50, phase = col - 1), marker = "hd").lines())
            panel.title("panel " + str(col))
        self.assertEqual(fig.build()._hash(), "0324ac5f0b60c8cb9c03898cc2d69809f19e33e0b99b150378130db628087441")

    # A colored table of values
    def test_heatmap(self):
        fig = prepare(60, 14)
        fig.draw(fig.heatmap([[1, 2, 3], [4, 5, 6], [7, 8, 9]], map = "viridis", fill = 1))
        self.assertEqual(fig.build()._hash(), "cd54e5beeb45206caf0ff16a2c8cafd89755da9c1fcbe26fc748f0b0612222f1")

    # Prices over three days
    def test_candlestick(self):
        fig = prepare(60, 14)
        fig.date("x").activate()
        data = {"date": ["01/01/2024", "02/01/2024", "03/01/2024"],
                "open": [1, 2, 3], "close": [2, 3, 2], "high": [3, 4, 4], "low": [0.5, 1.5, 1.5]}
        fig.draw(fig.candlestick(data))
        self.assertEqual(fig.build()._hash(), "1a0d07dd3da59b46639c8e462f13aa3f0439db1fb44f5039e5da393858a74c39")
