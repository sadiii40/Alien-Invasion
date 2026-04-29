class GameStats:
    """Track statistics"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #no reset for highscore
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change"""
        self.ships_left = 3
        self.score = 0