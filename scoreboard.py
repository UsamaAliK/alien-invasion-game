import pygame.font


class Scoreboard():
  """A class to manage the scoreboard."""
  def __init__(self,ai_settings,screen,stats):
      self.screen = screen
      self.screen_rect = screen.get_rect()
      self.ai_settings = ai_settings
      self.stats = stats
      # font settings for storing information
      self.font_color=(30,30,30)
      self.font = pygame.font.SysFont(None,30)

      # prepare the initial score image

      self.prep_score()
      self.prep_high_score()
      self.prep_level()


  def prep_score(self):
      rounded_score=int(round(self.stats.score,-1))
      score_str="SCORE: {:,}".format(rounded_score)
      self.score_image=self.font.render(score_str,True,self.font_color,self.ai_settings.bg_colours)
      self.score_rect=self.score_image.get_rect()
      self.score_rect.right=self.screen_rect.right-20
      self.score_rect.top=20

  def show_score(self):
      self.screen.blit(self.score_image,self.score_rect)
      self.screen.blit(self.high_score_image,self.high_score_rect)
      self.screen.blit(self.level_image,self.level_rect)


  def prep_high_score(self):
      round_high_score=int(round(self.stats.high_score,-1))
      high_score_str="HIGH SCORE: {:,}".format(round_high_score)
      self.high_score_image=self.font.render(high_score_str,True,self.font_color,self.ai_settings.bg_colours)

      # center the image of high score
      self.high_score_rect = self.high_score_image.get_rect()
      self.high_score_rect.centerx = self.screen_rect.centerx
      self.high_score_rect.top = self.score_rect.top





  def prep_level(self):

   self.level_image=self.font.render("LEVEL: " +str(self.stats.level),True,self.font_color,self.ai_settings.bg_colours)


   self.level_rect=self.level_image.get_rect()
   self.level_rect.right=self.score_rect.right
   self.level_rect.top=self.score_rect.bottom+10



