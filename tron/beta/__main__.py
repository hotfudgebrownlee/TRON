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

    cycle_x = 0
    for _ in range(constants.NUM_CYCLES):
        trail = []
        cycle_x += round(constants.MAX_X/(constants.NUM_CYCLES + 1))
        position = Point(cycle_x, constants.CYCLE_Y)
        velocity = Point(0,constants.CYCLE_SPEED)
        cycle = Cycle(position,velocity,constants.CYCLE_IMAGE)
        trail.append(cycle)
        for j in range(1,constants.TRAIL_LENGTH + 1):
            if j == 1:
                k = constants.CYCLE_IMG_SCALE
            else:
                k = constants.TRAIL_IMG_SCALE
            position = Point(cycle_x,constants.CYCLE_Y-(j*k))
            velocity = cycle.get_velocity()
            segment = Segment(position,velocity,constants.TRAIL_IMAGE)
            trail.append(segment)
        cast["cycles"].append(trail)

    obstacles = []
    while len(obstacles) <= constants.NUM_OBST:
        x = random.randint(0 + constants.OBST_WIDTH
                    ,constants.MAX_X - constants.OBST_WIDTH)
        y = random.randint(0 + constants.OBST_HEIGHT
                    ,constants.MAX_Y - constants.OBST_HEIGHT)
        obstacle = Obstacle(x, y)
        for trail in cast["cycles"]:
            cycle = trail[0]
            if not obstacle.collides_with_sprite(cycle):
                if obstacles:
                    for other in obstacles:
                        if not obstacle.collides_with_sprite(other):
                            obstacles.append(obstacle)
                else:
                    obstacles.append(obstacle)
    cast["obstacles"] = obstacles
    
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
