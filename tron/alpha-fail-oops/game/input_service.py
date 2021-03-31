import sys
from game.point import Point
import arcade

class InputService:
    """Detects player input. Communicates key presses which can then be
    translated to movement.

    Stereotype:
        Service Provider

    Attributes:
        _keys(list): up, down, left, right"""
    def __init__(self):
        """Class constructor."""
        self._keys = []

    def set_key(self,key):
        self._keys.append(key)

    def remove_key(self,key):
        self._keys.remove(key)
    
    def get_direction(self):
        """Gets direction for given actor.

        Returns:
            direction(Point): the selected direction."""
        x = 0
        y = 0

        if arcade.key.LEFT in self._keys:
            x = -1
            # direction = Point(0, 1)
            # return direction
        elif arcade.key.RIGHT in self._keys:
            x = 1
            # direction = Point(1, 0)
            # return direction
        
        if arcade.key.UP in self._keys:
            y = 1
            # direction = Point(0, -1)
            # return direction
        elif arcade.key.DOWN in self._keys:
            y = -1
            # direction = Point(-1, 0)
            # return direction

        """Implement logic so cycle doesn't run over self w direction
        switch"""

        direction = Point(x,y)
        return direction