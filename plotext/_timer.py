import time

class timer_class:
    def __init__(self):
        self.times = {}

    def get_current_time(self):
        return time.perf_counter()

    def is_event(self, label):
        return label in self.times

    def create_event(self, label):
        self.times[label] = {"start": self.get_current_time(), "elapsed": 0, "counter": 0}

    def time_event(self, label):
        self.times[label]["start"] =  self.get_current_time()

    def count_event(self, label):
        self.times[label]["counter"] += 1

    def update_elapsed_time(self, label):
        elapsed = 1000 * (self.get_current_time() - self.times[label]["start"])
        self.times[label]["elapsed"] += elapsed

    def start(self, label): 
        self.create_event(label) if not self.is_event(label) else None
        self.time_event(label) 
        return self

    def stop(self, label):
        self.update_elapsed_time(label)
        self.count_event(label)
        #self.times[label]["start"] = None
        return self

    def get_event_duration(self, label):
        return self.times[label]["elapsed"]

    def to_string(self, time):
        return f"{time:.3f} ms"

    def get_total_duration(self):
        total = 0
        for label in self.labels():
            total += self.get_event_duration(label)
        return total

    def labels(self):
        return self.times.keys()

    def get_report(self, full = True):
        out = f"Plotext Timing Report " + self.to_string(self.get_total_duration())
        if full:
            for label in self.labels():
                out += '\n└─ ' + label + ' ' + self.to_string(self.get_event_duration(label))
        return out

    def report(self, full = True):
        print(self.get_report(full))
        return self

    def clear(self):
        self.times.clear()
        return self

    def __repr__(self):
        return self.get_report()
