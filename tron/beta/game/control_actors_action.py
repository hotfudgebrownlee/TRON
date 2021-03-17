from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """Code template for controlling actors. Translates user input
    into some sort of movement or event on-screen.

    Stereotype:
        Controller

    Attributes:
        _input_service(InputService): An instance of InputService."""
    def __init__(self,input_service):
        """Class constructor.

        Args:
            input_service(InputService): an instance of InputService."""
        self._input_service = input_service
    
    def execute(self,cast):
        """Executes the action using given actors.

        Args:
            cast(dict): The game actors {key:tag,value:list}"""
        direction = self._input_service.get_direction().scale(constants.CYCLE_SPEED)
        trail = cast["cycles"][0]
        cycle = trail[0]
        cycle.set_velocity(direction)

