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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Solver Visualizer")  # Set the window title

    # Create the 2D grid of nodes
    grid = create_grid(ROWS, COLS, CELL_SIZE)

    # Are we in "start place" mode?
    placing_start = False
    # Are we in "end place" mode?
    placing_end = False

    # Keep reference to the start node and end node
    current_start = None
    current_end = None

    # Are we currently dragging to draw or erase walls?
    drawing_walls = False
    erasing_walls = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    placing_start = True
                    placing_end = False

                if event.key == pygame.K_e:
                    placing_end = True
                    placing_start = False

            # Mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                node = get_node_at_pos(grid, mouse_pos)

                if node:
                    if event.button == 1:
                        if placing_start:
                            if current_start:
                                current_start.reset()
                            node.make_start()
                            current_start = node
                            placing_start = False

                        elif placing_end:
                            if current_end:
                                current_end.reset()
                            node.make_end()
                            current_end = node
                            placing_end = False

                        else:
                            node.make_wall()       # Normal click → make a wall
                            drawing_walls = True   # Start drag-to-draw mode

                    elif event.button == 3:        # Right click → clear
                        node.reset()
                        if node == current_start:
                            current_start = None
                        if node == current_end:
                            current_end = None
                        erasing_walls = True       # Start drag-to-erase mode

            # Mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing_walls = False
                if event.button == 3:
                    erasing_walls = False

            # Mouse movement while a button might be held
            if event.type == pygame.MOUSEMOTION:
                mouse_buttons = pygame.mouse.get_pressed()
                mouse_pos = pygame.mouse.get_pos()
                node = get_node_at_pos(grid, mouse_pos)

                if node:
                    # If we are in drawing mode and left button is still held
                    if drawing_walls and mouse_buttons[0]:
                        if node.state not in (START, END):
                            node.make_wall()

                    # If we are in erasing mode and right button is still held
                    if erasing_walls and mouse_buttons[2]:
                        node.reset()
                        if node == current_start:
                            current_start = None
                        if node == current_end:
                            current_end = None

        # Fill the whole screen with a dark background color
        screen.fill((20, 20, 20))
        draw_grid(screen, grid)
        pygame.display.update()

    pygame.quit()


# Only run main() if this file is run directly, not imported
if __name__ == "__main__":
    main()
