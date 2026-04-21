import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an alien."""

    def __init__(self, ai_game):
        """Initialize the alien and its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the image
        self.image = pygame.image.load(
            self.settings.alien_image_path).convert_alpha()
        self.rect = self.image.get_rect()
        
        #start near the right edge
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        """Move the alien down"""
        self.rect.x -= self.settings.alien_speed