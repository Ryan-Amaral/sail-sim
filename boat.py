from sprite import Sprite
from math import sqrt

class Boat:

    def __init__(self, points=None, fill=None, outline=None, width=None):
        # status relative to boat
        self.sail_angle = 0
        self.rudder_angle = 0
        self.heading = 0
        self.speed = 0
        # current position
        self.x = 0
        self.y = 0

        # constants
        self.sail_min = -1
        self.sail_max = 1
        self.rudder_min = -1
        self.rudder_max = 1
        self.max_speed = 2 # meters per second

        # waypoints
        self.waypoints = []
        self.waypoint_idx = 0
        # radius for boat to get within to count as hitting waypoint
        self.wp_radius = 5
        # position of next waypoint
        self.wp_x = self.waypoints[0][0]
        self.wp_y = self.waypoints[0][1]

        # final goal position
        self.final_x = self.waypoints[-1][0]
        self.final_y = self.waypoints[-1][1]

        # for rendering
        if points is not None:
            self.sprite = Sprite(points, fill, outline, width)
        else:
            self.sprite = None

        # turns true when reached final waypoint
        self.finished = False

    """
    Rotate the sail a number of radians.
    """
    def rotate_sail(self, rad):
        self.sail_angle = max(min(self.sail_angle + rad, self.sail_max), self.sail_min)

    """
    Rotate the rudder a number of radians.
    """
    def rotate_rudder(self, rad):
        self.rudder_angle = max(min(self.rudder_angle + rad, self.rudder_max), self.rudder_min)

    """
    Set the sail to the given radian relative to origin.
    """
    def set_sail(self, rad):
        self.sail_angle = max(min(rad, self.sail_max), self.sail_min)

    """
    Set the rudder to the given radian relative to origin.
    """
    def set_rudder(self, rad):
        self.rudder_angle = max(min(rad, self.rudder_max), self.rudder_min)

    """
    Ignore any actual physical constraints, just move to target.
    """
    def update_position_dummy(self):

        # first move towards waypoint

        wp_dist_x = self.wp_x - self.x
        wp_dist_y = self.wp_y - self.y

        wp_dist = sqrt(wp_dist_x^2 + wp_dist_y^2)

        wp_dir_x = wp_dist_x/wp_dist
        wp_dir_y = wp_dist_y/wp_dist

        self.x += wp_dir_x * self.max_speed
        self.y += wp_dir_y * self.max_speed

        # check if in or past current waypoint
        wp_dist_x = self.wp_x - self.x
        wp_dist_y = self.wp_y - self.y

        wp_dist_2 = sqrt(wp_dist_x^2 + wp_dist_y^2)

        # update waypoint if needed
        if wp_dist < self.wp_radius:
            self.waypoint_idx += 1
            if self.waypoint_idx == len(self.waypoints):
                self.finished = True
                return
            self.wp_x = self.waypoints[self.waypoint_idx][0]
            self.wp_y = self.waypoints[self.waypoint_idx][1]

    """
    Actuates the boat based on the given inputs, and updates its position.
    Has the option to take sensor and actuator noise into account.
    """
    def update_position(self):

        # find target heading

        # find ideal rudder angle

        # find ideal sail angle

        # actuates rudders based on PID or other algorithm
        # or directly moves it to target if long term test

        # switch to next waypoint if needed

        pass

    """
    If running visual example, render the boat probably after each update position.
    """
    def render(self, window, fill="def", outline="def", width="def", undraw=True):
        self.sprite.set_position(self.x, self.y)
        self.sprite.set_rotation(self.heading)
        self.sprite.draw(window, fill, outline, width, undraw)