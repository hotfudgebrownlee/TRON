from game import constants
from game.action import Action
from game.point import Point
import random

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
        
        player1 = cast["cycles"][0]
        velocity = player1.get_velocity()
        direction = self._input_service.get_direction().scale(constants.CYCLE_SPEED)
        if self._input_service._keys == []:
        # if direction == Point(0,0):
            direction = velocity        
        player1.set_velocity(direction)

        

        player2 = cast["cycles"][1]
        change = random.randint(0,20)
        if change == 0:
            newdir = Point(constants.CYCLE_SPEED,0)
        elif change == 1:
            newdir = Point(0,constants.CYCLE_SPEED)
        elif change == 2:
            newdir = Point(-constants.CYCLE_SPEED,0)
        elif change == 3:
            newdir = Point(0,-constants.CYCLE_SPEED)
        else:
            newdir = player2.get_velocity()
        player2.set_velocity(newdir)
    
