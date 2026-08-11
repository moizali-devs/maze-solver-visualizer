# Maze Solver Visualizer

Interactive pathfinding and algorithm visualization built with Python and Pygame.

## About the Project

Maze Solver Visualizer is an interactive application that visually demonstrates how classical pathfinding algorithms explore a grid environment in real time.

Instead of relying only on theory or pseudocode, this project lets users draw obstacles, place start and end points, and observe how algorithms traverse the maze step by step.

## Features

- Interactive grid-based maze editor
- Real-time pathfinding visualization
- Depth First Search implementation
- A* shortest path algorithm using Manhattan heuristic
- Click and drag wall drawing and erasing
- Start and End node placement
- Dark and light theme toggle
- Built-in help overlay
- Smooth animation and clean navigation bar

## Algorithms Implemented

### Depth First Search

- Explores deeply along one path before backtracking
- Uses a stack-based approach
- Does not guarantee the shortest path
- Useful for understanding deep traversal behavior

### A* Pathfinding

- Uses cost plus heuristic evaluation
- Manhattan distance heuristic
- Guarantees the shortest path when one exists
- More efficient and goal-oriented search

## Controls

| Control | Action |
|---|---|
| Left Click and Drag | Draw walls |
| Right Click and Drag | Erase walls |
| Set Start | Place starting node |
| Set End | Place destination node |
| DFS or A* | Select algorithm |
| Visualize | Run selected algorithm |
| Theme | Toggle dark and light mode |
| Help | Open in-app instructions |
| ESC | Close help overlay |

## Project Structure

```
maze-solver-visualizer/
├── run.py
├── requirements.txt
├── assets/
│   └── start_screen/
│       └── saitama.png
├── src/
│   ├── algorithms/
│   │   ├── dfs.py
│   │   └── astar.py
│   ├── ui/
│   │   ├── topbar.py
│   │   ├── start_screen.py
│   │   ├── help_overlay.py
│   │   └── themes.py
│   ├── grid.py
│   └── node.py
```

## Download

Prebuilt executables for macOS, Windows, and Linux are published on the [Releases](https://github.com/moizali-devs/maze-solver-visualizer/releases/latest) page. No Python installation required.

## Installation (from source)

Requirements:

- Python 3.9 or higher
- Pygame

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python run.py
```

The start screen appears first, from where you can launch the visualizer.

## Building an Executable

```bash
pip install -r requirements-build.txt
pyinstaller run.spec
```

The built app is placed in the `dist/` folder. Cross-platform executables are also built automatically and attached to each [Release](https://github.com/moizali-devs/maze-solver-visualizer/releases) via GitHub Actions.

## Screenshots

**Start Screen**
![Start screen](https://github.com/user-attachments/assets/8905f2ee-ae9e-4925-bda7-b78a18051921)

**DFS Visualization**
![DFS visualization](https://github.com/user-attachments/assets/c3a0fb56-8bac-4934-9f5d-d54113717ad5)

**Help Overlay**
![Help overlay](https://github.com/user-attachments/assets/2fa44f45-486d-4e7b-86f1-9c17ab9525a1)

**A* Visualization**
![A* visualization](https://github.com/user-attachments/assets/1f3278d0-4bc4-4171-bddb-0f2d5b8fb014)

## Educational Use

- Computer Science students
- Algorithm visualization demonstrations
- AI and search algorithm coursework
- Understanding DFS versus heuristic-based search

## License

This project is open source under the [MIT License](LICENSE).
