import pygame, sys, os
from pygame.locals import * # This module contains various constants used by Pygame

def quit():
	''' Self explanatory '''
	sys.exit(0)
	pygame.quit()
	
def input(events):
	''' Function to handle mouse events and quit only '''
	for event in events:
		if event.type == QUIT:
			quit()
		else:
			if event.type == MOUSEBUTTONUP:
				print "FIRE!"
			if event.type == MOUSEBUTTONDOWN:
				print "Waiting..."
			if event.type == MOUSEMOTION:
				print "I am moving around!"
				
# Initialize all imported Pygame modules (a.k.a., get things started)
pygame.init()

# Set the display's dimensions
screenDimensions = (800, 600)
window = pygame.display.set_mode(screenDimensions)
pygame.display.set_caption('Pygame Test') # Set the window bar title
screen = pygame.display.get_surface() # This is where images are displayed

# The game loop
while True:
	input(pygame.event.get())
