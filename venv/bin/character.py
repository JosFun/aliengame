import pygame

IMG_PATH = "idle.png"

class Character():
    def __init__(self, name, screen):
        self.__name = name
        self.screen = screen

        self.image = pygame.image.load(IMG_PATH)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set the character's mid to the screen's mid
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.name