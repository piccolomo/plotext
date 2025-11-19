import time

class timer_class:
    def __init__(self):
        self.times = {}  # store events

    # Get current high-resolution time
    def get_current_time(self):
        return time.perf_counter()

    # Check if an event exists
    def is_event(self, label):
        return label in self.times

    # Create a new event
    def create_event(self, label):
        self.times[label] = {"start": self.get_current_time(), "elapsed": 0, "counter": 0}
        return self

    # Start timing an event
    def time_event(self, label):
        self.times[label]["start"] = self.get_current_time()
        return self

    # Increment event counter
    def count_event(self, label):
        self.times[label]["counter"] += 1
        return self

    # Update elapsed time for an event
    def update_elapsed_time(self, label):
        elapsed = 1000 * (self.get_current_time() - self.times[label]["start"])
        self.times[label]["elapsed"] += elapsed
        return self

    # Start an event (create if not exists)
    def start(self, label):
        if not self.is_event(label):
            self.create_event(label)
        self.time_event(label)
        return self

    # Stop an event and update time/counter
    def stop(self, label):
        self.update_elapsed_time(label)
        self.count_event(label)
        return self

    # Get elapsed duration of an event
    def get_event_duration(self, label):
        return self.times[label]["elapsed"]

    # Format time to string
    def to_string(self, t):
        return f"{t:.3f} ms"

    # Get total elapsed time across all events
    def get_total_duration(self):
        return sum(self.get_event_duration(label) for label in self.labels())

    # Get list of event labels
    def labels(self):
        return self.times.keys()

    # Generate full report
    def get_report(self, full=True):
        out = f"Plotext Timing Report {self.to_string(self.get_total_duration())}"
        if full:
            for label in self.labels():
                out += f'\n└─ {label} {self.to_string(self.get_event_duration(label))}'
        return out

    # Print report
    def report(self, full=True):
        print(self.get_report(full))
        return self

    # Clear all events
    def clear(self):
        self.times.clear()
        return self

    # String representation
    def __repr__(self):
        return self.get_report()
