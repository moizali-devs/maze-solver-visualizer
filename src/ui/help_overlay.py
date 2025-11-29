# src/ui/help_overlay.py
import pygame


def draw_help_overlay(surface, theme, current_algorithm):
    """Draw a simple help/info box over the screen."""
    width, height = surface.get_size()

    # Semi transparent dark overlay
    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    surface.blit(overlay, (0, 0))

    # Centered box
    box_width = 520
    box_height = 260
    box_rect = pygame.Rect(0, 0, box_width, box_height)
    box_rect.center = (width // 2, height // 2)

    pygame.draw.rect(surface, theme["TOPBAR_BG"], box_rect, border_radius=14)
    pygame.draw.rect(surface, theme["TOPBAR_BORDER"], box_rect, width=2, border_radius=14)

    # Helper to draw lines of text
    def draw_line(text, size, color, x, y, bold=False):
        font = pygame.font.SysFont("bahnschrift", size, bold=bold)
        render = font.render(text, True, color)
        rect = render.get_rect(midleft=(x, y))
        surface.blit(render, rect)

    text_color = theme["BUTTON_TEXT"]

    # Title
    draw_line("Help", 26, text_color, box_rect.left + 24, box_rect.top + 40, bold=True)

    # Controls
    draw_line("Controls:", 18, text_color, box_rect.left + 24, box_rect.top + 80, bold=True)
    draw_line("- Left click and drag: draw walls", 16, text_color, box_rect.left + 40, box_rect.top + 110)
    draw_line("- Right click and drag: erase walls", 16, text_color, box_rect.left + 40, box_rect.top + 135)
    draw_line("- Use the buttons at the top to set start/end and run algorithms.", 16,
              text_color, box_rect.left + 40, box_rect.top + 160)

    # Algorithms
    draw_line("Algorithms:", 18, text_color, box_rect.left + 24, box_rect.top + 195, bold=True)
    draw_line("DFS  - explores deeply along one path; not always shortest.", 16,
              text_color, box_rect.left + 40, box_rect.top + 220)
    draw_line("A*   - uses distance and a heuristic to find a shortest path.", 16,
              text_color, box_rect.left + 40, box_rect.top + 245)

    # Optional small indicator of current algorithm
    small = pygame.font.SysFont("bahnschrift", 14, bold=True)
    info = small.render(f"Current: {current_algorithm.upper()}", True, text_color)
    info_rect = info.get_rect(bottomright=(box_rect.right - 12, box_rect.bottom - 8))
    surface.blit(info, info_rect)
