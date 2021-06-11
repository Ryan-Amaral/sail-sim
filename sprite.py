class Sprite:
    
    def __init__(self, shape, points=None):
        self.shape = shape
        if points is not None:
            self.original_points = points
            self.is_poly = True
        else:
            self.original_points = None
            self.is_poly = False

    def rotate(self, deg):
        pass

    def translate(self, x, y):
        pass

    def reset_rotation(self):
        pass

    def set_positin(self, x, y):
        pass