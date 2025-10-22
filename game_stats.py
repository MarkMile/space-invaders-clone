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
        self.highscore: int = 0

    def reset_stats(self) -> None:
        """
        Reset statistics that can change during the game.

        This method is called when a new game starts to reset the player's
        starfighter lives, score, and level.
        """
        self.starfighter_left: int = self.settings.starfighter_limit
        self.score: int = 0
        self.level: int = 1
