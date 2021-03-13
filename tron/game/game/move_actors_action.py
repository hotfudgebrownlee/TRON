from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    """Code template for moving actors. The responsibility of this class
    is to move any actor that has a velocity greater than zero.

    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService."""
    def execute(self,cast):
        """Executes the action using the given actors.

        Args:
            cast(dict): The game actors {key:tag, value:list}"""
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)
    
    def _move_actor(self,actor):
        """Moves the given actor to its next position based on velocity.
        Will wrap the position from one side to the other when it reaches
        the edge.
        
        Args:
            actor (Actor): the actor to move."""
        px = actor.center_x
        vx = actor.change_x
        actor.center_x = 1 + (px + vx - 1) % (constants.MAX_X - 1)
        py = actor.center_y
        vy = actor.change_y
        actor.center_y = 1 + (py + vy - 1) % (constants.MAX_Y - 1)