import pygame                                      # For drawing rectangles

# States a cell can have
EMPTY = "empty"                                    # Normal cell
WALL = "wall"                                      # Barrier
START = "start"                                    # Start point
END = "end"                                        # Goal point
VISITED = "visited"                                # Explored by the algorithm
PATH = "path"                                      # Final shortest path cell


class Node:
    def __init__(self, row, col, size):
        self.row = row                              # Row index
        self.col = col                              # Column index
        self.size = size                            # Pixel size of the square cell
        self.state = EMPTY                          # Default state is empty

    def make_wall(self):
        self.state = WALL                           # Turn this cell into a wall

    def make_start(self):
        self.state = START                          # Mark as start cell

    def make_end(self):
        self.state = END                            # Mark as end cell

    def make_visited(self):
        # Only mark as visited if it is not start or end
        if self.state not in (START, END):
            self.state = VISITED                    # Mark as visited by the algorithm

    def make_path(self):
        # Only mark as path if it is not start or end
        if self.state not in (START, END):
            self.state = PATH                       # Mark as part of final path

    def reset(self):
        self.state = EMPTY                          # Reset back to empty

    def draw(self, surface, base_color):
        # Decide color based on state
        if self.state == WALL:
            color = (180, 180, 180)                 # Light gray for walls
        elif self.state == START:
            color = (0, 200, 0)                     # Green for start
        elif self.state == END:
            color = (200, 0, 0)                     # Red for end
        elif self.state == VISITED:
            color = (0, 120, 200)                   # Blue-ish for visited cells
        elif self.state == PATH:
            color = (255, 215, 0)                   # Yellow for final path
        else:
            color = base_color                      # Dark base for empty cells

        # Convert row/col location into pixel coordinates
        x = self.col * self.size                    # X position in pixels
        y = self.row * self.size                    # Y position in pixels

        # Define the rectangle representing this cell
        rect = pygame.Rect(x, y, self.size, self.size)

        # Draw the rectangle on the given surface
        pygame.draw.rect(surface, color, rect)
