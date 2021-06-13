import numpy as np
from graphics import *

class Sprite:
    
    def __init__(self, points, fill=None, outline=None, width=None):
        
        self.shape = None

        # the position relative to the center
        self.position = np.mean(points, axis=0)
        
        # save the points original positions with the centroid moved to the middle
        self.original_points = points - self.position

        # the points to update, for new rotations
        self.cur_points = np.copy(self.original_points)

        self.fill = fill
        self.outline = outline
        self.width = width


    def rotate(self, rad):
        
        R = np.array(((np.cos(rad), -np.sin(rad)),
                       (np.sin(rad), np.cos(rad))))

        self.cur_points = (R @ self.cur_points.transpose()).transpose()

    def translate(self, x, y):
        self.position += (x,y)

    def reset_rotation(self):
        self.cur_points = np.copy(self.original_points)

    def set_position(self, x, y):
        self.position = (x, y)

    def set_rotation(self, rad):

        R = np.array(((np.cos(rad), -np.sin(rad)),
                       (np.sin(rad), np.cos(rad))))

        self.cur_points = (R @ self.original_points.transpose()).transpose()

    def draw(self, window, fill="def", outline="def", width="def", undraw=True):

        # undraw the old
        if self.shape is not None:
            self.shape.undraw()

        # get points in order and create shape
        points0 = self.cur_points + self.position
        points = [Point(x, y) for (x, y) in points0]
        shape = Polygon(*points)

        # handle coloring and line thickness
        if fill != "def":
            self.fill = fill
        if self.fill is not None:
            shape.setFill(self.fill)

        if outline != "def":
            self.outline = outline
        if self.outline is not None:
            shape.setOutline(self.outline)

        if width != "def":
            self.width = width
        if self.width is not None:
            shape.setWidth(self.width)

        shape.draw(window)

        self.shape = shape