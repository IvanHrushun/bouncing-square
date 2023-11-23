#credits to Ivan
#discord ivan.7131

import pygame
import random
pygame.init()

display_width = 1700
display_height = 600

canvas = pygame.Surface((display_width, display_height))
pygame.display.set_caption("bouncing")

Red = (255, 0, 0)

Green = (40, 148, 10)

Blue = (0, 0, 255)

White = (255, 255, 255)

Black = (0, 0, 0)

plrX = 0
plrY = 0

cube_width = 100
cube_height = 100

fX = 0 #idk why is this here it just works
sX = display_width - cube_width #display width - cube width
fY = 0 #idk why is this here it just works
sY = display_height - cube_height #display height - cube height
numX = 100
numY = 300

plusfalX = True
minfalX = False

plusfalY = True
minfalY = False
speed = 4



display = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()
def run_game():
    global plrX, plrY, Red, Green, Blue, White, Black, fX, sX, sY, xY, num, plusfalX, minfalX, speed, numX, numY, plusfalY, minfalY
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            

        display.fill(Blue)
        cube = pygame.draw.rect(display, Red, (plrX, plrY, cube_width, cube_height))
        if plusfalX == True:
            numX += speed
            plrX = numX
            #print(numX)
            if numX >= sX:
                plusfalX = False
                minfalX = True
        if minfalX == True:
            numX -= speed
            plrX = numX
            #print(numX)
            if numX <= fX:
                plusfalX = True
                minfalX = False
        ##--------------------------X up Y down

        if plusfalY == True:
            numY += speed
            plrY = numY
            #print(numY)
            if numY >= sY:
                plusfalY = False
                minfalY = True
        if minfalY == True:
            numY -= speed
            plrY = numY
            #print(numY)
            if numY <= fY:
                plusfalY = True
                minfalY = False
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
run_game()
