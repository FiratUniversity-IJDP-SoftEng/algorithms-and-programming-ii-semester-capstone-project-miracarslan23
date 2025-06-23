# Pathfinding Visualization (Console-Based)

This project demonstrates a simple pathfinding visualization using the A* algorithm on a grid, displayed in the console.

## Features
- 10x10 grid representation
- Hardcoded start (S), end (E), and obstacles (#)
- Visualizes the shortest path (*) found by the A* algorithm
- Easy to modify for different grid sizes or obstacle layouts

## Requirements
- Python 3.7 or higher

## Installation
1. Clone this repository or download the files.
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the pathfinding visualization with:
```bash
python pathfinding.py
```

You will see the grid, obstacles, and the path found by the algorithm.

## Customization
- Edit `pathfinding.py` to change the grid size, start/end points, or obstacles.
- You can implement other algorithms (BFS, Dijkstra, etc.) for experimentation.

## Example Output
```
Grid:
S . . . . . . . . .
. . . . . . . . . .
. # # # # # . . . .
. . . . . # . . . .
. . . . . # . . . .
. . . . . # . . . .
. # # # # # . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . E

Finding path...

Path found:
S * * * * * * * * *
. . . . . . . . . *
. # # # # # . . . *
. . . . . # . . . *
. . . . . # . . . *
. . . . . # . . . *
. # # # # # . . . *
. . . . . . . . . *
. . . . . . . . . *
. . . . . . . . . E
``` 