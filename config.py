import pygame
from typing import Tuple

class GameConfiguration:
    """A class to store all settings for Space Invaders."""

    def __init__(self) -> None:
        """
        Initialize static game settings, including screen, starfighter,
        bullet, and invader settings.
        """
        # Screen settings
        self.screen_width: int = 1200
        self.screen_height: int = 800
        self.bg_color: Tuple[int, int, int] = (19, 19, 19)
        self.bg_image: pygame.Surface = pygame.image.load('images/background_image.png')

        # Starfighter settings
        self.starfighter_limit: int = 3

        # Bullet settings
        self.bullet_width: int = 5
        self.bullet_height: int = 20
        self.bullet_color: Tuple[int, int, int] = (200, 200, 200)
        self.bullets_allowed: int = 3

        # Invader settings
        self.fleet_drop_speed: int = 10

        # Invader image dimensions
        self.invaders_png_width: int = 60
        self.invaders_png_height: int = 44

        # Game progress settings
        self.speedup_scale: float = 1.1  # How quickly the game speeds up
        self.score_scale: float = 1.5    # How quickly the invader's point values increase

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """
        Initialize settings that change during the game, such as movement
        speeds and scoring.
        """
        self.starfighter_speed: float = 3.5
        self.bullet_speed: float = 9.0
        self.invader_speed: float = 2.0

        # Scoring
        self.invader_points: int = 50

        # Fleet direction: 1 for right, -1 for left.
        self.fleet_direction: int = 1

    def increase_speed(self) -> None:
        """
        Increase game speed and invader point values to make the gameplay 
        progressively harder.
        """
        self.starfighter_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.invader_speed *= self.speedup_scale

        self.invader_points: int = int(self.invader_points * self.score_scale)
