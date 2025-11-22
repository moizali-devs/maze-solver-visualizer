import pygame                      # Import pygame so we can use its drawing functions

# States a cell can have
EMPTY = "empty"                                   # Normal cell
WALL = "wall"                                     # Barrier
START = "start"                                   # Start point
END = "end"                                       # End/goal point


class Node:
    def __init__(self, row, col, size):
        self.row = row             # Row index of this node in the grid
        self.col = col             # Column index of this node in the grid
        # Pixel size of the box (one side and each side is the same because square)
        self.size = size
        self.state = EMPTY

    def make_wall(self):
        self.state = WALL                  # Change state to wall

    def make_start(self):
        self.state = START                  # Mark cell as start

    def make_end(self):
        self.state = END                    # Mark cell as goal

    def reset(self):
        self.state = EMPTY                 # Change state back to empty

    def draw(self, surface, base_color):
        if self.state == WALL:             # If the cell is a wall
            color = (180, 180, 180)        # Wall Color
        elif self.state == START:
            color = (0, 200, 0)          # Green color for start
        elif self.state == END:
            color = (200, 0, 0)          # Red for end
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
