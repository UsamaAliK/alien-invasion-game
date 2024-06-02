import pygame
class Ship():


    def __init__(self,ai_settings,screen):
        #initialize the ship and set its starting position
        self.screen=screen
        self.ai_settings=ai_settings

        #load the ship image and get it in rect form
        self.image=pygame.image.load('ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #start each new ship at the bottom of the screen
        self.rect.centerx=self.screen_rect.centerx # x_attribute of ship
        self.rect.bottom=self.screen_rect.bottom # y_attribute of ship
        self.center = float(self.rect.centerx)
        self.moving_R_flag=False
        self.moving_L_flag=False
    def update(self):
        if self.moving_R_flag and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_L_flag and self.rect.left > 0 :
            self.center-=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center
    def blitme(self):

         #draaw the ship at its current loaction
         self.screen.blit(self.image,self.rect)
