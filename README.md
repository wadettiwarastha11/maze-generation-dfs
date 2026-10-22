# maze-generation-dfs
A Python implementation of maze generation using Depth-First Search (DFS) and backtracking. This Data Structures mini project generates a random maze using a stack and displays the result in the terminal.

# Maze Generation Using DFS

## Project Information
- Subject: Data Structures
- Course: SPPU SE Computer Engineering
- Programming Language: Python
- Algorithm: Depth-First Search (DFS)

## Abstract
This project generates a random maze using the Depth-First
Search algorithm. The maze consists of paths and walls.
DFS explores an unvisited neighboring cell and continues
until no unvisited neighbor remains. It then backtracks
using a stack to explore other possible paths.

The process continues until all cells have been visited.
The generated maze is displayed in the terminal.

## Objectives
- Understand graph traversal using DFS.
- Implement a stack-based algorithm.
- Generate a random maze using backtracking.
- Apply data structures to a practical problem.

## Data Structures Used
- Stack: Tracks the current path through the maze.
- Set: Stores visited cells.
- List: Represents the maze grid.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run the following command:

   python maze_generation_dfs.py

## Algorithm
Depth-First Search (DFS) with backtracking.

## Complexity Analysis
Time Complexity: O(R x C)
Space Complexity: O(R x C)

R represents the number of rows and C represents
the number of columns in the logical grid.

## Applications
- Maze and puzzle generation.
- Game development.
- Pathfinding demonstrations.
- Graph traversal learning.

## Conclusion
This project demonstrates how DFS and backtracking
can be used to generate a maze. It provides practical
understanding of stacks, graph traversal, and visited
nodes in data structures.
