import pygame
import random

class enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 1
        self.ver = 1
        self.hor = 0
        self.hitbox = (self.x - 25, self.y - 25, 25*3, 25*3)
    
    def move(self, direction):
        if(direction == "left"):
            if (self.hor != 1):
                self.ver = 0
                self.hor = 1
            else:
                self.x -= self.vel
        elif (direction == "right"):
            if (self.hor != -1):
                self.ver = 0
                self.hor = -1
            else:
                self.x += self.vel
        elif (direction == "up"):
            if (self.ver != 1):
                self.ver = 1
                self.hor = 0
            else:
                self.y -= self.vel
        elif (direction == "down"):
            if (self.ver != -1):
                self.ver = -1
                self.hor = 0
            else:
                self.y += self.vel
        self.hitbox = (self.x - 25, self.y - 25, 25*3, 25*3)

    def auto_move(self):
        rand_dir = random.randint(0, 4)

    def draw(self, win):
        auto_move()
        for i in range(-1,2):
            for j in range(-1,2):
                if (((i != self.ver) and (j != self.hor)) and ((i != 0) and (j != 0))):
                    pass
                else:
                    pygame.draw.rect(win, (255, 0, 0), (self.x + j * 25, self.y + i * 25, 25, 25))
        pygame.draw.rect(win, (0, 0, 0), (self.x + self.hor * 25, self.y + self.ver * 25, 25, 25))