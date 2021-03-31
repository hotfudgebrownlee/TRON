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
        for player in cast["cycles"]:
            trail = player[1]
            count = len(trail)-1
            if count > 15:
                segment = trail[0]
                cast["obstacles"].append(segment)
                trail.remove(segment)
            cycle = player[0]
            if cycle.collides_with_list(cast["obstacles"]):
                sys.exit()