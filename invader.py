from __future__ import annotations  # Postpone type hint evaluation

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING, List

# To avoid circular imports during runtime
if TYPE_CHECKING:
    from config import GameConfiguration
    from space_invaders import SpaceInvaders


class Invader(Sprite):
    """Reprepresents a single invader in the fleet."""

    def __init__(
        self, game_instance: SpaceInvaders, frame_one: str, frame_two: str) -> None:
        """
        Initialize the invader and set its starting position.
        
        Args:
            game_instance (SpaceInvaders): The current game instance, providing
            access to the screen and settings.
            frame_one (str): File path to the first frame of the invader animation.
            frame_two (str): File path to the second frame of the invader animation.
        """
        super().__init__()
        self.screen: pygame.Surface = game_instance.screen
        self.settings: GameConfiguration = game_instance.settings

        # List storing two frames for the invader animation.
        self.invader_frames: List[pygame.Surface] = []
        self.current_sprite: int = 0

        # Append the frame to the invader_frames list to use for animation.
        self.invader_frames.append(pygame.image.load(frame_one))
        self.invader_frames.append(pygame.image.load(frame_two))

        # Load invader frame depending on the current_sprite variable and set the rect.
        self.image: pygame.Surface = self.invader_frames[self.current_sprite]
        self.rect: pygame.Rect = self.image.get_rect()

        # Start each new invader near the top-left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the invader's precise horisontal position as a float.
        self.x: float = float(self.rect.x)

    def update(self) -> None:
        """
        Move the invader horizontally based on the fleet direction and animate it.
        """
        self.x += self.settings.invader_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.animate_invader()

    def check_edges(self) -> bool:
        """
        Check wheter the invader is at the edge of the screen.

        Returns:
            bool: True if the invader is at the screen edge, False otherwise.
        """
        screen_rect: pygame.Rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def animate_invader(self) -> None:
        """
        Animate the invader by cycling through its frames at a controlled speed.
        """
        # # Control the animation (lower value = slower animation).
        self.current_sprite += 0.02

        # Reset frame index when the end is reached.
        if self.current_sprite >= len(self.invader_frames):
            self.current_sprite = 0

        # Update the displayed frame.
        self.image: pygame.Surface = self.invader_frames[int(self.current_sprite)]
