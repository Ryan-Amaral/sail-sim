from sprite import Sprite

class Boat:

    def __init__(self, points=None, fill=None, outline=None, width=None):
        # status relative to boat
        self.sail_angle = 0
        self.rudder_angle = 0
        self.heading = 0
        self.speed = 0

        # constants
        self.sail_min = -1
        self.sail_max = 1
        self.rudder_min = -1
        self.rudder_max = 1
        self.max_speed = 2 # meters per second
        
        # global reference frame
        # current position
        self.x = 0
        self.y = 0
        # final goal position
        self.final_x = 0
        self.final_y = 0
        # position of next waypoint
        self.wp_x = 0
        self.wp_y = 0

        self.waypoints = []
        self.waypoint_idx = 0

        # for rendering
        if points is not None:
            self.sprite = Sprite(points, fill, outline, width)
        else:
            self.sprite = None

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
        pass

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