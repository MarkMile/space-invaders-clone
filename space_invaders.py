import pygame
from sys import exit
from time import sleep
from typing import Tuple

from bullet import Bullet
from invader import Invader
from button_ui import Button
from game_stats import GameStats
from starfighter import Starfighter
from scoreboard_ui import Scoreboard
from config import GameConfiguration


class SpaceInvaders:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """
        Initialize the game, and create game resources.

        This sets up the display, initializes pygame, creates the game settings,
        statistics, scoreboard, and initializes all major game objects such as
        the player's starfighter, bullet group, and invaders fleet.
        """
        pygame.init()
        self.settings: GameConfiguration = GameConfiguration()
        self.clock: pygame.time.Clock = pygame.time.Clock()

        # Main display surface for the game window.
        self.screen: pygame.Surface = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Space Invaders Clone")

        # Start Space Invaders in an active state until the player starts the game.
        self.game_is_active: bool = False

        # Button that starts a new game when clicked.
        self.play_button: Button = Button(self, "play")

        # Game statistics and scoreboard setup.
        self.stats: GameStats = GameStats(self)
        self.score_board: Scoreboard = Scoreboard(self)

        # Player's starfighter and sprite groups for bullets and invaders.
        self.starfighter: Starfighter = Starfighter(self, "images/starfighter.png")
        self.bullets: pygame.sprite.Group = pygame.sprite.Group()
        self.invaders: pygame.sprite.Group = pygame.sprite.Group()

        # Create the initial fleet of invaders.
        self.create_invaders_fleet()

    def run_the_game(self) -> None:
        """
        Start the main loop for the Space Invaders game.

        This continuosly checks for user input, updates game elements (starfighter, bullets, invaders),
        and refreshes the screen at a consistent frame rate.
        """
        while True:
            self.check_events()

            if self.game_is_active:
                self.starfighter.update()
                self.update_bullets()
                self.update_invaders()

            self.update_screen()
            self.clock.tick(60)

    def update_screen(self) -> None:
        """
        Update images on the screen, and flip to the new screen.

        Draws all active game elements including the starfighter, bullets, invaders,
        scoreboard, and play button (if the game is inactive).
        """
        self.screen.blit(self.settings.bg_image, (0, 0))

        # Draw bullets.
        for bullet in self.bullets:
            bullet.draw_bullet()

        # Draw the starfighter.
        self.starfighter.blit_me()

        # Draw the invaders if the game is active.
        if self.game_is_active:
            self.invaders.draw(self.screen)

        # Draw the score information.
        self.score_board.show_scores()

        # Draw the play button if the game is inactive.
        if not self.game_is_active:
            self.play_button.draw_button()

        # Display the most recently drawn screen.
        pygame.display.flip()

    def check_events(self) -> None:
        """
        Respond to keypresses and mouse events.

        Handles player input such as quitting the game, moving the starfighter,
        firing bullets, and clicking the play button.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_keydown_events(self, event: pygame.event.Event) -> None:
        """
        Respond to keypress event.

        Handless movement keys (left/right), quitting the game ('q'),
        and firing bullets (spacebar).

        Args:
            event (pygame.event.Event): The event object representing the keypress.
        """
        if event.key == pygame.K_RIGHT:
            self.starfighter.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.starfighter.moving_left = True

        elif event.key == pygame.K_q:
            pygame.quit()
            exit()

        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup_events(self, event: pygame.event.Event) -> None:
        """
        Respond to key release events.

        Stops starfighter movement when the left or right arrow keys are released.

        Args:
            event (pygame.event.Event): The event object representing the key release.
        """
        if event.key == pygame.K_RIGHT:
            self.starfighter.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.starfighter.moving_left = False

    def check_play_button(self, mouse_pos: Tuple[int, int]) -> None:
        """
        Start a new game when the player clicks the Play button.

        Args:
            mouse_pos (Tuple[int, int]): The (x, y) position of the mouse
        """
        button_clicked: bool = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_is_active:
            # Reset the game statistics.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.score_board.prepare_player_score()
            self.score_board.prepare_stage()
            self.score_board.prep_starfighters_left()
            self.game_is_active = True

            # Clear old bullets and invaders.
            self.bullets.empty()
            self.invaders.empty()

            # Create a new fleet and center the starfighter.
            self.create_invaders_fleet()
            self.starfighter.center_starfighter()

            # Hide the mouse cursor during gameplay.
            pygame.mouse.set_visible(False)

    def load_invader_image(self, row_number: int) -> Invader:
        """
        Return an Invader instance with an image based on its row position.

        Args:
            row_number (int): The current row number of the invader.

        Returns:
            Invader: An instance of the Invader class with the appropriate image.
        """
        if row_number == 0:
            return Invader(
                self, "images/invader1_frame1.png", "images/invader1_frame2.png"
            )

        elif row_number == 1 or row_number == 2:
            return Invader(
                self, "images/invader2_frame1.png", "images/invader2_frame2.png"
            )

        else:
            return Invader(
                self, "images/invader3_frame1.png", "images/invader3_frame2.png"
            )

    def create_invader(self, current_x: int, current_y: int, row_number: int) -> None:
        """
        Create an invader and add it to the fleed at a specified position.

        Args:
            current_x (int): The x-coordinate for the invader's position.
            current_y (int): The y-coordinate for the invader's position.
            row_number (int): The current row number of the invader.
        """
        new_invader: Invader = self.load_invader_image(row_number)
        new_invader.x = current_x
        new_invader.rect.x = current_x
        new_invader.rect.y = current_y

        # Add the new invader to the invaders group.
        self.invaders.add(new_invader)

    def create_invaders_fleet(self) -> None:
        """
        Create a fleet of invaders on the screen.

        This medhod positions multiple rows of invaders evenly spaced across
        the screen. The number of rows and spacing depend on the configured
        invaders width, height and screen dimensions.
        """
        invaders_width: int = self.settings.invaders_png_width
        invaders_height: int = self.settings.invaders_png_height

        current_x: int = invaders_width
        current_y: int = 2 * invaders_height
        for row in range(5):
            while current_x < (self.settings.screen_width - 2 * invaders_width):
                self.create_invader(current_x, current_y, row)
                current_x += 2 * invaders_width

            # Finished a row. Reset x value, and increment y value.
            current_x = invaders_width
            current_y += 2 * invaders_height

    def check_fleet_edges(self) -> None:
        """
        Check if any invader has reached the edge of the screen and
        respond appropriately by changing the fleet's direction.
        """
        for invader in self.invaders:
            if invader.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self) -> None:
        """
        Drop the entire fleet one level and change the fleet's direction.
        """
        for invader in self.invaders.sprites():
            invader.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def update_invaders(self) -> None:
        """
        Update the positions of all the invaders in the fleet.

        Handles fleet movement, detects collisions between invaders and the starfighter,
        and checks if any invaders have reached the bottom of the screen.
        """
        self.check_fleet_edges()
        self.invaders.update()

        # Check for invader-starfighter collisions.
        if pygame.sprite.spritecollideany(self.starfighter, self.invaders):
            self.is_starfighter_hit()

        # Check for invaders reaching the bottom of the screen.
        self.check_invaders_bottom()

    def fire_bullet(self) -> None:
        """
        Fire a bullet if the limit on bullets has not been reached yet.

        Creates a new bullet and adds it to the bullets group.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self) -> None:
        """
        Update bullet positions and remove bullets that have disappeared.

        Also checks for bullet-invader collisions.
        """
        self.bullets.update()

        # Remove bullets that have gone off the top of the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.check_bullet_invader_collision()

    def check_bullet_invader_collision(self) -> None:
        """
        Handle collisions between bullets and invaders.

        When a bullet hits an invader, both are removed. If all invaders are destroyed,
        a new fleet is created, the game speed increases, and the level is incremented.
        """
        collisions = pygame.sprite.groupcollide(self.bullets, self.invaders, True, True)

        if collisions:
            for invaders in collisions.values():
                self.stats.score += self.settings.invader_points * len(invaders)
            self.score_board.prepare_player_score()
            self.score_board.check_highscore()

        if not self.invaders:
            # All invader destroyed: reset fleet and advance level.
            self.bullets.empty()
            self.create_invaders_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.score_board.prepare_stage()

    def is_starfighter_hit(self) -> None:
        """
        Respond to the player starfighter being hit by an invader.

        If starfighters remain, decrement the count, reset the fleet and starfighter position,
        and pause briefly. If no starfighters remain, end the game.
        """
        if self.stats.starfighter_left > 0:
            # Decrement starfighter_left.
            self.stats.starfighter_left -= 1
            self.score_board.prep_starfighters_left()

            # Remove any remaining bullets and invaders.
            self.bullets.empty()
            self.invaders.empty()

            # Create a new fleet and center the starfighter.
            self.create_invaders_fleet()
            self.starfighter.center_starfighter()

            sleep(1)
        else:
            self.game_is_active = False
            pygame.mouse.set_visible(True)

    def check_invaders_bottom(self) -> None:
        """
        Check if any invaders have reached the bottom of the screen.

        if so, treat it as if the starfighter got hit.
        """
        for invader in self.invaders.sprites():
            if invader.rect.bottom >= self.settings.screen_height:
                self.is_starfighter_hit()
                break


if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = SpaceInvaders()
    game.run_the_game()
