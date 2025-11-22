import pygame                        # Import pygame for drawing grid lines
# Import our Node class from node.py in the same package
from .node import Node

# Color for grid lines (slightly lighter gray)
GRID_LINE = (50, 50, 50)
CELL_COLOR = (30, 30, 30)            # Default fill color for each cell


def create_grid(rows, cols, size):
    # Create a 2D list (list of lists) of Node objects
    # If we want to change the size of the grid we will simply just change the "Size" variable when calling the function
    grid = []                        # Empty list that will hold all rows
    for r in range(rows):            # Loop through each row index
        row = []                     # List to hold one full row of nodes
        for c in range(cols):        # Loop through each column index
            node = Node(r, c, size)  # Create a new Node at row r, column c
            row.append(node)         # Add this node to the current row
        grid.append(row)             # Add the finished row to the grid
    return grid                      # Return the complete 2D grid


def draw_grid(surface, grid):
    # here surface is literally our screen lol
    # First draw each cell as a filled rectangle (there will be no seperation bcz all same color rn)
    for row in grid:                         # Loop through each row in the grid
        for node in row:                     # Loop through each Node in the row
            # Draw the node with the base cell color
            node.draw(surface, CELL_COLOR)

    # Then draw the grid lines on top
    # Total number of rows gets it and stores it in the "rows"
    rows = len(grid)
    # Total number of columns gets it and stores it in the "coloumns"
    cols = len(grid[0]) if rows > 0 else 0
    if rows == 0 or cols == 0:               # Safety check if grid is empty
        return                               # If there is nothing to draw, exit the function

    size = grid[0][0].size                   # Each cell uses the same size
    # Get the full surface width and height. This surface.get_size() is a built in python function.
    width, height = surface.get_size()

    # Draw horizontal lines for rows
    for r in range(rows + 1):                # One more line than rows to close the bottom
        y = r * size                         # Y position of the line
        pygame.draw.line(surface, GRID_LINE, (0, y),
                         (width, y))  # From left to right

    # Draw vertical lines for coloumns
    # One more line than columns to close the right side
    for c in range(cols + 1):
        x = c * size                         # X position of the line
        pygame.draw.line(surface, GRID_LINE, (x, 0),
                         (x, height))  # From top to bottom
