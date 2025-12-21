Maze Solver Visualizer
An interactive maze and pathfinding visualizer built using Python and Pygame.
This project visually demonstrates how classic search and pathfinding algorithms explore a grid in real time.

It allows users to draw walls, set start and end nodes, and observe how different algorithms behave step by step.

Motivation

Pathfinding algorithms are often taught theoretically, which makes them hard to visualize.
This project was built to bridge that gap by providing a clean, interactive, and visual way to understand how DFS and A star work internally.

Features

Interactive grid based maze editor

Real time algorithm visualization

Depth First Search implementation

A star shortest path algorithm with Manhattan heuristic

Click and drag wall drawing

Start and End node placement

Dark and Light theme toggle

In app help overlay explaining controls and algorithms

Smooth animations for exploration and final path

Clean UI with top control bar

Cross platform support

Algorithms
Depth First Search

Explores one path fully before backtracking

Uses a stack based approach

Does not guarantee the shortest path

Useful for understanding deep exploration behavior

A Star Pathfinding

Uses cost plus heuristic evaluation

Manhattan distance heuristic

Guarantees shortest path when one exists

Efficient and goal directed search

Controls

Left Click and Drag
Draw walls

Right Click and Drag
Erase walls

Set Start
Place the starting node

Set End
Place the destination node

DFS or A star
Select algorithm

Visualize
Run selected algorithm

Theme
Toggle dark and light mode

Help
Open in app instructions

ESC
Close help overlay

Project Structure
maze-solver-visualizer/
│
├── run.py
├── requirements.txt
├── assets/
│   └── start_screen/
│       └── saitama.png
│
├── src/
│   ├── algorithms/
│   │   ├── dfs.py
│   │   └── astar.py
│   │
│   ├── ui/
│   │   ├── topbar.py
│   │   ├── start_screen.py
│   │   ├── help_overlay.py
│   │   └── themes.py
│   │
│   ├── grid.py
│   └── node.py

Installation
Requirements

Python 3.9 or higher

Pygame

Install dependencies

pip install -r requirements.txt

Running the Project
python run.py


The start screen will appear, from where you can launch the visualizer.

Educational Use

This project is suitable for

Computer Science students

Algorithm visualization demos

AI and search algorithm coursework

Teaching DFS and A star intuitively

Future Improvements

Add BFS and Dijkstra

Adjustable animation speed slider

Weighted grids

Diagonal movement option

Save and load mazes

License

This project is open source and free to use for educational purposes.