import sys
from game import constants
import arcade

class OutputService:
    """Outputs game state. Draws game state in window.

    Stereotype:
        Service Provider

    Attributes:
        _screen (Screen): an arcade screen."""
    def clear_screen(self):
        """Clear the screen."""
        arcade.start_render()

    def draw_actor(self,actor):
        """Rendor the actor's image on-screen.

        Args:
            actor (Actor): The actor to render."""
        actor.draw()

    def draw_actors(self,actors):
        """Draw multiple actors.
        
        Args:
            actors (list): multiple actors to be rendered."""
        for actor in actors:
            self.draw_actor(actor)
