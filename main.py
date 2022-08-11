import pygame
import math

window = None
cube_img = None

W = 1600
H = 900

def renderCube(x, y, z):
	global window, cube_img, W, H, boom
	sx, sy = 0, 0
	sx += x
	sy += x / 2
	
	sx -= z
	sy += z / 2

	sy += y

	sx *= 16
	sy *= 16

	window.blit(cube_img, (sx + W/2, sy + H/2))

def update():
	pass

def render():
	global window, cube_img, W, H
	
	window.fill((60, 100, 120))

	size = 10

	for k in range(size, -size - 1, -1):
		for j in range(-size, size + 1, 1):
			for i in range(-size, size + 1, 1):


				if math.sqrt(k*k + j*j + i*i) <= size:
					renderCube(i, k, j)
	
	pygame.display.flip()

def main():
	global window, cube_img, W, H

	pygame.init()
	
	window = pygame.display.set_mode((W, H))
	cube_img = pygame.image.load("cube.png")
	
	running = True
	
	while running:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
		update()
		render()
		
	return 0


if __name__ == "__main__":
	main()


