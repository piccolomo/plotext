# A utility class to cycle through a predefined sequence of colors.

from plotext._methods import colors


class color_cycler:
    # Initialize with a color sequence
    def __init__(self, sequence):
        self.set_sequence(sequence)

    # Set a new sequence and reset usage
    def set_sequence(self, sequence):
        self.sequence = list(sequence)
        self.used = [False] * len(self.sequence)

    # Return next unused color, cycling if necessary
    def next_color(self):
        for i, used in enumerate(self.used):
            if not used:
                return self.sequence[i]
        self.reset()
        return self.next_color()

    # Mark a color as used
    def remove_color(self, color):
        for i, c in enumerate(self.sequence):
            if c == color:
                self.used[i] = True
        return self

    # Mark multiple colors as used
    def remove_colors(self, colors):
        [self.remove_color(color) for color in colors]
        return self

    # Get length of the sequence
    def get_length(self):
        return len(self.sequence)

    # Reset all colors to unused
    def reset(self):
        self.used = [False] * len(self.sequence)

    # Representation showing usage status
    def __repr__(self):
        used_status = [f"{colors.get_color_name(c)}{'▣' if u else '▢'}" for c, u in zip(self.sequence, self.used)]
        return f"ColorCycler: {'  '.join(used_status)}"
