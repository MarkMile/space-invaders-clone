# config.py
# A module defining the GameConfiguration class for storing game settings in the Space Invaders game.

import pygame
from typing import Tuple


class GameConfiguration:
    """A class to store all settings for Space Invaders."""

    def __init__(self) -> None:
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (19, 19, 19)
        self.game_icon = pygame.image.load("images/game_icon.png")
        self.bg_image = pygame.image.load("images/background_image.png")

        # Starfighter settings
        self.starfighter_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 3

        # Invader settings
        self.fleet_drop_speed = 10

        # Invader image dimensions
        self.invaders_png_width = 60
        self.invaders_png_height = 44

        # Game progress settings
        self.speedup_scale = 1.1  # How quickly the game speeds up
        self.score_scale = 1.5  # How quickly the invaders point values increase

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change throughout the game."""
        self.starfighter_speed = 3.5
        self.bullet_speed = 9.0
        self.invader_speed = 2.0

        # Scoring
        self.invader_points = 50

        # Fleet direction: 1 for right, -1 for left.
        self.fleet_direction = 1

    def increase_speed(self) -> None:
        """
        Increase speed settings and invader point values.
        This method is called to make the game progressively harder.
        """
        self.starfighter_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.invader_speed *= self.speedup_scale

        self.invader_points = int(self.invader_points * self.score_scale)
