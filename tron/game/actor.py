from game.point import Point
from game import constants
import arcade

class Actor(arcade.Sprite):
    """A class to represent actors."""
    def __init__(self,x,y):
        """Class constructor.

        Args:
            x(coordinate): center_x value
            y(coordinate): center_y value"""
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0

    def get_velocity(self):
        x = self.change_x
        y = self.change_y
        return Point(x,y)
