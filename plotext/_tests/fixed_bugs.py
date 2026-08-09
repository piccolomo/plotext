# One test per bug already fixed, so that none of them comes back

import unittest
import os
import tempfile
import io
import contextlib
from datetime import datetime, timezone, timedelta
import plotext as plt
from plotext._plotter.frame.date import date_class


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


# Bugs in the rulers and their ticks
class ruler_bugs(unittest.TestCase):

    # An empty list of tick positions used to be ignored, bringing the automatic ticks back
    def test_empty_tick_list_removes_the_ticks(self):
        fig = prepare()
        fig.draw(fig.bar(["a", "b", "c"], [3, 5, 2]))
        fig.ruler("y").lim(0, 100).ticks([])
        rows = rows_of(fig)
        self.assertFalse(any(row.startswith(("25", "50", "75", "100")) for row in rows))

    # A list of tick positions is still honored
    def test_tick_list_is_drawn(self):
        fig = prepare()
        fig.draw(fig.bar(["a", "b", "c"], [3, 5, 2]))
        fig.ruler("y").ticks([2, 4])
        rows = rows_of(fig)
        self.assertTrue(any(row.lstrip().startswith("4") for row in rows))


# Bugs in the bars
class bar_bugs(unittest.TestCase):

    # A value of zero used to paint the row beneath it, hiding the bar it is stacked upon
    def test_zero_value_leaves_the_baseline_alone(self):
        fig = prepare()
        fig.draw(fig.bar(["d1", "d2"], [[4, 0], [1, 5]], stacked = True, marker = ["x", "o"]))
        rows = rows_of(fig)
        bottom_row = max(index for index, row in enumerate(rows) if "x" in row or "o" in row)
        second_column = rows[-1].index("d2")
        self.assertEqual(rows[bottom_row][second_column], "o")

    # Bars of a negative height are drawn below zero
    def test_negative_bars(self):
        fig = prepare()
        fig.draw(fig.bar(["a", "b"], [3, -2]))
        self.assertTrue(any("-" in row[:5] for row in rows_of(fig)))

    # The text written inside a bar is the one asked for
    def test_bar_labels_of_your_own(self):
        fig = prepare()
        fig.draw(fig.bar(["a", "b"], [3, 5], labeled = ["first", "second"]))
        rows = rows_of(fig)
        self.assertTrue(any("first" in row for row in rows))
        self.assertTrue(any("second" in row for row in rows))


# Bugs in date support
class date_bugs(unittest.TestCase):

    # A form carrying hours used to raise an error, the default origin no longer being readable
    def test_form_with_hours(self):
        converter = date_class()
        converter.activate(form = "%d/%m/%Y %H:%M")
        self.assertEqual(converter.origin("string"), "01/01/1900 00:00")

    # A second call to activate used to throw the form away
    def test_second_activate_keeps_the_form(self):
        converter = date_class()
        converter.activate(form = "%Y-%m-%d")
        converter.activate()
        self.assertEqual(converter.convert("2024-04-11", "string"), "2024-04-11")

    # An hour used to be lost turning a datetime object into a timestamp and back
    def test_no_hour_lost(self):
        converter = date_class()
        converter.activate(form = "%Y-%m-%d %H:%M")
        stamp = converter.convert(datetime(2024, 4, 11, 9, 0), "timestamp")
        self.assertEqual(converter.convert(stamp, "string"), "2024-04-11 09:00")

    # A date carrying its own zone used to be written back in UTC, with the hours shifted
    def test_zone_of_the_axis(self):
        converter = date_class()
        converter.activate(form = "%d/%m/%Y %H:%M", zone = 3)
        moscow = timezone(timedelta(hours = 3))
        stamp = converter.convert(datetime(2026, 3, 1, 12, 0, tzinfo = moscow), "timestamp")
        self.assertEqual(converter.convert(stamp, "string"), "01/03/2026 12:00")

    # A date given to line() or event() used to stay a string, which broke the plot when it was built
    def test_dates_in_lines_and_events(self):
        fig = prepare()
        fig.date("x").activate(form = "%H:%M")
        fig.event(["02:00", "12:00", "20:00"])
        self.assertIn("02:00", rows_of(fig)[-1])


# Bugs elsewhere
class other_bugs(unittest.TestCase):

    # A signal wholly outside the limits used to crash the legend
    def test_signal_outside_the_limits(self):
        fig = prepare()
        fig.draw(fig.signal([1] * 20).label("far below"))
        fig.ruler("y").lim(10, 190)
        self.assertEqual(fig.build().size(), (60, 20))

    # Deleting a file outside the folder the program runs in is refused; two folders of their own are made, since on windows the temporary one may sit inside the folder the tests run from
    def test_delete_outside_the_working_folder(self):
        with tempfile.TemporaryDirectory() as working_folder, tempfile.TemporaryDirectory() as other_folder:
            here = os.getcwd()
            os.chdir(working_folder)
            try:
                outside = os.path.join(other_folder, "plotext_test_outside.txt")
                plt.file.write("keep me", outside)
                note = io.StringIO()
                with contextlib.redirect_stderr(note):
                    plt.file.delete(outside)
                self.assertTrue(os.path.exists(outside))
                self.assertIn("outside the working folder", note.getvalue())
                plt.file.delete(outside, safe = False)
                self.assertFalse(os.path.exists(outside))
            finally:
                os.chdir(here)

    # A colorized legend label used to be measured with its color codes counted as characters, widening the legend box over the plot
    def test_colorized_legend_label(self):
        fig = prepare()
        fig.draw(fig.signal(plt.sin(), marker = "hd").lines().label(plt.colorize("wave", "red")))
        rows = rows_of(fig)
        self.assertEqual(len({len(row) for row in rows}), 1)
        self.assertTrue(any("│ ▚ wave │" in row for row in rows))

    # A group of value zero used to paint one row of its own, covering the top of the group below it
    def test_zero_group_in_a_stacked_bar(self):
        fig = prepare()
        fig.draw(fig.bar(["a"], [[10], [0]], stacked = True))
        plot = fig.build()
        column = plot.width() // 2
        colors = {plot.get(row, column).foreground() for row in range(1, plot.height() - 3)}
        self.assertEqual(len(colors), 1)

    # A saved web page used to be the plot alone, so a browser guessed the character set and used a proportional font
    def test_saved_page_is_whole(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "plot.html")
            fig = prepare()
            fig.draw(fig.signal(plt.sin(), marker = "hd"))
            fig.build().save(path)
            page = plt.file.read(path)
            self.assertIn("<!DOCTYPE html>", page)
            self.assertIn("utf-8", page)
            self.assertIn("monospace", page)

    # A legend label used to lose its color when the signal label became a matrix, leaving the terminal to paint it
    def test_legend_label_is_colored(self):
        fig = prepare()
        fig.draw(fig.signal(plt.sin(), marker = "hd").lines().label("wave"))
        plot = fig.build()
        rows = rows_of(fig)
        row = [index for index, line in enumerate(rows) if "wave" in line][0]
        column = rows[row].index("wave")
        self.assertIsNotNone(plot.get(row, column).foreground())

    # The canvas color default leaves the terminal showing through
    def test_transparent_canvas(self):
        fig = prepare()
        fig.canvas("default")
        fig.draw(fig.signal(plt.sin()))
        plot = fig.build()
        self.assertEqual(plot.get(plot.height() // 2, plot.width() - 2).background(), None)
