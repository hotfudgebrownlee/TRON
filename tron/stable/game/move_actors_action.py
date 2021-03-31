from game import constants
from game.action import Action
from game.point import Point
from game.segment import Segment

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
        for player in cast["cycles"]:
            cycle = player[0]
            trail = player[1]
            self._rotate_img(cycle)
            self._move_actor(cycle)
            offset = cycle.get_velocity().reverse()
            img = cycle.get_trail()
            position = cycle.get_position().add(offset)
            segment = Segment(position,img)
            trail.append(segment)
    
    def _move_actor(self,actor):
        """Moves the given actor to its next position based on velocity.
        Will wrap the position from one side to the other when it reaches
        the edge.
        
        Args:
            actor (Actor): the actor to move."""
        x = 1 + (actor.center_x + actor.change_x - 1) % (constants.MAX_X - 1)
        y = 1 + (actor.center_y + actor.change_y - 1) % (constants.MAX_Y - 1)
        position = Point(x,y)
        # if position.equals(Point(-1,0)): #LEFT
        #     pass
        # elif position.equals(Point(1,0)): #RIGHT
        #     pass
        # elif position.equals(Point(0,1)): #UP
        #     pass
        # elif position.equals(Point(0,-1)): #DOWN
        #     pass
        actor.set_position(position)
