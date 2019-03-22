import sys
import pygame
from settings import Settings
from ship import Ship
from character import Character

import game_functions as gf

def run_game():
    #Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)
    name = input("Please give your name: ")
    char = Character(name, screen)

    #Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
            # Make the most recently drawn screen visible.
        # Redraw the screen during each iteration
        gf.update_screen(ai_settings,screen,ship, char)

run_game()