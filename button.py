import pygame

class Button:
    """A class to build a play button."""
    
    def __init__(self, ai_game):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        #load the custom play button image
        self.image = pygame.image.load(
            self.settings.play_button_image_path).convert_alpha()
        self.rect = self.image.get_rect()

        #center the button on screen
        self.rect.center = self.screen_rect.center

    def draw_button(self):
        """"Draw botton to screen"""
        self.screen.blit(self.image, self.rect)
