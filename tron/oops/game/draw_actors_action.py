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
        for obstacle in cast["obstacles"]:
            self._output_service.draw_actor(obstacle)
        for trail in cast["cycles"]:
            for segment in trail:
                self._output_service.draw_actor(segment)
            """
        for trail in cast["trails"]:
            for trail_bit in trail:
                self._output_service.draw_actor(trail_bit)
                """