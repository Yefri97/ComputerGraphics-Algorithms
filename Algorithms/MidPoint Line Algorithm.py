import pygame
import sys
import math

height = 800
width  = 800

white=(255, 255, 255)
black=(  0,   0,   0)
red=  (255,   0,   0)
green=(  0, 255,   0)
blue= (  0,   0, 255)

def xcar(px):
    return int(origin[0]+px)
 
def ycar(py):
    return int(origin[1]-py)

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

pygame.init()
screen = pygame.display.set_mode([width, height])

# int main() {

pygame.draw.rect(screen, white, [0, 0, 800, 800])

drawLine([0, 400], [800, 600])

pygame.display.flip()

# }

Finish = False
while (not Finish):
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            Finish = True