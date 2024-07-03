class settings():
    def __init__(self):
        """initialize game settings"""
        # screen settings
        self.screen_width=(1200)
        self.screen_height=(800)
        self.bg_colours=(230,230,230)
        # ship speed
        self.ship_limit=3
        # Bullet settings
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed=6
        self.fleet_drop_speed=150


        self.speed_scale= 1.1
        self.score_scale= 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        self.ship_speed_factor=3
        self.bullet_speed_factor=5

        self.alien_speed_factor=1

        # 1 represent right and -1 represent left
        self.fleet_direction=1
        self.alien_points=50
    def increase_speed(self):
        self.ship_speed_factor*=self.speed_scale
        self.bullet_speed_factor*=self.speed_scale
        self.alien_speed_factor*=self.speed_scale
        self.alien_points=int(self.alien_points*self.score_scale)


