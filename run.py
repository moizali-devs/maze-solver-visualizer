# import helper modules from src files and pygame library
import pygame
from src.grid import create_grid, draw_grid, get_node_at_pos

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

    running = True               # Flag to keep the game loop running
    while running:               # Main game loop
        for event in pygame.event.get():        # Get all events from pygame (keyboard, mouse, quit)
            if event.type == pygame.QUIT:       # If user clicks the close button
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:   # Any mouse button pressed
                mouse_pos = pygame.mouse.get_pos()     # Get mouse position in pixels
                # Find which node was clicked
                node = get_node_at_pos(grid, mouse_pos)

                if node is not None:                  # Only if click was inside grid
                    if event.button == 1:             # Left click
                        node.make_wall()              # Turn that cell into a wall
                    elif event.button == 3:           # Right click
                        node.reset()                        # Set running to False to exit the loop

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
