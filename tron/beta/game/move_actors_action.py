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
        for trail in cast["cycles"]:
            # for segment in trail:
            #     if not segment.get_velocity().is_zero():
            #         self._move_actor(segment)
            count = len(trail) - 1
            for n in range(count, -1, -1):
                segment = trail[n]
                if n > 0:
                    leader = trail[n - 1]
                    velocity = leader.get_velocity()
                    segment.set_velocity(velocity)
                else:
                    direction = segment.get_velocity()
                    segment.set_velocity(direction)
                self._move_actor(segment)
    
    def _move_actor(self,actor):
        """Moves the given actor to its next position based on velocity.
        Will wrap the position from one side to the other when it reaches
        the edge.
        
        Args:
            actor (Actor): the actor to move."""
        x = 1 + (actor.center_x + actor.change_x - 1) % (constants.MAX_X - 1)
        y = 1 + (actor.center_y + actor.change_y - 1) % (constants.MAX_Y - 1)
        position = Point(x,y)
        actor.set_position(position)