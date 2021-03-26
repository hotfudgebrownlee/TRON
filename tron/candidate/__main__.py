# program entry point
import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService

from game.cycle import Cycle
from game.obstacle import Obstacle
from game.segment import Segment

from game.director import Director
import arcade

def main():
    cast = {}

    cast["cycles"] = []

    cast["obstacles"] = arcade.SpriteList()

    cycle_x = 0

    for i in range(constants.NUM_CYCLES):
        trail = []
        cycle_x += round(constants.MAX_X/(constants.NUM_CYCLES + 1))
        position = Point(cycle_x, constants.CYCLE_Y)
        velocity = Point(0,constants.CYCLE_SPEED)
        if i == 0:
            img = constants.CYCLE_IMAGE
        else:
            img = constants.AI_IMAGE
        cycle = Cycle(position,velocity,img)
        trail.append(cycle)
        light_trail = arcade.SpriteList()
        trail.append(light_trail)
        cast["cycles"].append(trail)

    
        cast["obstacles"].append(cycle)
    
    script = {}
    input_service = InputService()
    output_service = OutputService()

    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handles_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handles_collisions_action]
    script["output"] = [draw_actors_action]

    director = Director(cast,script,input_service)
    director.setup()
    arcade.run()

if __name__ == "__main__":
    main()
