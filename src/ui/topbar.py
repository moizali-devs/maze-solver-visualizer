# src/ui/topbar.py
import pygame

from src.grid import TOP_OFFSET


class Button:
    """Simple rectangular button used in the top navigation bar."""

    def __init__(self, rect: pygame.Rect, label: str, action: str, primary: bool = False):
        self.rect = rect
        self.label = label
        self.action = action
        self.primary = primary

    def _primary_colors(self, theme):
        """Derive primary button colors from theme PATH color."""
        base = theme.get("PATH", (0, 200, 120))
        # Slightly brighter for hover
        hover = tuple(min(255, int(c * 1.1)) for c in base)
        # Choose text based on brightness
        text = (10, 10, 15) if sum(base) > 400 else (245, 245, 250)
        return base, hover, text

    def draw(self, surface, theme, mouse_pos):
        is_hover = self.rect.collidepoint(mouse_pos)

        if self.primary:
            base, hover, text_color = self._primary_colors(theme)
            bg_color = hover if is_hover else base
        else:
            bg_color = theme["BUTTON_BG_ACTIVE"] if is_hover else theme["BUTTON_BG"]
            text_color = theme["BUTTON_TEXT"]

        # Flat rectangle, small radius for clean look
        pygame.draw.rect(surface, bg_color, self.rect, border_radius=6)

        font = pygame.font.SysFont("bahnschrift", 16, bold=True)
        text_surf = font.render(self.label, True, text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)


class TopBar:
    """
    Horizontal navigation bar at the top of the window.

    Layout: title on the left, all controls in a single row on the right.
    """

    def __init__(self, width: int):
        self.height = TOP_OFFSET
        self.rect = pygame.Rect(0, 0, width, self.height)

        self.title = "Maze Solver Visualizer"

        # Button definitions: (label, action, primary?)
        self.button_defs = [
            ("DFS", "select_dfs", False),
            ("A*", "select_astar", False),
            ("VISUALIZE", "visualize", True),
            ("Set Start", "set_start", False),
            ("Set End", "set_end", False),
            ("Clear Walls", "clear_walls", False),
            ("Clear All", "clear_all", False),
            ("Theme", "toggle_theme", False),
            ("Help", "toggle_help", False),
        ]

        self.buttons = self._build_buttons(width)

    def _build_buttons(self, width: int):
        """Create button objects laid out in a single straight line."""
        padding_left_title = 18        # left padding before the title
        padding_right = 16             # right padding at end of bar
        button_gap = 8                 # space between buttons
        padding_y = 16                 # vertical padding inside bar

        # Space reserved for title on the left
        title_reserved_width = 220

        usable_left = padding_left_title + title_reserved_width
        usable_right = width - padding_right
        usable_width = max(0, usable_right - usable_left)

        num_buttons = len(self.button_defs)
        total_gap_width = button_gap * (num_buttons - 1)
        available_for_buttons = max(0, usable_width - total_gap_width)

        min_button_width = 70
        button_width = max(min_button_width, available_for_buttons // max(1, num_buttons))

        max_button_height = self.height - 2 * padding_y
        button_height = max(26, min(40, max_button_height))
        y = (self.height - button_height) // 2

        buttons = []
        x = usable_left
        for label, action, primary in self.button_defs:
            rect = pygame.Rect(x, y, button_width, button_height)
            buttons.append(Button(rect, label, action, primary))
            x += button_width + button_gap

        return buttons

    def handle_event(self, event):
        """Return the associated action string if a button is clicked."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for button in self.buttons:
                if button.rect.collidepoint(mouse_pos):
                    return button.action
        return None

    def draw(self, surface, theme):
        """Draw the top bar background, title text and buttons."""
        # Bar background
        pygame.draw.rect(surface, theme["TOPBAR_BG"], self.rect)

        # Bottom separator line like a navbar
        pygame.draw.line(
            surface,
            theme["TOPBAR_BORDER"],
            (self.rect.left, self.rect.bottom - 1),
            (self.rect.right, self.rect.bottom - 1),
            width=1,
        )

        # Title on the left
        title_font = pygame.font.SysFont("bahnschrift", 22, bold=True)
        subtitle_font = pygame.font.SysFont("bahnschrift", 12)
        title_color = theme["BUTTON_TEXT"]

        title_surf = title_font.render(self.title, True, title_color)
        title_rect = title_surf.get_rect()
        title_rect.left = 18
        title_rect.centery = self.rect.centery - 6
        surface.blit(title_surf, title_rect)

        # Small subtitle under title if there is room
        subtitle_surf = subtitle_font.render("DFS and A* maze solver", True, title_color)
        subtitle_rect = subtitle_surf.get_rect()
        subtitle_rect.left = 18
        subtitle_rect.top = title_rect.bottom - 2
        if subtitle_rect.bottom < self.rect.bottom - 6:
            surface.blit(subtitle_surf, subtitle_rect)

        # Buttons on the right
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.draw(surface, theme, mouse_pos)
