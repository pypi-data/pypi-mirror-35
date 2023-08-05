import pygame
from random import *

class Food(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = []
        self.image.extend([pygame.image.load('图片/食物1.png').convert_alpha(),\
                           pygame.image.load('图片/食物2.png').convert_alpha(),\
                           pygame.image.load('图片/食物3.png').convert_alpha(),\
                           pygame.image.load('图片/食物4.png').convert_alpha(),\
                           ])
        self.rect = self.image[1].get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.rect.left, self.rect.top = randint(10, self.width - 10), \
                                        randint(10, self.height - 10)    
        self.mask = pygame.mask.from_surface(self.image[3])

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = randint(10, self.width - 10), \
                                        randint(10, self.height - 10)
