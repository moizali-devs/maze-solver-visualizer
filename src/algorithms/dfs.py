import pygame                                      # For small delays
from src.node import WALL, VISITED, PATH          # Use state names from Node


def get_neighbors(grid, node):
    """Return valid neighbor nodes (up, down, left, right)."""
    neighbors = []                                 # List to store neighbor cells

    rows = len(grid)                               # Number of rows in grid
    cols = len(grid[0])                            # Number of columns

    r = node.row                                   # Current node row
    c = node.col                                   # Current node column

    # Up
    if r > 0:
        neighbors.append(grid[r - 1][c])           # Cell above

    # Down
    if r < rows - 1:
        neighbors.append(grid[r + 1][c])           # Cell below

    # Left
    if c > 0:
        neighbors.append(grid[r][c - 1])           # Cell to the left

    # Right
    if c < cols - 1:
        neighbors.append(grid[r][c + 1])           # Cell to the right

    return neighbors                               # Return all valid neighbors


def reconstruct_path(came_from, current, draw):
    """Walk backward from end node to start node and mark the path."""
    while current in came_from:                    # While there is a parent stored
        current = came_from[current]              # Move to the parent node
        current.make_path()                       # Mark this cell as part of the path
        draw()                                    # Redraw the screen
        pygame.time.delay(20)                     # Small delay so we can see the path


def dfs(draw, grid, start, end):
    """
    Depth-First Search visualization.
    draw: function that redraws the screen.
    grid: 2D list of Node objects.
    start: start Node.
    end: end Node.
    """

    stack = [start]                               # Use a stack for DFS (LIFO)
    visited = set()                               # Keep track of visited nodes
    came_from = {}                                # Map child node -> parent node

    while stack:                                  # While there are nodes to explore
        current = stack.pop()                     # Get the last node added (DFS behavior)

        if current in visited:                    # If we already visited this node
            continue                              # Skip it

        visited.add(current)                      # Mark node as visited in memory

        if current is not start and current is not end:
            current.make_visited()                # Color this node as visited

        if current == end:                        # If we reached the goal
            reconstruct_path(came_from, end, draw) # Draw the final path
            return True                           # DFS succeeded

        for neighbor in get_neighbors(grid, current):  # Check each neighbor
            if neighbor.state == WALL:                # Ignore walls
                continue

            if neighbor not in visited:               # Only visit not-yet-visited cells
                stack.append(neighbor)                # Add neighbor to stack
                came_from[neighbor] = current         # Remember how we got to neighbor

        draw()                                        # Redraw grid with updates
        pygame.time.delay(10)                        # Small delay for animation

    return False                                      # No path found
