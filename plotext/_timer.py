import time

class timer_class:
    def __init__(self):
        self.times = {}

    def start(self, label):
        self.times[label] = {"start": time.perf_counter(), "elapsed": None}
        return self

    def stop(self, label):
        end = time.perf_counter()
        elapsed = 1000 * (end - self.times[label]["start"])
        self.times[label]["elapsed"] = elapsed
        self.times[label]["start"] = None
        return self

    def get_time(self, label):
        return self.times[label]["elapsed"]

    def to_string(self, time):
        return f"{time:.3f} ms"

    def get_total(self):
        total = 0
        for label in self.labels():
            total += self.get_time(label)
        return total

    def labels(self):
        return self.times.keys()

    def get_report(self, full = True):
        out = f"Plotext Timing Report " + self.to_string(self.get_total())
        if full:
            for label in self.labels():
                out += '\n└─ ' + label + ' ' + self.to_string(self.get_time(label))
        return out

    def report(self, full = True):
        print(self.get_report(full))
        return self

    def clear(self):
        self.times.clear()
        return self

    def __repr__(self):
        return self.get_report()
