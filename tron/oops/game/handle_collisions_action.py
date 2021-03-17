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
        for trail in cast["cycles"]:
            self._handle_obst_collision(trail[0],cast["obstacles"])
            # self._handle_self_collision(trail)
            # for other in cast["cycles"]:
            #     if not other == trail:
            #         self._handle_other_collision(trail,other)
    
    def _handle_obst_collision(self, cycle, obstacles):
        for obstacle in obstacles:
            if cycle.collides_with_sprite(obstacle):
                sys.exit()

    def _handle_self_collision(self,trail):
        cycle = trail[0]
        for segment in range(1,len(trail),1):
            if cycle.collides_with_sprite(segment):
                sys.exit()
    
    def _handle_other_collision(self,trail,other):
        cycle = trail[0]
        for segment in trail:
            if cycle.collides_with_sprite(segment):
                sys.exit()