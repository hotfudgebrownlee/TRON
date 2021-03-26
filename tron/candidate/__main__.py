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

    """
    for _ in range(constants.NUM_CYCLES):
        cycle_x += round(constants.MAX_X/(constants.NUM_CYCLES + 1))
        position = Point(cycle_x, constants.CYCLE_Y)
        velocity = Point(0,constants.CYCLE_SPEED)
        cycle = Cycle(position,velocity,constants.CYCLE_IMAGE)
        cast["cycles"].append(cycle)

    # Create a list for the light trails.
    trails = arcade.SpriteList()
    cast["trails"] = trails
    
    obstacles = []
    for i in range(constants.NUM_OBST):
        if i % 4 == 0:
            x1 = 0
            x2 = constants.MAX_X / 2
            y1 = constants.MAX_Y / 2
            y2 = constants.MAX_Y
        elif i % 4 == 1:
            x1 = constants.MAX_X / 2
            x2 = constants.MAX_X
            y1 = constants.MAX_Y / 2
            y2 = constants.MAX_Y
        elif i % 4 == 2:
            x1 = constants.MAX_X / 2
            x2 = constants.MAX_X
            y1 = 0
            y2 = constants.MAX_Y / 2
        elif i % 4 == 3:
            x1 = 0
            x2 = constants.MAX_X / 2
            y1 = 0
            y2 = constants.MAX_Y / 2
        x = random.randint(x1 + constants.OBST_WIDTH, x2 - constants.OBST_WIDTH)
        y = random.randint(y1 + constants.OBST_HEIGHT, y2 - constants.OBST_HEIGHT)
        obstacle = Obstacle(x, y)
        for trail in cast["cycles"]:
            cycle = trail[0]
            if not obstacle.collides_with_sprite(cycle):
                obstacles.append(obstacle)
    cast["obstacles"] = obstacles
    """

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
