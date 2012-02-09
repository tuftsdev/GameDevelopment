import pygame, sys, os
from pygame.locals import * # This module contains various constants used by Pygame

def quit():
	''' Self explanatory '''
	pygame.quit()
	sys.exit(0)
	
def input(events):
	''' Function to handle events, particularly quitting the program '''
	for event in events:
		if event.type == QUIT:
			quit()
		else:
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					quit()
				else:
					print event.key

# Initialize all imported Pygame modules (a.k.a., get things started)
pygame.init()

# Set the display's dimensions
screenDimensions = (800, 600)
window = pygame.display.set_mode(screenDimensions)
pygame.display.set_caption('Pygame Test') # Set the window bar title
screen = pygame.display.get_surface() # This is where images are displayed

# Draw
img = pygame.image.load("krusty.jpg").convert()
screen.blit(img, (10, 10))
pygame.display.flip()

# The game loop
while True:
	input(pygame.event.get())
