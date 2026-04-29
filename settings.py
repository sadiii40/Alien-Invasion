from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Asset paths
        self._base_dir = Path(__file__).parent
        self._images_dir = self._base_dir / "Assets" / "images" 
        self.ship_image_path = self._images_dir / "ship.png"
        self.laser_image_path = self._images_dir / "laser.png"
        self.bg_image_path = self._images_dir / "background.png"
        self.alien_image_path = self._images_dir / "alien.png"
        #Ship settings
        self.ship_speed = 1.5
        self._fonts_dir = self._base_dir / "Assets" / "Fonts"
        self.font_path = self._fonts_dir / "Boogaloo-Regular.ttf"
        self.play_button_image_path = self._images_dir / "play_button.png"
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10