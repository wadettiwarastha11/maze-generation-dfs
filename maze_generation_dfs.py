
import random

ROWS = 10
COLS = 10

# Directions: row change, column change
DIRECTIONS = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]


def generate_maze(rows, cols):
    # All cells initially contain walls
    maze = [['#' for _ in range(2 * cols + 1)]
            for _ in range(2 * rows + 1)]

    visited = set()
    stack = [(0, 0)]
    visited.add((0, 0))

    maze[1][1] = ' '

    while stack:
        r, c = stack[-1]
        neighbors = []

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited):
                neighbors.append((nr, nc, dr, dc))

        if neighbors:
            nr, nc, dr, dc = random.choice(neighbors)

            # Remove wall between current and next cell
            maze[2 * r + 1 + dr][2 * c + 1 + dc] = ' '
            maze[2 * nr + 1][2 * nc + 1] = ' '

            visited.add((nr, nc))
            stack.append((nr, nc))
        else:
            # Backtrack when no unvisited neighbor exists
            stack.pop()

    # Mark start and destination
    maze[1][1] = 'S'
    maze[2 * rows - 1][2 * cols - 1] = 'E'

    return maze


def display_maze(maze):
    for row in maze:
        print(''.join(row))


if __name__ == "__main__":
    print("MAZE GENERATION USING DFS")
    print("-------------------------")

    maze = generate_maze(ROWS, COLS)
    display_maze(maze)
    print("\nS = Start | E = End | # = Wall")
