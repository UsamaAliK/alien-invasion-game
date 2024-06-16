import sys

import bullets
import pygame
from bullets import bullet



def check_Keydown_events(event,ship,ai_settings,screen,bullets):


        if event.key==pygame.K_RIGHT:
                ship.moving_R_flag=True

        elif event.key==pygame.K_LEFT:
                ship.moving_L_flag=True

        elif event.key==pygame.K_SPACE:
           fire_bullets(ai_settings,screen,ship,bullets)
def check_KeyUP_events(event,ship):


    if event.key==pygame.K_RIGHT:
            ship.moving_R_flag=False

    elif event.key==pygame.K_LEFT:
             ship.moving_L_flag=False
def check_events(ai_settings,screen,ship,bullets):


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
             check_Keydown_events(event,ship,ai_settings,screen,bullets)

        elif event.type==pygame.KEYUP:
           check_KeyUP_events(event,ship)
def updating_screen(ai_setting,screen,ship,bullets):


    screen.fill(ai_setting.bg_colours)
    for bullet in bullets.sprites():
        bullet.drwa_bullet()
    ship.blitme()
    pygame.display.flip()
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
def fire_bullets(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullets=bullet(ai_settings,screen,ship)
        bullets.add(new_bullets)