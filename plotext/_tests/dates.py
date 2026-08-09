# Tests of date support: the three ways of writing a date, and the settings holding them together

import unittest
from datetime import datetime, timedelta, timezone
import plotext as plt
from plotext._plotter.frame.date import date_class


# A date given one way comes back the same way
class conversion_tests(unittest.TestCase):

    # A date written as text survives text to timestamp and back
    def test_text_round_trip(self):
        converter = date_class()
        converter.activate(form = "%d/%m/%Y")
        stamp = converter.convert("11/04/2024", "timestamp")
        self.assertEqual(converter.convert(stamp, "string"), "11/04/2024")

    # A date carrying hours and minutes survives the same trip
    def test_hours_round_trip(self):
        converter = date_class()
        converter.activate(form = "%d/%m/%Y %H:%M")
        stamp = converter.convert("11/04/2024 09:30", "timestamp")
        self.assertEqual(converter.convert(stamp, "string"), "11/04/2024 09:30")

    # The same moment written as text and as an object gives the same timestamp
    def test_text_and_object_agree(self):
        converter = date_class()
        converter.activate(form = "%Y-%m-%d %H:%M")
        from_text = converter.convert("2024-04-11 09:00", "timestamp")
        from_object = converter.convert(datetime(2024, 4, 11, 9, 0), "timestamp")
        self.assertEqual(from_text, from_object)

    # A date carrying its own time zone keeps it
    def test_own_time_zone(self):
        converter = date_class()
        converter.activate(form = "%Y-%m-%d %H:%M")
        east = datetime(2024, 4, 11, 9, 0, tzinfo = timezone(timedelta(hours = 5)))
        self.assertEqual(converter.convert(converter.convert(east, "timestamp"), "string"), "2024-04-11 04:00")


# The form and the origin are settings of their own, each left alone unless given
class setting_tests(unittest.TestCase):

    # The origin is the first of January 1900 until asked otherwise
    def test_default_origin(self):
        converter = date_class()
        self.assertEqual(converter.origin("string"), "01/01/1900")

    # An origin given as text, as an object or as a number is accepted
    def test_origin_forms(self):
        converter = date_class()
        converter.activate(form = "%Y-%m-%d", origin = "2020-01-01")
        self.assertEqual(converter.origin("string"), "2020-01-01")
        converter.activate(origin = datetime(1995, 3, 2, tzinfo = timezone.utc))
        self.assertEqual(converter.origin("string"), "1995-03-02")

    # Clearing brings back the default form and origin
    def test_clear(self):
        converter = date_class()
        converter.activate(form = "%Y-%m-%d", origin = "2020-01-01")
        converter.clear()
        self.assertEqual(converter.origin("string"), "01/01/1900")
        self.assertEqual(converter.convert("11/04/2024", "timestamp"), date_class().convert("11/04/2024", "timestamp"))


# Dates reach the plot as text, as objects and as timestamps alike
class plot_tests(unittest.TestCase):

    # A plot of datetime objects writes the dates along the axis
    def test_datetime_objects_on_the_axis(self):
        fig = plt.figure
        fig.clear()
        plt.terminal.limit(False, False)
        fig.plot_size(80, 16)
        fig.date("x").activate(form = "%Y-%m-%d %H:%M")
        start = datetime(2024, 4, 11, 9, 0)
        times = [start + timedelta(minutes = 30 * step) for step in range(10)]
        fig.draw(fig.signal(times, plt.sin(length = 10)))
        rows = fig.build().string(colorless = True).rstrip("\n").split("\n")
        self.assertTrue(any("2024-04-11" in row for row in rows))
