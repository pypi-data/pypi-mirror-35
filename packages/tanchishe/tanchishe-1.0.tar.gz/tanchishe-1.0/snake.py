import pygame
from pygame.locals import *

class My_Snake(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('图片/滑稽.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = ((self.width - self.rect.width) // 2),\
                                          ((self.height - self.rect.height) // 2)
        self.speed = [0, -15]
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]
        
        if self.rect.left > self.width:
            self.rect.left = 0
        elif self.rect.right < 0:
            self.rect.right = self.width
        elif self.rect.top > self.height:
            self.rect.top = 0 
        elif self.rect.bottom < 0:
            self.rect.bottom = self.height

    def moveUp(self):
        if self.speed[0]:
            self.speed = [0, -15]
            if self.speed[0] > 0:
                self.image = pygame.transform.rotate(self.image, 90)#有问题
                #self.image = pygame.transform.flip(self.image, False, True) 
            else:
                self.image = pygame.transform.rotate(self.image, -90)

    def moveDown(self):
        if self.speed[0]:
            self.speed = [0, 15]
            if self.speed[0] > 0:
                self.image = pygame.transform.rotate(self.image, -90)#有问题
            else:
                self.image = pygame.transform.rotate(self.image, 90)
 
    def moveLeft(self):
        if self.speed[1]:
            self.speed = [-15, 0]
            if self.speed[1] > 0:
                self.image = pygame.transform.rotate(self.image, -90)#有问题
            else:
                self.image = pygame.transform.rotate(self.image, 90)

    def moveRight(self):
        if self.speed[1]:
            self.speed = [15, 0]
            if self.speed[1] > 0:
                self.image = pygame.transform.rotate(self.image, 90)#有问题
            else:
                self.image = pygame.transform.rotate(self.image, -90)

class Snake(pygame.sprite.Sprite):
    def __init__(self, bg_size, last_rect, last_speed):
        pygame.sprite.Sprite.__init__(self)

        self.last_rect = last_rect
        self.last_speed = last_speed
        self.image = pygame.image.load('图片/滑稽1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]

        if self.last_speed[0] < 0:
            self.rect.left, self.rect.top = (self.last_rect.left + 15), self.last_rect.top
        elif self.last_speed[0] > 0:
            self.rect.left, self.rect.top = (self.last_rect.left - 15), self.last_rect.top

        if self.last_speed[1] < 0:
            self.rect.left, self.rect.top = self.last_rect.left, (self.last_rect.top + 15)
        elif self.last_speed[1] > 0:
            self.rect.left, self.rect.top = self.last_rect.left, (self.last_rect.top - 15)
            
        self.speed = self.last_speed
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]

        if self.rect.left > self.width:
            self.rect.left = 0
        elif self.rect.right < 0:
            self.rect.right = self.width
        elif self.rect.top > self.height:
            self.rect.top = 0 
        elif self.rect.bottom < 0:
            self.rect.bottom = self.height



        


        
