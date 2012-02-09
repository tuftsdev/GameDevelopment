# Simple game clock example
# Reference: http://www.pygame.org/docs/ref/time.html

import pygame, sys
from pygame.locals import *

def myquit():
	''' Self explanatory '''
	pygame.quit()
	sys.exit(0)
	
def main():
	# Initialize Pygame
	pygame.init()
	
	# Set up screen
	SCREEN_WIDTH = 600
	SCREEN_HEIGHT = 480
	window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Game Clock') # Set the window bar title
	screen = pygame.display.get_surface() # This is where images are displayed
	
	# Set up font
	font = pygame.font.Font(None, 36)

	# Set up clock
	clock = pygame.time.Clock()
	FPS = 30
	seconds = 0
	pygame.time.set_timer(USEREVENT + 1, 1000) # Used to correctly implement seconds
	
	while True: # for each frame
		clock.tick(FPS)
		screen.fill((255, 255, 255))		
		time_display = font.render("Time: " + str(clock.get_time()), 1, (0, 0, 0))
		rawtime_display = font.render("Raw Time: " + str(clock.get_rawtime()), 1, (0, 0, 0))
		fps_display = font.render("FPS: " + str(clock.get_fps()), 1, (0, 0, 0))
		pygame_total_ticks_display = font.render("Pygame Ticks (total): " + str(pygame.time.get_ticks()), 1, (0, 0, 0))
		seconds_display = font.render("Seconds: " + str(seconds), 1, (0, 0, 0))
		screen.blit(time_display, (10, 10))
		screen.blit(rawtime_display, (10, 35))
		screen.blit(fps_display, (10, 60))
		screen.blit(pygame_total_ticks_display, (10, 85))
		screen.blit(seconds_display, (10, 110))
		for event in pygame.event.get():
			if event.type == QUIT:
				quit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					myquit()
			elif event.type == USEREVENT + 1:
				seconds+=1
		pygame.display.flip()

main()
