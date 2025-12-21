import pygame
import sys
import os

# Utility functions for resource loading, text rendering, help popup, and start screen.
# These are used for managing assets and UI elements in the application when executing from different environments.
def resource_path(relative_path: str) -> str:
    """
    Get absolute path to resource, works for dev and for PyInstaller.
    """
    # When running as a bundled app
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        # When running from source with `python run.py`
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def draw_text(surface, text, size, color, x, y, font_name="bahnschrift", bold=False):
    font = pygame.font.SysFont(font_name, size, bold=bold)
    render = font.render(text, True, color)
    rect = render.get_rect(center=(x, y))
    surface.blit(render, rect)


def draw_help_popup(surface):
    width, height = surface.get_size()

    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 170))
    surface.blit(overlay, (0, 0))

    box_w, box_h = 560, 300
    box = pygame.Rect(0, 0, box_w, box_h)
    box.center = (width // 2, height // 2)

    pygame.draw.rect(surface, (38, 37, 35), box, border_radius=16)
    pygame.draw.rect(surface, (90, 88, 84), box, width=2, border_radius=16)

    def line(txt, y, size=18, bold=False):
        font = pygame.font.SysFont("bahnschrift", size, bold=bold)
        surf = font.render(txt, True, (245, 245, 245))
        surface.blit(surf, (box.left + 22, y))

    line("Help", box.top + 18, size=26, bold=True)
    line("Controls:", box.top + 62, size=18, bold=True)
    line("Left click and drag: draw walls", box.top + 95, size=16)
    line("Right click and drag: erase walls", box.top + 120, size=16)
    line("Use Set Start / Set End buttons to place nodes", box.top + 145, size=16)
    line("Press Visualize to run DFS or A*", box.top + 170, size=16)

    line("Close:", box.top + 220, size=18, bold=True)
    line("Press ESC or click the HELP button again", box.top + 250, size=16)


def start_screen(surface):
    WIDTH, HEIGHT = surface.get_size()

    saitama = pygame.image.load(resource_path("assets/start_screen/saitama.png"))
    saitama = pygame.transform.scale(saitama, (260, 260))
    saitama_rect = saitama.get_rect()

    BG = (28, 27, 25)
    LEFT_PANEL = (193, 155, 52)
    CARD_BG = (38, 37, 35)
    CARD_BORDER = (80, 78, 74)
    RED = (215, 52, 52)
    RED_HOVER = (240, 80, 80)
    TEXT_MAIN = (245, 245, 245)

    left_panel_rect = pygame.Rect(0, 0, int(WIDTH * 0.40), HEIGHT)

    card_width = int(WIDTH * 0.45)
    card_height = int(HEIGHT * 0.62)
    card_rect = pygame.Rect(0, 0, card_width, card_height)
    card_rect.center = (int(WIDTH * 0.70), HEIGHT // 2)

    saitama_rect.bottomleft = (left_panel_rect.left + 30, HEIGHT - 30)

    BUTTON_WIDTH, BUTTON_HEIGHT = 260, 54
    BUTTON_GAP = 18

    start_rect = pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)
    help_rect = pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)
    exit_rect = pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)

    buttons_center_x = card_rect.centerx
    first_button_y = card_rect.centery - BUTTON_HEIGHT - BUTTON_GAP

    start_rect.center = (buttons_center_x, first_button_y)
    help_rect.center = (buttons_center_x, first_button_y + BUTTON_HEIGHT + BUTTON_GAP)
    exit_rect.center = (buttons_center_x, first_button_y + 2 * (BUTTON_HEIGHT + BUTTON_GAP))

    show_help = False

    running = True
    while running:
        surface.fill(BG)

        pygame.draw.rect(surface, LEFT_PANEL, left_panel_rect)

        draw_text(surface, "MAZE VISUALIZER", 28, (35, 24, 10),
                  left_panel_rect.centerx, int(HEIGHT * 0.14), bold=True)
        draw_text(surface, "DFS and A*", 20, (35, 24, 10),
                  left_panel_rect.centerx, int(HEIGHT * 0.19))

        surface.blit(saitama, saitama_rect)

        pygame.draw.rect(surface, CARD_BORDER, card_rect, border_radius=18)
        inner_card = card_rect.inflate(-6, -6)
        pygame.draw.rect(surface, CARD_BG, inner_card, border_radius=16)

        draw_text(surface, "Maze Solver Visualizer", 34, TEXT_MAIN,
                  inner_card.centerx, inner_card.top + 55, bold=True)

        mouse_pos = pygame.mouse.get_pos()

        def draw_button(rect, base_color, label):
            is_hover = rect.collidepoint(mouse_pos)
            color = RED_HOVER if is_hover else base_color
            pygame.draw.rect(surface, (90, 25, 25), rect.move(0, 3), border_radius=12)
            pygame.draw.rect(surface, color, rect, border_radius=12)
            draw_text(surface, label, 24, TEXT_MAIN, rect.centerx, rect.centery, bold=True)

        draw_button(start_rect, RED, "START")
        draw_button(help_rect, RED, "HELP")
        draw_button(exit_rect, RED, "EXIT")

        if show_help:
            draw_help_popup(surface)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_help = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_rect.collidepoint(mouse_pos) and not show_help:
                    return True

                if exit_rect.collidepoint(mouse_pos) and not show_help:
                    pygame.quit()
                    sys.exit()

                if help_rect.collidepoint(mouse_pos):
                    show_help = not show_help

        pygame.display.update()
