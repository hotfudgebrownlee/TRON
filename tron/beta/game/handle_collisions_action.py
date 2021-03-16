import random
from game import constants
from game.action import Action
import sys

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for cycle in cast["cycles"]:
            self._handle_obst_collision(cycle,cast["obstacles"])
    
    def _handle_obst_collision(self, cycle, obstacles):
        for obstacle in obstacles:
            if cycle.collides_with_sprite(obstacle):
                sys.exit()