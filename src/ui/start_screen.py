import pygame
import sys


def draw_text(surface, text, size, color, x, y, font_name="bahnschrift", bold=False):
    font = pygame.font.SysFont(font_name, size, bold=bold)
    render = font.render(text, True, color)
    rect = render.get_rect(center=(x, y))
    surface.blit(render, rect)


def start_screen(surface):
    WIDTH, HEIGHT = surface.get_size()

    # Load and scale Saitama PNG
    saitama = pygame.image.load("assets/start_screen/saitama.png")
    saitama = pygame.transform.scale(saitama, (260, 260))
    saitama_rect = saitama.get_rect()

    # Colors
    BG = (28, 27, 25)
    LEFT_PANEL = (193, 155, 52)
    CARD_BG = (38, 37, 35)
    CARD_BORDER = (80, 78, 74)
    RED = (215, 52, 52)
    RED_HOVER = (240, 80, 80)
    TEXT_MAIN = (245, 245, 245)
    TEXT_SUB = (210, 210, 210)
    ACCENT = (255, 210, 90)

    # Left panel wider for clean padding
    left_panel_rect = pygame.Rect(0, 0, int(WIDTH * 0.40), HEIGHT)

    # Card
    card_width = int(WIDTH * 0.45)
    card_height = int(HEIGHT * 0.62)
    card_rect = pygame.Rect(0, 0, card_width, card_height)
    card_rect.center = (int(WIDTH * 0.70), HEIGHT // 2)

    # Saitama positioned nicely on left
    saitama_rect.bottomleft = (left_panel_rect.left + 30, HEIGHT - 30)

    # Buttons
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

    running = True
    while running:
        surface.fill(BG)

        # Left panel
        pygame.draw.rect(surface, LEFT_PANEL, left_panel_rect)

        # Title on left panel
        draw_text(surface, "MAZE VISUALIZER", 28, (35, 24, 10),
                  left_panel_rect.centerx, int(HEIGHT * 0.14), bold=True)
        draw_text(surface, "DFS and A*", 20, (35, 24, 10),
                  left_panel_rect.centerx, int(HEIGHT * 0.19))

        # Saitama
        surface.blit(saitama, saitama_rect)

        # Main card
        pygame.draw.rect(surface, CARD_BORDER, card_rect, border_radius=18)
        inner_card = card_rect.inflate(-6, -6)
        pygame.draw.rect(surface, CARD_BG, inner_card, border_radius=16)

        draw_text(surface, "Maze Solver Visualizer", 34, TEXT_MAIN,
                  inner_card.centerx, inner_card.top + 55, bold=True)

        # Mouse tracking
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Button drawing function
        def draw_button(rect, base_color, label):
            is_hover = rect.collidepoint(mouse_pos)
            color = RED_HOVER if is_hover else base_color

            pygame.draw.rect(surface, (90, 25, 25), rect.move(0, 3), border_radius=12)
            pygame.draw.rect(surface, color, rect, border_radius=12)
            draw_text(surface, label, 24, TEXT_MAIN,
                      rect.centerx, rect.centery, bold=True)

        # Buttons
        draw_button(start_rect, RED, "START")
        draw_button(help_rect, RED, "HELP")
        draw_button(exit_rect, RED, "EXIT")

        # Bottom tagline – your original line
        # draw_text(
        #     surface,
        #     "Finding the shortest path? That’s just common sense.",
        #     16,
        #     ACCENT,
        #     inner_card.centerx,
        #     inner_card.bottom -30,   # moved inside the card
        # )

        # Click handling
        if click[0]:
            if start_rect.collidepoint(mouse_pos):
                return True
            if exit_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()
            if help_rect.collidepoint(mouse_pos):
                print("Help clicked (future expansion)")

        # Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
