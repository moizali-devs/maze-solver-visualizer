# import helper modules from src files and pygame library
import pygame
from src.grid import create_grid, draw_grid, get_node_at_pos   # Grid helpers
from src.node import START, END                                # State names
from src.algorithms.dfs import dfs                             # Our DFS function

# Window size in pixels
WIDTH, HEIGHT = 800, 600          # Width and height of the window

# Grid settings
ROWS, COLS = 30, 40               # Number of rows and columns in the grid

# Size of each cell in pixels based on width and number of columns
CELL_SIZE = WIDTH // COLS


def redraw(screen, grid):
    """Helper function to clear screen, draw grid, and update display."""
    screen.fill((20, 20, 20))         # Fill background with dark color
    draw_grid(screen, grid)           # Draw cells and grid lines
    pygame.display.update()           # Refresh the window


def main():
    # Initialize all pygame modules so we can use them
    pygame.init()

    # Create the main window with specified size
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Solver Visualizer")  # Set the window title

    # Build a 2D list of Node objects
    grid = create_grid(ROWS, COLS, CELL_SIZE)

    # Are we in "start place" mode?
    placing_start = False
    # Are we in "end place" mode?
    placing_end = False

    # Keep reference to the start node and end node
    current_start = None
    current_end = None

    # Drag states for walls (from previous step)
    drawing_walls = False                # Are we dragging to draw walls?
    erasing_walls = False                # Are we dragging to erase walls?

    running = True                       # Flag to keep the game loop running
    while running:                       # Main game loop
        for event in pygame.event.get():  # Get all events from pygame
            if event.type == pygame.QUIT:  # If user clicks the close button
                running = False

            # Keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:   # Press S to place start
                    placing_start = True
                    placing_end = False

                if event.key == pygame.K_e:   # Press E to place end
                    placing_end = True
                    placing_start = False

                if event.key == pygame.K_d:   # Press D to run DFS
                    # Only run DFS if both start and end exist
                    if current_start and current_end:
                        dfs(lambda: redraw(screen, grid), grid, current_start, current_end)

            # Mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()           # Get mouse x, y
                node = get_node_at_pos(grid, mouse_pos)      # Find which node was clicked

                if node:
                    if event.button == 1:                    # Left click
                        if placing_start:                    # If S was pressed before
                            if current_start:                # If a start already exists
                                current_start.reset()        # Clear old start
                            node.make_start()                # Make new start
                            current_start = node             # Save reference
                            placing_start = False            # Exit start mode

                        elif placing_end:                    # If E was pressed before
                            if current_end:                  # If an end already exists
                                current_end.reset()          # Clear old end
                            node.make_end()                  # Make new end
                            current_end = node               # Save reference
                            placing_end = False              # Exit end mode

                        else:
                            node.make_wall()                 # Normal click → make a wall
                            drawing_walls = True             # Start drag-to-draw mode

                    elif event.button == 3:                  # Right click → clear
                        node.reset()                         # Reset node state
                        if node == current_start:
                            current_start = None
                        if node == current_end:
                            current_end = None
                        erasing_walls = True                 # Start drag-to-erase mode

            # Mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:                        # Left released
                    drawing_walls = False                    # Stop drawing
                if event.button == 3:                        # Right released
                    erasing_walls = False                    # Stop erasing

            # Mouse moved
            if event.type == pygame.MOUSEMOTION:
                mouse_buttons = pygame.mouse.get_pressed()   # Check which buttons are held
                mouse_pos = pygame.mouse.get_pos()           # Current mouse position
                node = get_node_at_pos(grid, mouse_pos)      # Node under mouse

                if node:
                    if drawing_walls and mouse_buttons[0]:   # Drag drawing with left
                        if node.state not in (START, END):   # Do not override start/end
                            node.make_wall()

                    if erasing_walls and mouse_buttons[2]:   # Drag erasing with right
                        node.reset()
                        if node == current_start:
                            current_start = None
                        if node == current_end:
                            current_end = None

        # Draw everything each frame
        redraw(screen, grid)

    pygame.quit()                           # Cleanly close all pygame modules


# Only run main() if this file is run directly, not imported
if __name__ == "__main__":
    main()                                  # Start the program
