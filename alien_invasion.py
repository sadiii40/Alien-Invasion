"""
Program: Alien Invasion - Track 2
Author: Sadikshya Chalise
Purpose:  Custom Alien Invasion game where a ship on the left edge moves up and down firing horizontal laser bullets.
Starter: https://github.com/RedBeard41/alien_Invasion_starter
        and, guided by the textbook, Python Crash Course
Date: 04/13/2026
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        """Initialize the game, and create resources"""
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Load and scale background image
        self.bg_image = pygame.image.load(
            self.settings.bg_image_path).convert()
        self.bg_image = pygame.transform.scale(
            self.bg_image,
            (self.settings.screen_width, self.settings.screen_height))

        # Create ship and bullets group
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """The main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypress"""
        #move up or down
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        #fire bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        #quit
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the group"""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()
        # remove bullets that go off the right edge
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)


    def _create_fleet(self):
        """Create a fleet of aliens"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        #pattern - 5 rows
        for row in range(5):
            for col in range(row + 1):
                alien = Alien(self)
                alien.rect.x = (self.settings.screen_width -
                    alien_width * 2) - (col * alien_width * 2)
                alien.rect.y = (row * alien_height * 2) + alien_height
                alien.y = float(alien.rect.y)
                print(f"Alien at x={alien.rect.x}, y={alien.rect.y}")  # add here
                self.aliens.add(alien)
            
    def _update_aliens(self):
        """Update positions of all aliens and check collision"""
        self.aliens.update()

        #bullet and alien collision
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        #alien and ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!")

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        #draw background
        self.screen.blit(self.bg_image, (0, 0))        #draw bullets and ship
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

# AI Disclosure: Drafted myself and polished using AI