import pygame
import random
from config import config

class enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 1
        self.ver = 1
        self.hor = 0
        self.hitbox = (self.x - 25, self.y - 25, 25*3, 25*3)
        self.direction = ['left', 'right', 'up', 'down']
        self.current_direction = 3
        self.visible = True

    def hit(self):
        self.visible = False
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

    def auto_move(self):
        rand_dir = random.randint(0, 100)
        if (rand_dir < 4):
            self.move(self.direction[rand_dir])
            self.current_direction = rand_dir
        else:
            self.move(self.direction[self.current_direction])

    def draw(self, win):
        if self.visible:
            self.auto_move()
            for i in range(-1,2):
                for j in range(-1,2):
                    if (((i != self.ver) and (j != self.hor)) and ((i != 0) and (j != 0))):
                        pass
                    else:
                        pygame.draw.rect(win, (255, 0, 0), (self.x + j * 25, self.y + i * 25, 25, 25))
            pygame.draw.rect(win, (0, 0, 0), (self.x + self.hor * 25, self.y + self.ver * 25, 25, 25))