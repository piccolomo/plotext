from plotext._string import correct_label
from plotext._matrix import matrix_class

class bar_lower_class():
    def __init__(self):
        self.set_left()
        self.set_center()
        self.set_right()

        self.set_width()
        self.set_height(1)

    def set_left(self, label = None):
        self.left = None if label is None else correct_label(label)

    def set_center(self, label = None):
        self.center = None if label is None else correct_label(label)

    def set_right(self, label = None):
        self.right = None if label is None else correct_label(label)

    def set_width(self, width = None):
        self.width = int(width) if width is not None else None

    def set_height(self, height = None):
        self.height = int(bool(height)) if height is not None else None

    def get_height(self):
        return int(self.height and [self.left, self.center, self.right] != [None] * 3)
    
    def build(self):
        self.matrix = matrix_class(self.width, self.get_height())
        self.insert_left()
        self.insert_center()
        self.insert_right()

    def insert_left(self):
        just_do_it = self.height == 1 and self.left is not None and len(self.left) <= self.width
        self.matrix.insert_horizontal_string(0, 0, self.left, 'left', overwrite = False) if just_do_it else None
        
    def insert_center(self):
        just_do_it = self.height == 1 and self.center is not None and len(self.center) <= self.width
        self.matrix.insert_horizontal_string(0, self.width // 2, self.center, 'center', overwrite = False) if just_do_it else None

    def insert_right(self):
        just_do_it = self.height == 1 and self.right is not None and len(self.right) <= self.width
        self.matrix.insert_horizontal_string(0, self.width, self.right, 'right', overwrite = False) if just_do_it else None
        
    def clear(self):
        self.__init__()
        

class bar_upper_class(bar_lower_class):
    def __init__(self):
        super().__init__()
        self.set_label()
        self.set_title()

    def set_title(self, label = None):
        self.title = None if label is None else correct_label(label)

    def set_label(self, label = None):
        self.label = None if label is None else correct_label(label)

    def update_labels(self):
        self.set_center(self.label)
        self.set_center(self.title) if self.label is None else self.set_left(self.title)

    def build(self):
        self.update_labels()
        super().build()
    


    
