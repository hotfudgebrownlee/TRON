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
            if count > 8:
                for i in range(count-7):
                    segment = trail[i]
                    if not segment._can_kill:
                        segment.set_kill(True)
                        cast["obstacles"].append(segment)
            cycle = player[0]
            if cycle.collides_with_list(cast["obstacles"]):
                sys.exit()

            # self._handle_obst_collision(trail[0],cast["obstacles"])
            
            # self._handle_self_collision(trail)