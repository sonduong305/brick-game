import pygame

class projectile(object):
    def __init__(self,x,y,radius,color, hor, ver):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.hor = hor
        self.ver = ver
        self.vel = 4

    def draw(self,win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)