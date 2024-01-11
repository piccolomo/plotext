class placement_class():

    axes = ['x', 'y']
    axis = axes[0]
    
    xsides = ["lower", "upper"] 
    ysides = ["left", "right"]
        
    xside = xsides[0]
    yside = ysides[0]
    
    orientations = ['horizontal', 'vertical']
    orientations_short = ['h', 'v']
    orientations_int = [0, 1]
    orientation = orientations[0]
        
    horizontal_alignments = ['left', 'center', 'right', 'dynamic']
    horizontal_alignments_short = ['l', 'c', 'r', 'd']
    horizontal_alignments_int = [-1, 0, 1, 2]
    horizontal_alignment = horizontal_alignments[0]
        
    vertical_alignments = ['top', 'center', 'bottom']
    vertical_alignments_short = ['t', 'c', 'b']
    vertical_alignments_int = [-1, 0, 1]
    vertical_alignment = vertical_alignments[0]

    def correct_axis(self, axis = None):
        is_integer = isinstance(axis, int) and 1 <= axis <= 2
        axis = self.axes[axis - 1] if is_integer else axis
        axis = self.axis if axis is None else axis
        axis = axis if axis in self.axes else self.axis
        return axis
    
    def correct_side(self, axis = None, side = None):
        axis = self.correct_axis(axis)
        sides = self.xsides if axis == 'x' else self.ysides
        is_integer = isinstance(side, int) and 1 <= side <= 2
        not_correct = side is None or (isinstance(side, str) and side.strip() not in sides)
        return sides[side - 1] if is_integer else sides[0] if not_correct else side.strip()

    def correct_xside(self, side = None):
        return self.correct_side('x', side)

    def correct_yside(self, side = None):
        return self.correct_side('y', side)

    def xside_to_index(self, xside = None):
        xside = self.correct_xside(xside)
        return self.xsides.index(xside)

    def yside_to_index(self, yside = None):
        yside = self.correct_yside(yside)
        return self.ysides.index(yside)
    

    def correct_orientation(self, orientation = None):
        orientation = self.orientation if orientation is None else orientation
        orientation = self.orientations[self.orientations_short.index(orientation)] if orientation in self.orientations_short else orientation
        return self.orientation if orientation not in self.orientations else orientation

    def correct_horizontal_alignment(self, alignment = None):
        alignment = self.horizontal_alignment if alignment is None else alignment
        alignment = self.horizontal_alignments[self.horizontal_alignments_short.index(alignment)] if alignment in self.horizontal_alignments_short else alignment
        alignment = self.horizontal_alignments[self.horizontal_alignments_int.index(alignment)] if alignment in self.horizontal_alignments_int else alignment
        return self.horizontal_alignment if alignment not in self.horizontal_alignments else alignment

    def get_horizontal_alignment_index(self, alignment = None):
        alignment = self.correct_horizontal_alignment(alignment)
        return self.horizontal_alignments.index(alignment)

    def correct_vertical_alignment(self, alignment = None):
        alignment = self.vertical_alignment if alignment is None else alignment
        alignment = self.vertical_alignments[self.vertical_alignments_short.index(alignment)] if alignment in self.vertical_alignments_short else alignment
        alignment = self.vertical_alignments[self.vertical_alignments_int.index(alignment)] if alignment in self.vertical_alignments_int else alignment
        return self.vertical_alignment if alignment not in self.vertical_alignments else alignment

    def get_vertical_alignment_index(self, alignment = None):
        alignment = self.correct_vertical_alignment(alignment)
        return self.vertical_alignments.index(alignment)
    
        
placement = placement_class()
