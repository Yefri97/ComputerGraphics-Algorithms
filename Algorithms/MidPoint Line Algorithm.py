import pygame
import sys
import math

#Define constants
height = 800
width  = 800
origin = [width/2, height/2]

#Define colors
white=(255, 255, 255)
black=(  0,   0,   0)
red=  (255,   0,   0)
green=(  0, 255,   0)
blue= (  0,   0, 255)

# Transform component x from cartesian coordinate to screen coordinate
def xcar(px):
    return int(origin[0]+px)

# Transform component y from cartesian coordinate to screen coordinate
def ycar(py):
    return int(origin[1]-py)

# Draw the origin lines
def draw_origin(sc, color, border):
    pygame.draw.line(sc, color, [xcar(-width/2), ycar(0)], [xcar(width/2), ycar(0)], border)
    pygame.draw.line(sc, color, [xcar(0), ycar(-height/2)], [xcar(0), ycar(height/2)], border)

'''
# MidPoint line algorithm
def drawLine(p0, p1):
    dy = p1[1] - p0[1]
    dx = p1[0] - p0[0]
    d = 2 * dy - dx

    x = p0[0]
    y = p0[1]
    while (x < p1[0]):
        screen.set_at((x, y), blue)
        print (x, y)
        if d > 0:
            y = y + 1
            d = d - (2 * dx)
        x = x + 1
        d = d + (2 * dy)
'''

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    #pygame.draw.rect(screen, white, [0, 0, 800, 800])

    draw_origin(screen, white, 2)
    #drawLine([0, 400], [800, 600])

    pygame.display.flip()

    Finish = False
    while (not Finish):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                Finish = True
