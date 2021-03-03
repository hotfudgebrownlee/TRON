# TRON
Tron is a program where there are two light cycles that chase
each other around the screen. The goal of each player is to cut
the other off with the light trail behind his or her light cycle.
If a player runs into any light trail (their own or their enemy's)
the player dies.

This program runs using Python 3.8.0 or higher and arcade 2.1.0.

WISH LIST:
  - Main Scene:
    - Play Button
    -Help Button
  - Game Scene:
    - User-controlled P1
    - AI-controlled P2
    - Multicolored cycles
    - Life display (3 each)
    - Various levels of AI intelligence
    - Collision detection
    - Sound effects
    - Music
    - Players can go through walls
  - Help Scene:
    - Instructions
    - Back button
  - Life Lost Scene:
    - Player x lost a life
    - Next round button
    - Optional Quit button
  - End Scene:
    - Player x won
    - Play again button
    - Quit button



FEATURE LIST (priorities):
  1. Moving Bikes (control) and trails
  2. Basic AI for P2
  3. Collision detection
  4. Multiple lives feature
  5. Move through walls
  6. Design/colors/cool light trails
  7. Win/loss display screens
  8. Sounds
  9. Button layout

  Priority 1 is top priority, 2 is mid-level, 3 is late priority

  - (2)Main Scene:
    - (2)-Play Button
    - (3)-Help Button
  - (1)Game Scene:
    - (1)-User-controlled P1
    - (1)-AI-controlled P2
    - (3)-Multicolored cycles
    - (2)-Life display - (3 each)
    - (3)-Various levels of AI intelligence
    - (1)-Collision detection
    - (3)-Sound effects
    - (3)-Music
    - (2)-Players can go through walls
  - (3)Help Scene:
    - (3)-Instructions
    - (3)-Back button
  - (2)Life Lost Scene:
    - (2)-Player x lost a life
    - (2)-Next round button
    - (3)-Optional Quit button
  - (2)End Scene:
    - (2)-Player x won
    - (3)-Play again button
    - (3)-Quit button


This project will be completed over the course of four weeks.
We will release an Alpha, Beta, working, and final copy of the game.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and arcade 2.1.0 or new installed 
and running on your machine. You can install arcade by opening a terminal 
and running the following command.
```
python3 -m pip install arcade
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.
```
python3 TRON 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the batter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- TRON              (source code for game)
  +-- game              (specific game classes)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Arcade 2.1.0

## Authors
---
* Jaren Brownlee- bro15108@byui.edu
* Christian Martinez- mar19036@byui.edu
* Dustin Trinh- tri15001@byui.edu
* Michael Fisher- fis17005@byui.edu