import pygame                      # Import pygame so we can use its drawing functions


# Simple states for each cell
EMPTY = "empty"                            # Cell has nothing
WALL = "wall"                              # Cell is a wall


class Node:
    def __init__(self, row, col, size):
        self.row = row             # Row index of this node in the grid
        self.col = col             # Column index of this node in the grid
        self.state = EMPTY
        # Pixel size of the box (one side and each side is the same because square)
        self.size = size

    def make_wall(self):
        self.state = WALL                  # Change state to wall

    def reset(self):
        self.state = EMPTY                 # Change state back to empty

    def draw(self, surface, base_color):
        if self.state == WALL:             # If the cell is a wall
            color = (180, 180, 180)        # Light gray color for walls
        else:
            color = base_color             # Use the base color for empty cells

        # Convert row and column to actual x, y pixel coordinates
        # X position in pixels (columns go left to right)
        x = self.col * self.size
        # Y position in pixels (rows go top to bottom)
        y = self.row * self.size

        # Create a pygame rectangle for this cell (rect=rectangle)
        rect = pygame.Rect(x, y, self.size, self.size)  # (x, y, width, height)

        # Draw the filled rectangle on the given surface (we use simple pygame function for this)
        pygame.draw.rect(surface, color, rect)
