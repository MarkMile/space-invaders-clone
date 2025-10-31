from __future__ import annotations  # Postpone type hint evaluation

import pygame.font
from pygame.sprite import Group
from starfighter import Starfighter
from typing import TYPE_CHECKING, Tuple

# To avoid circular imports during runtime
if TYPE_CHECKING:
    from game_stats import GameStats
    from config import GameConfiguration
    from space_invaders import SpaceInvaders


class Scoreboard:
    """Display and manage scoring information for Space Invaders."""

    def __init__(self, game_instance: SpaceInvaders) -> None:
        """
        Initialize scorekeeping attributes and prepare score displays.

        Args:
            game_instance (SpaceInvaders): The current game instance, providing
            access to the screen, settings, and game statistics.
        """
        self.game: SpaceInvaders = game_instance
        self.screen: pygame.Surface = game_instance.screen
        self.screen_rect: pygame.rect = game_instance.screen.get_rect()
        self.settings: GameConfiguration = game_instance.settings
        self.stats: GameStats = game_instance.game_stats

        # Font and color settings for score and level elements.
        self.font_color: Tuple[int, int, int] = (255, 255, 255)
        self.stage_font: pygame.font.Font = pygame.font.Font("font/RetroGaming.ttf", 20)
        self.score_font: pygame.font.Font = pygame.font.Font("font/RetroGaming.ttf", 35)
        self.highscore_font: pygame.font.Font = pygame.font.Font(
            "font/RetroGaming.ttf", 22
        )

        # Prepare the intial rendered images.
        self.prepare_player_score()
        self.prepare_highscore()
        self.prepare_stage()
        self.prep_starfighters_left()

    def prepare_player_score(self) -> None:
        """
        Render the current score as an image and position it on the screen.
        """
        rounded_score: int = round(self.stats.score, -1)
        score_str: str = f"{rounded_score:,}"
        self.player_score_img: pygame.Surface = self.score_font.render(
            score_str, True, self.font_color, self.settings.bg_color
        )

        # Display the score at the top-right corner of the screen.
        self.player_score_rect: pygame.Rect = self.player_score_img.get_rect()
        self.player_score_rect.right = self.screen_rect.right - 20
        self.player_score_rect.top = 20

    def show_scores(self) -> None:
        """
        Draw all scoring elements to the screen, including score, high score,
        level, and remaining starfighters.
        """
        self.screen.blit(self.stage_image, self.stage_rect)
        self.screen.blit(self.player_score_img, self.player_score_rect)
        self.screen.blit(self.highscore_img, self.highscore_rect)
        self.starfighters.draw(self.screen)

    def prepare_highscore(self) -> None:
        """
        Render the high score as an image and center it at the top of the screen.
        """
        highscore: int = round(self.stats.highscore, -1)
        highscore_str: str = f"highscore: {highscore:,}"
        self.highscore_img: pygame.Surface = self.highscore_font.render(
            highscore_str, True, self.font_color, self.settings.bg_color
        )

        # Center the high score near the top of the screen.
        self.highscore_rect: pygame.Rect = self.highscore_img.get_rect()
        self.highscore_rect.center = self.screen_rect.center
        self.highscore_rect.top = self.player_score_rect.top - 5

    def check_highscore(self) -> None:
        """
        Check wheter the current score exceeds the high score.
        If so, update the high score and re-render its image.
        """
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prepare_highscore()

    def prepare_stage(self) -> None:
        """
        Render the current level as an image and position it below the high score.
        """
        stage_str: str = f"stage {self.stats.level}"
        self.stage_image: pygame.Surface = self.stage_font.render(
            stage_str, True, self.font_color, self.settings.bg_color
        )

        # Position the stage text below the high score.
        self.stage_rect: pygame.Rect = self.stage_image.get_rect()
        self.stage_rect.center = self.screen_rect.center
        self.stage_rect.top = self.highscore_rect.bottom + 5

    def prep_starfighters_left(self) -> None:
        """
        Display the remaining starfighters as icons at the top-left corner of the screen.
        """
        self.starfighters: pygame.sprite.Group = Group()
        for starfighter_number in range(self.stats.starfighter_left):
            starfighter = Starfighter(self.game, "images/ships_left.png")
            starfighter.rect.x = 20 + starfighter_number * (starfighter.rect.width + 10)
            starfighter.rect.y = self.highscore_rect.top
            self.starfighters.add(starfighter)
