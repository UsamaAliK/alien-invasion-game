class settings():
    def __init__(self):
        """initialize game settings"""
        # screen settings
        self.screen_width=(1200)
        self.screen_height=(800)
        self.bg_colours=(230,230,230)
        # ship speed
        self.ship_speed_factor=1.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed=6
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        # 1 represent right and -1 represent left
        self.fleet_direction=1