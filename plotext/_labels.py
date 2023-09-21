class labels_class():
    def __init__(self):
        self.set_left_label()
        self.set_center_label()
        self.set_right_label()

# Label  Functions 

    def set_left_label(self, label = None):
        self.left_label = self.correct_label(label)
        self.show_left_label = self.left_label is not None

    def set_center_label(self, label = None):
        self.center_label = self.correct_label(label)
        self.show_center_label = self.center_label is not None

    def set_right_label(self, label = None):
        self.right_label = self.correct_label(label)
        self.show_right_label = self.right_label is not None

    def update_show_label(self):
        self.show_label = self.show_left_label or self.show_center_label or self.show_right_label

    def correct_label(self, label = None): 
        label = None if label is None else str(label).strip()
        spaces = only_spaces(label)
        label = None if spaces else label 
        return label
