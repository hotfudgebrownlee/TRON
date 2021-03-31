import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

MAX_X = 800
MAX_Y = 600

NUM_CYCLES = 2
CYCLE_Y = MAX_Y/2
CYCLE_SPEED = 2.5

CYCLE_IMAGE = DIRROOT.joinpath("assets/player_bike.png")
CYCLE_TRAIL = DIRROOT.joinpath("assets/player_trail.png")
AI_TRAIL = DIRROOT.joinpath("assets/ai_trail.png")
AI_IMAGE = DIRROOT.joinpath("assets/ai_bike.png")