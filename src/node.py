import pygame                      # Import pygame so we can use its drawing functions


class Node:
    def __init__(self, row, col, size):
        self.row = row             # Row index of this node in the grid
        self.col = col             # Column index of this node in the grid
        # Pixel size of the box (one side and each side is the same because square)
        self.size = size

    def draw(self, surface, color):
        # Convert row and column to actual x, y pixel coordinates
        # X position in pixels (columns go left to right)
        x = self.col * self.size
        # Y position in pixels (rows go top to bottom)
        y = self.row * self.size

        # Create a pygame rectangle for this cell (rect=rectangle)
        rect = pygame.Rect(x, y, self.size, self.size)  # (x, y, width, height)

        # Draw the filled rectangle on the given surface (we use simple pygame function for this)
        pygame.draw.rect(surface, color, rect)
