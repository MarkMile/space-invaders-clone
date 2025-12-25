from __future__ import annotations  # Postpone type hint evaluation

import pygame
from pygame.sprite import Sprite
from typing import Tuple, TYPE_CHECKING

# To avoid circular imports during runtime
if TYPE_CHECKING:
    from space_invaders import SpaceInvaders
    from config import GameConfiguration


class Bullet(Sprite):
    """A class to manage bullets fired from the player's starfighter."""

    def __init__(self, game_instance: SpaceInvaders) -> None:
        """
        Initialize a bullet object at the starfighter's current position.

        Creates a rectangular bullet object using the game's configuration
        settings for color, speed and dimensions. The bullet's initial
        position is set to the starfighter's midtop position.

        Args:
            game_instance (SpaceInvaders): The current game instance, providing
            access to the screen, settings, and starfighter position.
        """
        super().__init__()
        self.screen: pygame.Surface = game_instance.screen
        self.settings: GameConfiguration = game_instance.settings
        self.color: Tuple[int, int, int] = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and set the correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = game_instance.starfighter.rect.midtop

        # Store the bullet's vertical position as a float for fine control.
        self.y = float(self.rect.y)

    def update(self) -> None:
        """
        Move the bullet upward on the screen

        Updates the bullet's position based on its speed and applies the change
        to the associated rectagle for rendering.
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """
        Draw the bullet to the screen.

        Renders a filled rectangle representing the bullet at its current position.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
