from plotext._string import correct_label
from plotext._matrix import matrix_class
from plotext._system import copy


class bar_lower_class():
    def __init__(self):
        self.clear_labels()
        self.set_width()

    def clear_labels(self):
        self.set_left()
        self.set_center()
        self.set_right()
        self.update_height()
        
    def set_left(self, label = None):
        self.left = None if label is None else correct_label(label)

    def set_center(self, label = None):
        self.center = None if label is None else correct_label(label)

    def set_right(self, label = None):
        self.right = None if label is None else correct_label(label)

    def set_width(self, width = None):
        self.width = int(width) if width is not None else None

    def update_height(self):
        self.height = int([self.left, self.center, self.right] != [None] * 3)
    
    def build(self):
        self.update_height()
        self.matrix = matrix_class(self.width, self.height)
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

    def copy(self):
        return copy(self)

    def backup(self):
        self.left_backup = self.left
        self.center_backup = self.center
        self.right_backup = self.right
        self.width_backup = self.width

    def restore(self):
        self.left = self.left_backup
        self.center = self.center_backup
        self.right = self.right_backup
        self.width = self.width_backup
        

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

    def copy(self):
        return copy(self)

    def backup(self):
        super().backup()
        self.title_backup = self.title
        self.label_backup = self.label
        
    def restore(self):
        super().restore()
        self.title = self.title_backup 
        self.label = self.label_backup 

    


    
