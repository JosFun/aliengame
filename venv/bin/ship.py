import pygame
from settings import Settings

class Ship():
    def __init__(self, screen, ai_settings):
        """Initialize the ship and set its starting position."""
        self.screen = screen # Draw the ship on the specified screen

        self.ai_settings = ai_settings

        # Load the ship's image and get its rect
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Since we want to work with float values when it comes to the ship's velocity and rect.centerx is an integer, we have to do the following:
        self.centerx = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags"""
        if self.moving_right == True:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left == True:
            self.centerx -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
