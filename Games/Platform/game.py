import pygame
import sys
import math

#Define constants
height = 800
width  = 800

#Define colors
white=(255, 255, 255)
black=(  0,   0,   0)
red=  (255,   0,   0)
green=(  0, 255,   0)
blue= (  0,   0, 255)

class player(pygame.sprite.Sprite):

	def __init__(self, imagen, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

	def move_left():
        self.rect.x -= 5

    def move_right():
        self.rect.x += 5

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    # Create local variables
    universe = pygame.sprite.Group()
    players  = pygame.sprite.Group()

    p = Player('img/player.png', 400, 700)
	players.add(p)
	universe.add(p)

    reloj    = pygame.time.Clock()

    Finish = False
    while (not Finish):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Finish = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                  p.move_left()
                if event.key == K_RIGHT:
                  p.move_right()

        pygame.draw.rect(screen, BLACK, [0, 0, 800, 800])

        universe.update()
		universe.draw(screen)

        pygame.display.flip()
		reloj.tick(60)
