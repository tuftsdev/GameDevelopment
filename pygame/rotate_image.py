import pygame, sys
from pygame.locals import *

def myquit():
	''' Self explanatory '''
	pygame.quit()
	sys.exit(0)

def check_inputs(events):
	''' Function to handle events, particularly quitting the program '''
	for event in events:
		if event.type == QUIT:
			quit()
		else:
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					myquit()
				elif event.key == K_LEFT:
					print "Rotate image left"
				elif event.key == K_RIGHT:
					print "Rotate image right"
				else:
					print event.key

def main():
	# Initialize Pygame
	pygame.init()
	
	# Set up screen
	SCREEN_WIDTH = 600
	SCREEN_HEIGHT = 480
	window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Rotate Image') # Set the window bar title
	screen = pygame.display.get_surface() # This is where images are displayed

	img = pygame.image.load("alien2.gif").convert()

	#Rotate image
	image_rotated = pygame.transform.rotate(img, -45)

	screen.blit(image_rotated, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

	pygame.display.flip()

	while True:
		check_inputs(pygame.event.get())

main()
