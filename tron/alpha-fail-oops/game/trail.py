from game import constants
from game.actor import Actor
from game.point import Point
class Trail:
    def __init__(self):
        self._trails = []
        self._prepare_trail()
    def get_trails(self):
        return self._segments
    def get_trail(self):
        return self._segments[1]
    def move_trail(self, direction):
        count = len(self._trails) - 1
        for n in range(count,-1,-1):
            trail = self._trails[n]
            if n > 0:
                cycle = self._segments[n-1]
                velocity = cycle.get_velocity()
                trail.set_velocity(velocity)
            else:
                trail.set_velocity(direction)
    def _add_trail(self, image, position, velocity):
        trail = Actor(image)
        trail.set_position(position)
        trail.set_velocity(velocity)
        self._trails.append(trail)
    def _prepare_trail(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        for n in range(20):
            image = constants.CYCLE_IMAGE if n == 0 else constants.TRAIL_IMAGE
            position = Point(x - n, y)
            velocity = Point(1, 0)
            self._add_trail(image, position, velocity)