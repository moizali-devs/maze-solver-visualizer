# src/grid.py
import pygame

from .node import Node

# Space at the top reserved for the control bar
TOP_OFFSET = 110  # pixels  (match your top bar height)

def create_grid(rows, cols, size):
    """Create a 2D list of Node objects."""
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(Node(r, c, size))
        grid.append(row)
    return grid


def draw_grid(surface, grid, theme):
    """Draw all nodes and the grid lines."""
    if not grid:
        return

    rows = len(grid)
    cols = len(grid[0])
    cell_size = grid[0][0].size
    width, _height = surface.get_size()

    # Draw cells
    for row in grid:
        for node in row:
            node.draw(surface, theme, TOP_OFFSET)

    # Grid lines (horizontal)
    for r in range(rows + 1):
        y = TOP_OFFSET + r * cell_size
        pygame.draw.line(surface, theme["GRID_LINE"], (0, y), (width, y))

    # Grid lines (vertical)
    for c in range(cols + 1):
        x = c * cell_size
        pygame.draw.line(
            surface,
            theme["GRID_LINE"],
            (x, TOP_OFFSET),
            (x, TOP_OFFSET + rows * cell_size),
        )


def get_node_at_pos(grid, pos):
    """Convert mouse position to a node in the grid, or None if outside."""
    if not grid:
        return None

    x, y = pos
    cell_size = grid[0][0].size

    # Adjust for the top offset area (control bar)
    y_relative = y - TOP_OFFSET
    if y_relative < 0:
        return None

    col = x // cell_size
    row = y_relative // cell_size

    rows = len(grid)
    cols = len(grid[0])

    if 0 <= row < rows and 0 <= col < cols:
        return grid[row][col]

    return None
