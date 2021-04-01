import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

MAX_X = 800
MAX_Y = 600

NUM_CYCLES = 2
CYCLE_Y = MAX_Y/2
CYCLE_SPEED = 2.5

GAMEOVER = False

CYCLE_IMAGE = DIRROOT.joinpath("assets/player_bike.png")
CYCLE_TRAIL = DIRROOT.joinpath("assets/player_trail.png")
CYCLE_DOWN = DIRROOT.joinpath("assets/player_down.png")
CYCLE_LEFT = DIRROOT.joinpath("assets/player_left.png")
CYCLE_RIGHT = DIRROOT.joinpath("assets/player_right.png")
AI_TRAIL = DIRROOT.joinpath("assets/ai_trail.png")
AI_IMAGE = DIRROOT.joinpath("assets/ai_bike.png")
AI_DOWN = DIRROOT.joinpath("assets/ai_down.png")
AI_LEFT = DIRROOT.joinpath("assets/ai_left.png")
AI_RIGHT = DIRROOT.joinpath("assets/ai_right.png")