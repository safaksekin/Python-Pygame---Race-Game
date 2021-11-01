import pygame
import sys
import random
from pygame import mixer

pygame.init()
clock=pygame.time.Clock()

score=0

window=pygame.display.set_mode((600,800))

bg1=pygame.image.load("materials_data/background-1_0.png")
bg1=pygame.transform.scale(bg1,(100,100))
bg1dark=pygame.image.load("materials_data/dd.png")
bg1dark=pygame.transform.scale(bg1dark,(100,100))

bg2=pygame.image.load("materials_data/bg1.jpg")
bg2=pygame.transform.scale(bg2,(100,100))
bg2dark=pygame.image.load("materials_data/background1_glow.jpg")
bg2dark=pygame.transform.scale(bg2dark,(100,100))

run = True
l=True
r=False

while True:
    window.fill((255,255,255))
    window.blit(bg1,(100,100))
    window.blit(bg2, (400, 100))
    while run:
        while l:
            window.blit(bg1dark,(100,100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        window.blit(bg1, (100, 100))
                        r=True
                        l=False
                    if event.key == pygame.K_SPACE:
                        run=False
        while r:
            window.blit(bg2dark,(400,100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        window.blit(bg2, (400, 100))
                        l=True
                        r=False
                    if event.key == pygame.K_SPACE:
                        run=False




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    pygame.display.update()
    clock.tick(60)