import pygame 
from pygame.locals import *

pygame.init()

width, height = 2000, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Collision")

m1, m2 = 5, 20
v1, v2 = 5, 5

running = True

small_rect = Rect(width//2 - 50, height//2 - 50 , 50, 50)
big_rect = Rect(width//2 + 150, height//2 - 150 , 150, 150)


while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	window.fill((9,110,143))

	
	if small_rect.x < width:
		small_rect = small_rect.move(v1,0)

	if big_rect.x >= 0:
		big_rect = big_rect.move(-v2,0)

	pygame.draw.rect(window, (50, 50, 50), (width//2 - 500, height//2-200 , 20, 200))
	pygame.draw.rect(window, (250, 250, 250), small_rect)
	pygame.draw.rect(window, (0, 0, 250),big_rect )

	pygame.display.update()

pygame.quit()