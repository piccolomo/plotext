from plotext._date import date_class, dt
import math


def get_data_type(data):
    return 'numerical' if len(data) == 0 else 'string' if isinstance(data[0], str) else 'datetime' if isinstance(data[0], dt) else 'numerical'


class string_converter_class():
    def __init__(self):
        self.clear()

    def clear(self):
        self.mapping = {}

    def convert(self, strings):
        [self.mapping.update({el: len(self.mapping)}) for el in strings if el not in self.mapping]
        return [self.mapping[el] for el in strings]

    def get_ticks(self):
        ticks = list(self.mapping.values())
        labels = list(self.mapping.keys())
        return ticks, labels
