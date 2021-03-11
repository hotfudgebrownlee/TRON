import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

MAX_X = 800
MAX_Y = 500

NUM_CYCLES = 1
CYCLE_Y = MAX_Y/2
CYCLE_MOVE_SCALE = 5

NUM_OBST = 4
OBST_WIDTH = 25
OBST_HEIGHT = 25
OBST_SPACE = 10

"""
CYCLE_1_IMAGE = DIRROOT.joinpath("images/.png")
CYCLE_2_IMAGE = DIRROOT.joinpath("images/.png")
OBSTACLE_IMAGE = DIRROOT.joinpath("images/.png")
TRAIL_1_IMAGE = DIRROOT.joinpath("images/.png")
TRAIL_2_IMAGE = DIRROOT.joinpath("images/.png")
"""
