import os
import random
import sys
import time
import pygame


def image_from_url(url):
    try:
        from urllib2 import urlopen
        from cStringIO import StringIO as inout
    except ImportError:
        from urllib.request import urlopen
        from io import BytesIO as inout
    myurl = urlopen(url)
    return inout(myurl.read())


Bug_URL = ('https://wallpapers.com/images/hd/close-up-cockroach-transparent-background-xxe7n3uqepeusxdz.jpg')
Racket_URL = ('https://cdn-icons-png.flaticon.com/512/4881/4881475.png')
Hit_URL = ('https://cdn-icons-png.flaticon.com/512/4881/4881475.png')
Splat_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/Splat_zpsbdf5c74a.png')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK  = (255, 182, 193)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((900, 700), 0, 32)
pygame.display.set_caption('Created with ❤ by Aditya Tripathi')
clock = pygame.time.Clock()
u = True
d = False
level = 2
score = 0
splat_image = pygame.image.load(image_from_url(Splat_URL))
bug = pygame.image.load(image_from_url(Bug_URL))
bug_image = pygame.transform.scale(bug, (85, 70))
Racket = pygame.image.load(image_from_url(Racket_URL))
Racket = pygame.transform.scale(Racket, (200, 200))
Rackethit = pygame.image.load(image_from_url(Hit_URL))
Rackethit = pygame.transform.scale(Rackethit, (250, 250))
myfont = pygame.font.SysFont("Lucida Console", 30)
myfont2 = pygame.font.SysFont("Lucida Console", 100)
myfont3 = pygame.font.SysFont("Comic Sans MS", 80)
place = [(800, 298), (800, 200), (800, 80), (800, 500)]
setplace = random.choice(place)
splt = False
Racket_strike = pygame.transform.rotate(Racket, 180)
label = myfont.render("Play", 1, WHITE)
label4 = myfont.render("Quit", 1, RED)
label3 = myfont2.render("Insect Invasion", 1, PINK)
label2 = myfont2.render("GAME OVER", 1, RED)
i = 255
racket_rect = Racket.get_rect(topleft=(-25, 298))
bug_rect = bug_image.get_rect(topleft=(setplace))
splatrect = splat_image.get_rect()
hit = False
l = False
strike = False
p = False
while True:
    DISPLAYSURF.fill(BLACK)
    key = pygame.key.get_pressed()

    if l and key[pygame.K_UP]:
        racket_rect.y -= level
    if l and key[pygame.K_DOWN]:
        racket_rect.y += level
    if l and key[pygame.K_SPACE]:
        strike = True
        Racket_strike = pygame.transform.rotate(Racket, 290)

        DISPLAYSURF.blit(Racket_strike, racket_rect)
    if not key[pygame.K_SPACE]:
        DISPLAYSURF.blit(Racket, racket_rect)
    DISPLAYSURF.blit(bug_image, bug_rect)

    if p:
        bug_rect.x -= level

    if p == False:
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(label3, (0, 70))
        DISPLAYSURF.blit(label, (420, 550))
        DISPLAYSURF.blit(label4, (420, 580))
        Racket_hit = pygame.transform.rotate(Rackethit, 290)
        DISPLAYSURF.blit(Racket_hit, (250, 200))
        if key[pygame.K_UP]:
            u = True
            d = False
        if u:
            pygame.draw.rect(DISPLAYSURF, WHITE, (410, 550, 90, 30,), 3)
            if key[pygame.K_RETURN]:
                p = True
                l = True

        if key[pygame.K_DOWN]:
            d = True
            u = False
        if d:
            pygame.draw.rect(DISPLAYSURF, RED, (410, 580, 90, 30,), 3)
            if key[pygame.K_RETURN]:
                pygame.quit()

    if key[pygame.K_SPACE] and racket_rect.colliderect(bug_rect) and l:
        splt = True
        place = [(800, 500), (800, 80), (800, 200), (800, 298)]
        setplace = random.choice(place)
        bug_rect = bug_image.get_rect(topleft=(setplace))
        DISPLAYSURF.blit(bug_image, bug_rect)
        level += 0.5
        score += 1
        Racket_hit = pygame.transform.rotate(Rackethit, 290)
        DISPLAYSURF.blit(Racket_hit, racket_rect)
        DISPLAYSURF.blit(bug_image, bug_rect)

    if p:
        scoreboard = myfont.render('Score: {}'.format(score), 1, WHITE)
        DISPLAYSURF.blit(scoreboard, (10, 10))

    if bug_rect.x <= -25:
        l = False
        t = True
        a = True
        if t and a:
            label = myfont.render(" Play Again", 1, WHITE)
            DISPLAYSURF.blit(label2, (200, 250))
            DISPLAYSURF.blit(label, (370, 550))
            DISPLAYSURF.blit(label4, (440, 580))
        if key[pygame.K_UP]:
            u = True
            d = False

        if u:
            pygame.draw.rect(DISPLAYSURF, WHITE, (360, 550, 230, 30,), 3)
            if key[pygame.K_RETURN]:
                bug_rect = bug_image.get_rect(topleft=(setplace))
                racket_rect = Racket.get_rect(topleft=(-25, 298))
                level = 2
                score = 0
                p = True
                l = True
                t = False
                a = False
        if key[pygame.K_DOWN]:
            d = True
            u = False
        if d:
            pygame.draw.rect(DISPLAYSURF, RED, (430, 580, 90, 30,), 3)
            if key[pygame.K_RETURN]:
                pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
