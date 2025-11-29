import pygame                                      # For small animation delays
from heapq import heappush, heappop               # Priority queue for A* open set
from src.node import WALL, VISITED, PATH, START, END  # State names for clarity


def get_neighbors(grid, node):
    """Return valid neighbor nodes (up, down, left, right)."""
    neighbors = []                                 # List of neighbor cells

    rows = len(grid)                               # Total rows
    cols = len(grid[0])                            # Total columns

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


def heuristic(a, b):
    """Manhattan distance between two nodes a and b."""
    return abs(a.row - b.row) + abs(a.col - b.col) # |Δrow| + |Δcol|


def reconstruct_path(came_from, current, draw):
    """Walk backward from end node to start node and mark the final path."""
    while current in came_from:                    # While we have a parent stored
        current = came_from[current]               # Move to the parent node
        if current.state not in (START, END):      # Don't override start or end
            current.state = PATH                   # Mark as part of the final path
        draw()                                     # Redraw the screen
        pygame.time.delay(20)                      # Small delay so we see the path build


def astar(draw, grid, start, end):
    """
    A* pathfinding visualization.
    draw: function that redraws the screen.
    grid: 2D list of Node objects.
    start: start Node.
    end: end Node.
    """

    # Priority queue for open set: (f_score, tie_breaker, node)
    open_set = []                                  # List that will act as a heap
    count = 0                                      # Tie-breaker to avoid comparing nodes

    # Push the start node into the open set with f_score 0
    heappush(open_set, (0, count, start))          # (priority, order, node)

    came_from = {}                                 # child node -> parent node
    g_score = {start: 0}                           # Cost from start to this node
    f_score = {start: heuristic(start, end)}       # Estimated total cost (g + h)

    open_set_hash = {start}                        # Quick membership check for open set
    visited = set()                                # Closed set of fully processed nodes

    while open_set:                                # While there are nodes to explore
        _, _, current = heappop(open_set)          # Get node with lowest f_score
        open_set_hash.remove(current)              # Remove it from the open set hash

        if current in visited:                     # If we already processed this node
            continue                               # Skip it

        visited.add(current)                       # Mark node as processed

        if current == end:                         # If we reached the goal
            reconstruct_path(came_from, end, draw) # Draw the final path
            return True                            # A* succeeded

        # Visual: mark visited cells (except start and end)
        if current is not start and current is not end:
            current.state = VISITED                # Color as visited

        # Explore neighbors
        for neighbor in get_neighbors(grid, current):
            if neighbor.state == WALL:             # Skip walls
                continue

            # Tentative g_score if we go via current
            tentative_g = g_score[current] + 1     # Cost from start to neighbor

            # If neighbor not seen before or we found a cheaper path
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current      # Best parent so far
                g_score[neighbor] = tentative_g    # Update cost from start
                f_score[neighbor] = tentative_g + heuristic(neighbor, end)  # g + h

                if neighbor not in open_set_hash:  # If neighbor not already queued
                    count += 1                     # Increase tie-breaker
                    heappush(open_set, (f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)    # Remember it's in open set

        draw()                                     # Redraw grid with changes
        pygame.time.delay(10)                      # Small delay so animation is visible

    # If we exit the loop, no path was found
    return False
