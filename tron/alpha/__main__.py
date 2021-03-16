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
# from game.trail import Trail

from game.director import Director
import arcade

def main():
    cast = {}

    cast["cycles"] = []

    cycle_x = 0
    for _ in range(constants.NUM_CYCLES):
        cycle_x += round(constants.MAX_X/(constants.NUM_CYCLES + 1))
        cycle = Cycle(cycle_x, constants.CYCLE_Y, constants.CYCLE_IMAGE)
        cast["cycles"].append(cycle)
        """
        TRAIL LOGIC

        """
    cast["obstacles"] = []
    while len(cast["obstacles"]) <= constants.NUM_OBST:
        x = random.randint(0 + constants.OBST_WIDTH
                    ,constants.MAX_X - constants.OBST_WIDTH)
        y = random.randint(0 + constants.OBST_HEIGHT
                    ,constants.MAX_Y - constants.OBST_HEIGHT)
        obstacle = Obstacle(x, y)
        for cycle in cast["cycles"]:
            if not obstacle.collides_with_sprite(cycle):
                if cast["obstacles"]:
                    for other in cast["obstacles"]:
                        if not obstacle.collides_with_sprite(other):
                            cast["obstacles"].append(obstacle)
                else:
                    cast["obstacles"].append(obstacle)
    
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
