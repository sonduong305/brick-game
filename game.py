import pygame
from player import player
from enemy import enemy
from projectile import projectile
from config import config

pygame.init()

win_size = config.size
win = pygame.display.set_mode(win_size)

pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

def redrawGameWindow():
    pygame.draw.rect(win, (0, 0, 0), (0, 0, win_size[0], win_size[1]))
    man.draw(win)
    for goblin in enemies:
        goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()




run = True
man = player(12,12)
enemies = []
enemies = [enemy(50,50), enemy(50,450), enemy(800,50)]
shoot_loop = 0
bullets = []
while run:
    clock.tick(60)

    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 5:
        shoot_loop = 0

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        for goblin in enemies:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    bullets.pop(bullets.index(bullet))

        if bullet.x < win_size[0] and bullet.x > 0 and  bullet.y < win_size[1] and bullet.y > 0:
            bullet.x -= bullet.vel * bullet.hor
            bullet.y -= bullet.vel * bullet.ver
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_SPACE] and shoot_loop == 0 :
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x - man.hor * 25 + 12.5), round(man.y - man.ver * 25 + 12.5), 6, (255,255,255), man.hor, man.ver))
            shoot_loop = 1

    if keys[pygame.K_LEFT]:
        man.move("left")

    elif keys[pygame.K_RIGHT]:
        man.move("right")

    elif keys[pygame.K_UP]:
        man.move("up")
        
    elif keys[pygame.K_DOWN]:
        man.move("down")


    redrawGameWindow()
pygame.quit()