# src/node.py
import pygame  # For drawing rectangles

# States that each cell can have
EMPTY = "empty"
WALL = "wall"
START = "start"
END = "end"
VISITED = "visited"
PATH = "path"


class Node:
    def __init__(self, row, col, size):
        self.row = row                # Row index in grid
        self.col = col                # Column index in grid
        self.size = size              # Cell size in pixels
        self.state = EMPTY            # Default state

    # State helper methods
    def make_wall(self):
        self.state = WALL

    def make_start(self):
        self.state = START

    def make_end(self):
        self.state = END

    def make_visited(self):
        if self.state not in (START, END):
            self.state = VISITED

    def make_path(self):
        if self.state not in (START, END):
            self.state = PATH

    def reset(self):
        self.state = EMPTY

    def draw(self, surface, theme, top_offset):
        """Draw this node on the given surface using the theme colors."""
        # Pick color based on current state
        if self.state == WALL:
            color = theme["WALL"]
        elif self.state == START:
            color = theme["START"]
        elif self.state == END:
            color = theme["END"]
        elif self.state == VISITED:
            color = theme["VISITED"]
        elif self.state == PATH:
            color = theme["PATH"]
        else:
            color = theme["EMPTY"]

        # Convert grid position to screen position
        x = self.col * self.size                       # X coordinate
        y = top_offset + self.row * self.size          # Y coordinate with top margin

        rect = pygame.Rect(x, y, self.size, self.size) # Rectangle for this cell
        pygame.draw.rect(surface, color, rect)         # Draw the filled cell
