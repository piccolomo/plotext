
class color_cycler:
    def __init__(self, sequence):
        self.set_sequence(sequence)

    def set_sequence(self, sequence):
        self.sequence = list(sequence)
        self.used = [False] * len(self.sequence)


    def next_color(self):
        for i, used in enumerate(self.used):
            if not used:
                #self.used[i] = True
                return self.sequence[i]
        self.reset()
        return self.next_color()

    def remove_color(self, color):
        for i, c in enumerate(self.sequence):
            if c == color:
                self.used[i] = True
        return self

    def remove_colors(self, colors):
        [self.remove_color(color) for color in colors]
        return self

    def get_length(self):
        return len(self.sequence)

    def reset(self):
        self.used = [False] * len(self.sequence)

    def __repr__(self):
        used_status = [f"{c}{'▣' if u else '▢'}" for c, u in zip(self.sequence, self.used)]
        return f"ColorCycler: {'  '.join(used_status)}"