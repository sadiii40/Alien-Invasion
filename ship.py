import pygame
class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image
        # Load ship image
        self.image = pygame.image.load(self.settings.ship_image_path).convert()
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        #start at left edge
        self.rect.midleft = self.screen_rect.midleft

        #store float for vertical position
        self.y = float(self.rect.y)

        #movement
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement"""

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect) 