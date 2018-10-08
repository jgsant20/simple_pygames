class Settings:
    """Settings for game_character"""

    def __init__(self):
        self.width = 1280
        self.height = 720
        self.rgb_colors = (10, 10, 10)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_width = 2
        self.bullet_height = 5
        self.bullet_speed = 2
        self.bullet_rgb = (255, 255, 255)