# A utility class to cycle through a predefined sequence of pixels.

from plotext._primitives.pixel import pixel as pixel_class


class color_cycler:
    # Initialize with a sequence of pixel objects
    def __init__(self, sequence):
        self.set_sequence(sequence)

    # Accepts a sequence of pixel objects (caller, typically defaults, is responsible for the promotion)
    def set_sequence(self, sequence):
        self.sequence = list(sequence)
        self.used = [False] * len(self.sequence)

    # Return a copy of the next unused pixel (wrapping around when exhausted)
    def next_pixel(self):
        for i, used in enumerate(self.used):
            if not used:
                return self.sequence[i].copy()
        self.reset()
        return self.next_pixel()

    # Mark sequence pixels that fully match p (fg + bg + style) as used
    def remove_pixel(self, p):
        for i, q in enumerate(self.sequence):
            if q._equals(p):
                self.used[i] = True
        return self

    # Mark multiple pixels
    def remove_pixels(self, pixels):
        for p in pixels:
            self.remove_pixel(p)
        return self

    def length(self):
        return len(self.sequence)

    def reset(self):
        self.used = [False] * len(self.sequence)

    def __repr__(self):
        # Paint each ▣/▢ glyph with its pixel's own ANSI colour (recycles pixel._get_string() which wraps the literal "PlotextPixel()" in the pixel's codes)
        return "PlotextColorCycler(" + "  ".join(p._get_string().replace("PlotextPixel()", '▣' if u else '▢') for p, u in zip(self.sequence, self.used)) + ")"
