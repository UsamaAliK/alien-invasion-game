import pygame
from pygame.sprite import Sprite

class bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        # create a bullet object at ship's current position
        super(bullet,self).__init__()
        self.screen=screen

        # create a bullet rect at (0,0) then positioning it
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top= ship.rect.top

        #  store the bullet position as decimal value
        self.y=float(self.rect.y)

        # giving colours to bullets
        self.colour=ai_settings.bullet_color

        # speed of bullet
        self.speed_factor=ai_settings.bullet_speed_factor
    def update(self):
        # move the bullet up the screen

         # update the decimal position of bullet
        self.y-=self.speed_factor
        # update the bullet position
        self.rect.y=self.y
    def drwa_bullet(self):

         # draw the bullet to the screen

         pygame.draw.rect(self.screen,self.colour,self.rect)

