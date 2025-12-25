# game_stats.py
# A module defining the GameStats class for tracking game statistics in the Space Invaders game.

from __future__ import annotations  # Postpone type hint evaluation

from typing import TYPE_CHECKING

# To avoid circular imports during runtime
if TYPE_CHECKING:
    from space_invaders import SpaceInvaders
    from config import GameConfiguration


class GameStats:
    """Track statistics for Space Invaders."""

    def __init__(self, game_instance: SpaceInvaders) -> None:
        """
        Initialize game statistics and settings reference.

        Args:
            game_instance (SpaceInvaders): The current game instance, providing
            access to the game settings.
        """
        self.settings: GameConfiguration = game_instance.settings
        self.reset_stats()

        # High score persists across game sessions.
        self.highscore = 0

    def reset_stats(self) -> None:
        """
        Reset statistics that can change during the game (Called when starting a new game.).
        """
        self.starfighter_left: int = self.settings.starfighter_limit
        self.score = 0
        self.level = 1
