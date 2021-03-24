import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

MAX_X = 800
MAX_Y = 600

NUM_CYCLES = 2
CYCLE_Y = MAX_Y/2
CYCLE_MOVE_SCALE = 5
CYCLE_SPEED = 1.5

NUM_OBST = 4
OBST_WIDTH = 25
OBST_HEIGHT = 25
OBST_SPACE = 10

CYCLE_IMAGE = DIRROOT.joinpath("assets/blue_sq.png")
TRAIL_IMAGE = DIRROOT.joinpath("assets/white_sq.png")
OBSTACLE_IMAGE = DIRROOT.joinpath("assets/red_sq.png")

CYCLE_IMG_SCALE = 64
TRAIL_IMG_SCALE = 3