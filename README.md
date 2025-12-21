<h1 align="center">Maze Solver Visualizer</h1>

<p align="center">
  <strong>Interactive Pathfinding and Algorithm Visualization</strong><br>
  <em>Built using Python and Pygame</em>
</p>

<p align="center">
  Algorithms · Visualization · Interactive Grid · Clean UI
</p>

<hr>

<h2>About the Project</h2>

<p>
Maze Solver Visualizer is an interactive application designed to visually demonstrate how classical
pathfinding algorithms explore a grid environment in real time.
</p>

<p>
Instead of relying only on theory or pseudocode, this project allows users to draw obstacles,
place start and end points, and observe how algorithms traverse the maze step by step.
</p>

<hr>

<h2>Features</h2>

<ul>
  <li>Interactive grid based maze editor</li>
  <li>Real time pathfinding visualization</li>
  <li>Depth First Search implementation</li>
  <li>A star shortest path algorithm using Manhattan heuristic</li>
  <li>Click and drag wall drawing and erasing</li>
  <li>Start and End node placement</li>
  <li>Dark and Light theme toggle</li>
  <li>Built in help overlay</li>
  <li>Smooth animation and clean navigation bar</li>
</ul>

<hr>

<h2>Algorithms Implemented</h2>

<h3>Depth First Search</h3>

<ul>
  <li>Explores deeply along one path before backtracking</li>
  <li>Uses a stack based approach</li>
  <li>Does not guarantee the shortest path</li>
  <li>Useful for understanding deep traversal behavior</li>
</ul>

<h3>A Star Pathfinding</h3>

<ul>
  <li>Uses cost plus heuristic evaluation</li>
  <li>Manhattan distance heuristic</li>
  <li>Guarantees the shortest path when one exists</li>
  <li>More efficient and goal oriented search</li>
</ul>

<hr>

<h2>Controls</h2>

<ul>
  <li><strong>Left Click and Drag</strong> Draw walls</li>
  <li><strong>Right Click and Drag</strong> Erase walls</li>
  <li><strong>Set Start</strong> Place starting node</li>
  <li><strong>Set End</strong> Place destination node</li>
  <li><strong>DFS or A star</strong> Select algorithm</li>
  <li><strong>Visualize</strong> Run selected algorithm</li>
  <li><strong>Theme</strong> Toggle dark and light mode</li>
  <li><strong>Help</strong> Open in app instructions</li>
  <li><strong>ESC</strong> Close help overlay</li>
</ul>

<hr>

<h2>Project Structure</h2>

<pre>
maze-solver-visualizer/
│
├── run.py
├── requirements.txt
│
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
</pre>

<hr>

<h2>Installation</h2>

<p><strong>Requirements</strong></p>

<ul>
  <li>Python 3.9 or higher</li>
  <li>Pygame</li>
</ul>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>Running the Application</h2>

<pre>
python run.py
</pre>

<p>
The start screen will appear first, from where you can launch the visualizer.
</p>

<hr>

<h2>Screenshots</h2>

<p>
You may add screenshots to enhance GitHub presentation.
</p>

<pre>
screenshots/
├── start_screen.png
  <img width="900" height="400" alt="image" src="https://github.com/user-attachments/assets/8905f2ee-ae9e-4925-bda7-b78a18051921" />

├── dfs_visualization.png
  <img width="900" height="400" alt="image" src="https://github.com/user-attachments/assets/c3a0fb56-8bac-4934-9f5d-d54113717ad5" />

├── help_overlay.png
  <img width="900" height="400" alt="image" src="https://github.com/user-attachments/assets/2fa44f45-486d-4e7b-86f1-9c17ab9525a1" />

└── astar_visualization.png├──
  <img width="900" height="400" alt="image" src="https://github.com/user-attachments/assets/1f3278d0-4bc4-4171-bddb-0f2d5b8fb014" />

  

</pre>
<hr>

<h2>Educational Use</h2>

<ul>
  <li>Computer Science students</li>
  <li>Algorithm visualization demonstrations</li>
  <li>AI and search algorithm coursework</li>
  <li>Understanding DFS versus heuristic based search</li>
</ul>

<hr>

<h2>License</h2>

<p>
This project is open source and intended for educational and learning purposes.
</p>
