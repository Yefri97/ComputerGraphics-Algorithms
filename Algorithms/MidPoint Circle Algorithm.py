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

# MidPoint circle algorithm
def drawCircle(p, r, color):
    x = r
    y = 0
    d = 1 - x

    while (y <= x):
        screen.set_at((xcar( x + p[0]), ycar( y + p[1])), color)
        screen.set_at((xcar( y + p[0]), ycar( x + p[1])), color)
        screen.set_at((xcar(-x + p[0]), ycar( y + p[1])), color)
        screen.set_at((xcar(-y + p[0]), ycar( x + p[1])), color)
        screen.set_at((xcar(-x + p[0]), ycar(-y + p[1])), color)
        screen.set_at((xcar(-y + p[0]), ycar(-x + p[1])), color)
        screen.set_at((xcar( x + p[0]), ycar(-y + p[1])), color)
        screen.set_at((xcar( y + p[0]), ycar(-x + p[1])), color)
        if d > 0:
            x = x - 1
            d = d - (2 * x)
        y = y + 1
        d = d + (2 * y) + 1

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    draw_origin(screen, white, 2)

    drawCircle([  0,   0], 100, blue)
    drawCircle([  0, 100],  50, green)
    drawCircle([100, 100], 250, red)

    pygame.display.flip()

    Finish = False
    while (not Finish):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                Finish = True
