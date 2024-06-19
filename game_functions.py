import sys
import pygame
from bullets import bullet
from Alien import alien


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


def updating_screen(ai_setting,screen,ship,bullets,Aliens):

    screen.fill(ai_setting.bg_colours)
    for bullet in bullets.sprites():
        bullet.drwa_bullet()
    ship.blitme()
    Aliens.draw(screen)

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


def get_alien_num(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width

    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_settings,ship_height,alien_height):

    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows




def create_alien(ai_settings,screen,aliens,alien_num,row_num):

    Alien = alien(ai_settings, screen)
    alien_width = Alien.rect.width
    Alien.x = alien_width + 2 * alien_width * alien_num

    Alien.rect.x = Alien.x
    Alien.rect.y=Alien.rect.height+2*Alien.rect.height*row_num
    aliens.add(Alien)


def create_fleet(ai_settings,screen,ship,aliens):

    Alien=alien(ai_settings,screen)
    number_alien_x=get_alien_num(ai_settings,Alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,Alien.rect.height)
    for row_num in range(number_rows):
     for alien_num in range(number_alien_x):
        create_alien(ai_settings,screen,aliens,alien_num,row_num)



def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1



def update_aliens(ai_settings,aliens):
    aliens.update()
    check_fleet_edges(ai_settings,aliens)


