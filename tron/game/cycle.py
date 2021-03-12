from game import constants
from game.actor import Actor
from game.point import Point
import arcade
class Cycle(Actor):
    """A light cycle, which moves around the screen trying not to
    die. The responsibility of the Cycle is to move and not run
    into any obstacles, other cycles, or its own trail.

    Stereotype:
        Structurer, Information Holder, 

    Attributes:
        _trail_bits (list): The trail behind the cycle
            (a list of Actor instances)"""
    def __init__(self,x,y):
        """The class constructor.

        Args:
            self(Cycle): An instance of Cycle."""
        self.center_x = x
        self.center_y = y
        self._trail_bits = []
        self._prepare_trail()

    def _prepare_trail(self):
        """Prepares the trail to follow behind the cycle.

        Args:
            self(Cycle): an instance of Cycle."""
        x = self.center_x
        y = self.center_y
        velocity = Point(0,0)
        position = Point(x,y)
        self._add_trail_bit(position,velocity,constants.CYCLE_IMAGE)
        for k in range(1,constants.TRAIL_LENGTH + 1):
            if k == 1:
                n = constants.CYCLE_IMG_SCALE
            else:
                n = constants.TRAIL_IMG_SCALE
            position = Point(x,y-(k*n))
            self._add_trail_bit(position,velocity,constants.TRAIL_IMAGE)

    def _add_trail_bit(self,position,velocity,image):
        """Adds a new bit to the end of the trail.

        Args:
            self(Cycle): an instance of Cycle.
            position (Point): The bit's position.
            velocity (Point): The bit's velocity."""
        bit = Actor(image)
        bit.set_position(position)
        bit.set_velocity(velocity)
        self._trail_bits.append(bit)

    def move_cycle(self,direction):
        """Moves the cycle in a given direction.

        Args:
            self(Cycle): An instance of Cycle.
            direction(Point): the direction to move."""
        count = len(self._trail_bits) - 1

        for n in range(count, -1, -1):
            bit = self._trail_bits[n]
            if n > 0:
                leader = self._trail_bits[n-1]
                velocity = leader.get_velocity()
                segment = set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            segment.move_next()