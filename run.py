# import helper modules from src files and pygame library
import pygame
from src.grid import create_grid, draw_grid, get_node_at_pos
from src.node import START, END

# Window size in pixels
WIDTH, HEIGHT = 800, 600          # Width and height of the window

# Grid settings
ROWS, COLS = 30, 40  # Number of rows and columns in the grid

# Size of each cell in pixels based on width and number of columns
CELL_SIZE = WIDTH // COLS


def main():
    # Initialize all pygame modules (Turning on and removing all pygame features so we can use them)
    pygame.init()

    # Create the main window
    # Set the window size (Width and height as specified above)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(
        "Maze Solver Visualizer")  # Set the window title

    # Create the 2D grid of nodes
    # Build a 2D list of Node objects
    grid = create_grid(ROWS, COLS, CELL_SIZE)

    # Are we in "start place" mode?
    placing_start = False
    # Are we in "end place" mode?
    placing_end = False

    # Keep reference to the start node and end node
    current_start = None
    current_end = None

    running = True               # Flag to keep the game loop running
    while running:               # Main game loop
        for event in pygame.event.get():        # Get all events from pygame (keyboard, mouse, quit)
            if event.type == pygame.QUIT:       # If user clicks the close button
                running = False

            if event.type == pygame.KEYDOWN:  # this is for basically checking if the key s is pressed if it is pressed then we place the start node
                if event.key == pygame.K_s:
                    placing_start = True
                    placing_end = False

                if event.key == pygame.K_e:  # this is for basically checking if the key e is pressed if it is pressed then we place the end node
                    placing_end = True
                    placing_start = False

            # Mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()          # Get mouse x, y
                # Find which node was clicked
                node = get_node_at_pos(grid, mouse_pos)

                if node:
                    if event.button == 1:                   # Left click
                        if placing_start:                   # If S was pressed
                            if current_start:               # If a start already exists
                                current_start.reset()       # Clear old start
                            node.make_start()               # Make new start
                            current_start = node            # Save reference
                            placing_start = False           # Exit start mode

                        elif placing_end:                   # If E was pressed
                            if current_end:                 # If an end already exists
                                current_end.reset()         # Clear old end
                            node.make_end()                 # Make new end
                            current_end = node              # Save reference
                            placing_end = False             # Exit end mode

                        else:
                            node.make_wall()                # Normal click → make a wall

                    elif event.button == 3:                 # Right click → clear
                        node.reset()                        # Reset node state
                        if node == current_start:
                            current_start = None
                        if node == current_end:
                            current_end = None

        # Fill the whole screen with a dark background color
        screen.fill((20, 20, 20))
        # Draw all cells and the grid lines
        draw_grid(screen, grid)  # (we pass the surface grid!)
        # Update the window with whatever we just drew
        pygame.display.update()

    pygame.quit()                              # Cleanly close all pygame modules


# Only run main() if this file is run directly, not imported
if __name__ == "__main__":
    main()                                     # Start the program
