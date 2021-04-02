from game import constants
from game.action import Action
from game.point import Point
from game.segment import Segment
import arcade
import sys

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
        for player in cast["cycles"]:
            cycle = player[0]
            trail = player[1]
            self._move_actor(cycle)
            offset = cycle.get_velocity().reverse()
            img = cycle.get_trail()
            position = cycle.get_position().add(offset)
            segment = Segment(position,img)
            trail.append(segment)
    
    def _move_actor(self,actor):
        """Moves the given actor to its next position based on velocity.
        Will wrap the position from one side to the other when it reaches
        the edge.
        
        Args:
            actor (Actor): the actor to move."""
        velocity = Point(actor.change_x, actor.change_y)
        if velocity.equals(Point(-constants.CYCLE_SPEED,0)): #LEFT
            actor.texture = arcade.load_texture(actor.get_img('lft'))
        elif velocity.equals(Point(constants.CYCLE_SPEED,0)): #RIGHT
            actor.texture = arcade.load_texture(actor.get_img('rgt'))
        elif velocity.equals(Point(0,constants.CYCLE_SPEED)): #UP
            actor.texture = arcade.load_texture(actor.get_img('fwd'))
        elif velocity.equals(Point(0,-constants.CYCLE_SPEED)): #DOWN
            actor.texture = arcade.load_texture(actor.get_img('bck'))
        x = 1 + (actor.center_x + actor.change_x - 1) % (constants.MAX_X - 1)
        y = 1 + (actor.center_y + actor.change_y - 1) % (constants.MAX_Y - 1)
        position = Point(x,y)
        actor.set_position(position)
