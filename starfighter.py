
from __future__ import annotations  # Postpone type hint evaluation

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

# To avoid circular imports during runtime
if TYPE_CHECKING:
    from config import GameConfiguration
    from space_invaders import SpaceInvaders


class Starfighter(Sprite):
    """A class to manage the starfighter."""

    def __init__(self, game_instance: SpaceInvaders, image_path: str) -> None:
        super().__init__()
        """ 
        Initialize the starfighter and set its starting position. 
        
        Args:
            game_instance (SpaceInvaders): The current game instance, providing
            access to the screen and settings.
            image_path (str): The file path to the starfighter image.
        """
        self.screen: pygame.Surface = game_instance.screen
        self.screen_rect: pygame.rect = game_instance.screen.get_rect()
        self.settings: GameConfiguration = game_instance.settings

        # Load the starfighter image and get its rect.
        self.image: pygame.Surface = pygame.image.load(image_path)
        self.rect: pygame.rect = self.image.get_rect()

        # Start each new starfighter at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the starfighter's precise horizontal position as a float.
        self.x: float = float(self.rect.x)

        # Movement flags. Used to track continuous movement input.
        self.moving_right: bool = False
        self.moving_left: bool = False

    def update(self) -> None:
        """
        Update the starfighter's position based on the movement flag.

        Ensures that the starfighter remains within the screen boundaries
        while moving left or right.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.starfighter_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.starfighter_speed

        # Update rect object based on the new float position.
        self.rect.x = self.x

    def center_starfighter(self) -> None:
        """
        Center the starfighter at the bottom of the screen.

        This is typically called after the player loses a life or
        when a new game or level begins.
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blit_me(self) -> None:
        """
        Draw the starfighter at its current location on the screen.
        """
        self.screen.blit(self.image, self.rect)
