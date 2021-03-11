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

    def get_velocity(self):
        x = self.change_x
        y = self.change_y
        return Point(x,y)
