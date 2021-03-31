from game.action import Action
from game import constants
import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.

    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService."""
    def __init__(self,output_service):
        """Class constructor.

        Args:
            _output_service(OutputService): an instance of OutputService."""
        self._output_service = output_service

    def execute(self,cast):
        """Executes the action using given actors.

        Args:
            cast(dict): the game actors {key:tag, value:list}"""
        self._output_service.clear_screen()
        
        for cycle in cast["cycles"]:
            self._output_service.draw_actor(cycle[0])
            self._output_service.draw_actor(cycle[1])

        self._output_service.draw_actor(cast["obstacles"])