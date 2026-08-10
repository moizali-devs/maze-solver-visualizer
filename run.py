# run.py
import pygame

from src.algorithms.astar import astar
from src.algorithms.dfs import dfs
from src.grid import TOP_OFFSET, create_grid, draw_grid, get_node_at_pos
from src.node import END, PATH, START, VISITED, WALL
from src.ui.help_overlay import draw_help_overlay
from src.ui.start_screen import start_screen
from src.ui.themes import DARK_THEME, LIGHT_THEME
from src.ui.topbar import TopBar

# Window and grid settings
WIDTH, HEIGHT = 1280, 800  # You can change this resolution
ROWS = 30                  # Number of rows in the grid
# Cell size based on available vertical space under the top bar
CELL_SIZE = (HEIGHT - TOP_OFFSET) // ROWS
COLS = WIDTH // CELL_SIZE        # Number of columns derived from width


def redraw(screen, grid, theme, topbar, show_help, current_algorithm):
    screen.fill(theme["BACKGROUND"])
    draw_grid(screen, grid, theme)

    # Draw help overlay first so topbar stays clickable on top
    if show_help:
        draw_help_overlay(screen, theme, current_algorithm)

    topbar.draw(screen, theme)
    pygame.display.update()


def place_default_start_end(grid):
    """Place start near left and end near right at middle row."""
    rows = len(grid)
    cols = len(grid[0])

    mid_row = rows // 2

    start_node = grid[mid_row][2]
    end_node = grid[mid_row][cols - 3]

    start_node.make_start()
    end_node.make_end()

    return start_node, end_node


def clear_walls_and_paths(grid, keep_start_end=True):
    """Clear walls, visited, and path states."""
    for row in grid:
        for node in row:
            if keep_start_end and node.state in (START, END):
                continue
            if node.state in (WALL, VISITED, PATH):
                node.reset()


def clear_all(grid):
    """Reset the whole grid and return new default start and end."""
    for row in grid:
        for node in row:
            node.reset()
    return place_default_start_end(grid)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Solver Visualizer")

    # Show start menu
    if not start_screen(screen):
        return

    # Initial theme and algorithm
    current_theme = DARK_THEME
    current_algorithm = "dfs"

    # Build grid and default start/end
    grid = create_grid(ROWS, COLS, CELL_SIZE)
    current_start, current_end = place_default_start_end(grid)

    # Control bar and state flags
    topbar = TopBar(WIDTH)
    placing_start = False
    placing_end = False
    drawing_walls = False
    erasing_walls = False
    show_help = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_help = False
            # Quit
            if event.type == pygame.QUIT:
                running = False

            # Top bar actions
            action = topbar.handle_event(event)
            if action == "select_dfs":
                current_algorithm = "dfs"
            elif action == "select_astar":
                current_algorithm = "astar"
            elif action == "set_start":
                placing_start = True
                placing_end = False
            elif action == "set_end":
                placing_end = True
                placing_start = False
            elif action == "visualize":
                if current_start and current_end:
                    if current_algorithm == "dfs":
                        dfs(
                            lambda: redraw(
                                screen, grid, current_theme, topbar, show_help, current_algorithm
                            ),
                            grid,
                            current_start,
                            current_end,
                        )
                    else:
                        astar(
                            lambda: redraw(
                                screen, grid, current_theme, topbar, show_help, current_algorithm
                            ),
                            grid,
                            current_start,
                            current_end,
                        )
            elif action == "clear_walls":
                clear_walls_and_paths(grid, keep_start_end=True)
            elif action == "clear_all":
                current_start, current_end = clear_all(grid)
            elif action == "toggle_theme":
                current_theme = LIGHT_THEME if current_theme is DARK_THEME else DARK_THEME
            elif action == "toggle_help":
                show_help = not show_help

            # Mouse input for grid
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                node = get_node_at_pos(grid, mouse_pos)

                if node:
                    if event.button == 1:  # Left click
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
                            node.make_wall()
                            drawing_walls = True
                    elif event.button == 3:  # Right click
                        if node == current_start:
                            current_start = None
                        if node == current_end:
                            current_end = None
                        node.reset()
                        erasing_walls = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing_walls = False
                if event.button == 3:
                    erasing_walls = False

            if event.type == pygame.MOUSEMOTION: 
                mouse_buttons = pygame.mouse.get_pressed()
                mouse_pos = pygame.mouse.get_pos()
                node = get_node_at_pos(grid, mouse_pos)

                if node:
                    if drawing_walls and mouse_buttons[0]:
                        if node.state not in (START, END):
                            node.make_wall()
                    if erasing_walls and mouse_buttons[2]:
                        if node == current_start:
                            current_start = None
                        if node == current_end:
                            current_end = None
                        node.reset()

        redraw(screen, grid, current_theme, topbar, show_help, current_algorithm)

    pygame.quit()


if __name__ == "__main__":
    main()
