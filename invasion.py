from settings import settings
from pygame.sprite import Group
import game_functions as gf
from ship import Ship
import pygame
from game_stats import GameStats
from button import Button


def run_game():
   pygame.init()
   ai_settings=settings()



   screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
   pygame.display.set_caption("Alien invasion")
   play_button=Button(ai_settings,screen,'PLAY!')
   stats=GameStats(ai_settings)
   ship = Ship(ai_settings,screen)
   bullets=Group()
   Aliens=Group()
   gf.create_fleet(ai_settings,screen,ship,Aliens)


   while True:
       gf.check_events(ai_settings,screen,stats,play_button,ship,Aliens,bullets)
       if stats.game_active:
         ship.update()
         gf.update_bullets(ai_settings,screen,ship,Aliens,bullets)
         gf.update_aliens(ai_settings,stats,screen,ship,Aliens,bullets)
       gf.updating_screen(ai_settings,screen,stats,ship,bullets,Aliens,play_button)

run_game()

