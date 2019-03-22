import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # some kind of key has been pressed
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP: # some kind of key has been released
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship, char):
    """Update images on the screen and flip to the new screen. """
    screen.fill(ai_settings.bg_color)
    # Redraw the screen during each pass through the loop.
    ship.blitme()
    char.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()