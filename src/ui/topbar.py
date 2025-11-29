# src/ui/topbar.py
import pygame
from src.grid import TOP_OFFSET


class Button:
    def __init__(self, rect, label, action):
        self.rect = rect        # pygame.Rect for position and size
        self.label = label      # Text shown on the button
        self.action = action    # String describing what this button does

    def draw(self, surface, theme, mouse_pos):
        """Draw button with hover effect."""
        is_hover = self.rect.collidepoint(mouse_pos)

        base = theme["BUTTON_BG"]
        active = theme["BUTTON_BG_ACTIVE"]
        text_color = theme["BUTTON_TEXT"]

        color = active if is_hover else base

        # Small shadow effect
        shadow_rect = self.rect.move(0, 2)
        pygame.draw.rect(surface, theme["TOPBAR_BORDER"], shadow_rect, border_radius=8)
        pygame.draw.rect(surface, color, self.rect, border_radius=8)

        font = pygame.font.SysFont("bahnschrift", 18, bold=True)
        render = font.render(self.label, True, text_color)
        text_rect = render.get_rect(center=self.rect.center)
        surface.blit(render, text_rect)


class TopBar:
    def __init__(self, width):
        self.height = TOP_OFFSET                   # Match grid top offset
        self.rect = pygame.Rect(0, 0, width, self.height)

        # Buttons layout
        padding_x = 10
        padding_y = 10
        button_width = 110
        button_height = 32
        gap = 8

        buttons = []

        # Positions in a single row
        labels_actions = [
            ("DFS", "select_dfs"),
            ("A*", "select_astar"),
            ("Set Start", "set_start"),
            ("Set End", "set_end"),
            ("Visualize", "visualize"),
            ("Clear Walls", "clear_walls"),
            ("Clear All", "clear_all"),
            ("Theme", "toggle_theme"),
            ("Help", "toggle_help"),
        ]

        x = padding_x
        y = padding_y

        for label, action in labels_actions:
            rect = pygame.Rect(x, y, button_width, button_height)
            buttons.append(Button(rect, label, action))
            x += button_width + gap

        self.buttons = buttons

    def handle_event(self, event):
        """Return an action string if a button was clicked, else None."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for button in self.buttons:
                if button.rect.collidepoint(mouse_pos):
                    return button.action
        return None

    def draw(self, surface, theme):
        """Draw the top bar and all buttons."""
        pygame.draw.rect(surface, theme["TOPBAR_BG"], self.rect)
        pygame.draw.rect(surface, theme["TOPBAR_BORDER"], self.rect, width=1)

        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.draw(surface, theme, mouse_pos)
