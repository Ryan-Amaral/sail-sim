import numpy as np
from graphics import *

class Sprite:
    
    def __init__(self, points):
        # save shape reference for drawing and built in graphics stuff
        #self.shape = Polygon(points)

        # the position relative to the center
        self.position = np.mean(points, axis=0)
        
        # save the points positions with the centroid moved to the middle
        self.zeroed_points = points - self.position

    def rotate(self, deg):
        pass

    def translate(self, x, y):
        self.position += (x,y)

    def reset_rotation(self):
        pass

    def set_position(self, x, y):
        pass

    def draw(self, window):
        points0 = self.zeroed_points + self.position
        points = [Point(x, y) for (x, y) in points0]
        shape = Polygon(*points)
        shape.draw(window)