import pygame
from config import config

class player(object):
    def __init__(self, x, y):
        self.x = x*20
        self.y = y*20
        self.vel = 1.5
        self.ver = 1
        self.hor = 0
        self.hitbox = (self.x - 25, self.y - 25, 25*3, 25*3)
    
    def move(self, direction):
        if(direction == "left"):
            if (self.hor != 1):
                self.ver = 0
                self.hor = 1
            elif (self.x > 25):
                self.x -= self.vel
        elif (direction == "right"):
            if (self.hor != -1):
                self.ver = 0
                self.hor = -1
            elif (self.x < config.size[0] - 50):
                self.x += self.vel
        elif (direction == "up"):
            if (self.ver != 1):
                self.ver = 1
                self.hor = 0
            elif (self.y > 25):
                self.y -= self.vel
        elif (direction == "down"):
            if (self.ver != -1):
                self.ver = -1
                self.hor = 0
            elif (self.y < config.size[1] - 50):
                self.y += self.vel
        self.hitbox = (self.x - 25, self.y - 25, 25*3, 25*3)

    def draw(self, win):
        for i in range(-1,2):
            for j in range(-1,2):
                if (((i != self.ver) and (j != self.hor)) and ((i != 0) and (j != 0))):
                    pass
                else:
                    pygame.draw.rect(win, (0, 255, 255), (self.x + j * 25, self.y + i * 25, 25, 25))
