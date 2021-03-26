import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

MAX_X = 800
MAX_Y = 600

NUM_CYCLES = 2
CYCLE_Y = MAX_Y/2
CYCLE_SPEED = 2.5

CYCLE_IMAGE = DIRROOT.joinpath("assets/blue_sq.png")
TRAIL_IMAGE = DIRROOT.joinpath("assets/white_sq.png")
AI_IMAGE = DIRROOT.joinpath("assets/red_sq.png")