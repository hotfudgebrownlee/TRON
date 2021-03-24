from game.point import Point
from game import constants
import arcade

class Actor(arcade.Sprite):
    """A class to represent actors."""
    def __init__(self,image):
        """Class constructor.

        Args:
            image(picture): picture to be passed to Sprite class."""
        super().__init__(image)
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    def get_velocity(self):
        x = self.change_x
        y = self.change_y
        return Point(x,y)

    def get_position(self):
        x = self.center_x
        y = self.center_y
        return Point(x,y)

    def set_position(self, position):
        """Sets a new position.
        
        Args:
            position(Point): new position."""
        self.center_x = position.get_x()
        self.center_y = position.get_y()

    def set_velocity(self, velocity):
        """Sets a new velocity.
        
        Args:
            velocity(Point): new velocity."""
        self.change_x = velocity.get_x()
        self.change_y = velocity.get_y()           