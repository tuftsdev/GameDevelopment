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
				#else:
				#	print event.key
			else:
				print event

# Initialize all imported Pygame modules (a.k.a., get things started)
pygame.init()

# Enable joystick support
pygame.joystick.init()

# Set the display's dimensions
screenDimensions = (800, 600)
window = pygame.display.set_mode(screenDimensions)
pygame.display.set_caption('Pygame Test') # Set the window bar title
screen = pygame.display.get_surface() # This is where images are displayed

# Clear the background
background = pygame.Surface(screen.get_size()).convert()
background.fill((0, 255, 0))
screen.blit(background, (0,0))

# Draw
try:
	img = pygame.image.load("krusty.jpg").convert()
	screen.blit(img, (10, 10))
except pygame.error, message:
	pass
	
# Draw a string onto screen
font = pygame.font.Font(None, 36)
text = font.render("Hey hey kids!", 1, (0, 0, 255))
screen.blit(text, (500, 400))
pygame.display.flip()

# Play a sound
try:
	sound = pygame.mixer.Sound("krusty.wav")
	sound.play()
except pygame.error, message:
	pass
	
# Detect if joystick is available
joysticks = pygame.joystick.get_count()
if joysticks:
	print str(joysticks) + " joystick(s) detected!"

# Initialize each joystick
	for i in range(joysticks):
		joystick = pygame.joystick.Joystick(i)
		joystick.init()
		name = joystick.get_name()
		print "Joystick " + str(i) + " name: " + name

# The game loop
while True:
	input(pygame.event.get())

