import pygame, sys, os
from pygame.locals import * # This module contains various constants used by Pygame

def quit():
	''' Self explanatory '''
	pygame.quit()
	sys.exit(0)
	
def input(events):
	''' Function to handle events, particularly quitting the program '''
	for event in events:
		print event		
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				quit()
			else:
				print event.key

# Initialize all imported Pygame modules (a.k.a., get things started)
pygame.init()

# Set the display's dimensions
screenDimensions = (800, 600)
window = pygame.display.set_mode(screenDimensions, pygame.RESIZABLE)
pygame.display.set_caption('KRUSTY!!!') # Set the window bar title
screen = pygame.display.get_surface() # This is where images are displayed

# The game loop
boing_sound = pygame.mixer.Sound("boing.wav").play()
background = pygame.Surface(screen.get_size())
while True:
	# Clear screen
	background = background.convert()
	background.fill((100, 0, 100))
	screen.blit(background, (0, 0))

	# Draw
	img = pygame.image.load("krusty.jpg").convert()
	screen.blit(img, (10, 10))
	pygame.display.flip()

	# Process events via input function
	input(pygame.event.get())
