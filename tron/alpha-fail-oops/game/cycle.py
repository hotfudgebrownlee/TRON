from game import constants
from game.actor import Actor
from game.point import Point
import arcade
class Cycle(Actor):
    """A light cycle, which moves around the screen trying not to
    die. The responsibility of the Cycle is to move and not run
    into any obstacles, other cycles, or its own trail.

    Stereotype:
        Structurer, Information Holder"""
    def __init__(self,position,velocity,image):
        """The class constructor.

        Args:
            self(Cycle): An instance of Cycle."""
        super().__init__(image)
        self.center_x = position.get_x()
        self.center_y = position.get_y()
        self.change_x = velocity.get_x()
        self.change_y = velocity.get_y()