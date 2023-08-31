import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    
    #Initializing the Pygame module, Settings class and creen object.
    pygame.init()
    ai_settings=Settings()

    screen=pygame.display.set_mode( (ai_settings.screen_width,ai_settings.screen_height) )

    pygame.display.set_caption("Alien Invasion Game! -Amey")

    # Make the Play button
    play_button = Button(ai_settings, screen, "Play")

    #Create an object to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Making a ship
    ship=Ship(ai_settings, screen)

    #Making an Alien
    alien=Alien(ai_settings=ai_settings, screen=screen)

    #Making a group to store bullets in.
    bullets=Group()

    #Making a group to store aliens in.
    aliens=Group()

    #Create the fleet of Aliens.
    gf.create_fleet(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens)
    
    #Creating the main game Loop
    while True:

        if not stats.game_active:
            play_button.draw_button()
        
        #Tracking Keyboard and Mouse movement
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings=ai_settings, screen=screen, stats=stats, sb=sb, ship=ship, aliens=aliens, bullets=bullets)
            gf.update_aliens(ai_settings=ai_settings, stats=stats, screen=screen, sb=sb, ship=ship, aliens=aliens, bullets=bullets)

        else:
            play_button.draw_button()
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        #The below calls are added just so that it can avoid any stuttering or flickering while displaying, as i have noticed it happen in my code 
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        aliens.draw(screen)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        sb.show_score()

        pygame.display.flip()

    
run_game()