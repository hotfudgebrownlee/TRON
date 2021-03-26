from game import constants
from game.actor import Actor
from game.point import Point
import arcade
class Segment(Actor):
    """A segment of the trail that follows the light cycle.

    Stereotype:
        Structurer, Information Holder"""
    def __init__(self,position,image):
        """The class constructor.

        Args:
            self(Segment): An instance of Segment."""
        super().__init__(image)
        self.center_x = position.get_x()
        self.center_y = position.get_y()
        self._can_kill = False

    def update_animation(self, image):
        """Updates the image."""
        self.image = image

    def set_kill(self,kill):
        self._can_kill = kill