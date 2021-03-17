from game.point import Point
from game import constants
from game.actor import Actor
import arcade

class Obstacle(Actor):
    def __init__(self, x, y):
        super().__init__(constants.OBSTACLE_IMAGE)

        self.center_x = x
        self.center_y = y