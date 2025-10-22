from __future__ import annotations  # Postpone type hint evaluation

import pygame.font
from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:  # To avoid circular imports during runtime
    from space_invaders import SpaceInvaders


class Button:
    """Represents a clickable button in the game UI."""

    def __init__(self, game_instance: SpaceInvaders, button_text: str) -> None:
        """
        Initialize button attributes and prepare its initial appearance.

        Args:
            game_instance (SpaceInvaders): The current game instance, providing access to the screen.
            button_text (str): The text to display on the button.
        """
        self.screen: pygame.Surface = game_instance.screen
        self.screen_rect: pygame.Rect = game_instance.screen.get_rect()

        # Define button dimensions and properties.
        self.width: int = 200
        self.height: int = 50
        self.text_color: Tuple[int, int, int] = (0, 0, 0)
        self.button_color: Tuple[int, int, int] = (255, 255, 255)
        self.font: pygame.font.Font = pygame.font.SysFont(None, 48)

        # Create button's rectangle and center it on the screen.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare the button message as a rendered image.
        self.prepare_text(button_text)

    def prepare_text(self, button_text: str) -> None:
        """
        Render the button's text into an image and center it on the button.

        Args:
            button_text (str): The text to display on the button.
        """
        self.text_image: pygame.Surface = self.font.render(
            button_text, True, self.text_color, self.button_color
        )
        self.text_image_rect: pygame.Rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self) -> None:
        """
        Draw the button on the screen, including its background and text.
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
