class Settings():
    """Settings for alien invasion game"""

    def __init__(self):
        self.width = 1280
        self.height = 800
        self.rgb_colors = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3
