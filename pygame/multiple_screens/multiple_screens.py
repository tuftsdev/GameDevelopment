# Multiple screens example (e.g., opening -> gameplay -> game over)

import pygame, sys
from pygame.locals import *

def myquit():
	''' Self explanatory '''
	pygame.quit()
	sys.exit(0)

def load_image(image_name):
	''' The proper way to load an image '''
	try:
		image = pygame.image.load(image_name)
	except pygame.error, message:
		print "Cannot load image: " + image_name
		raise SystemExit, message
	return image.convert_alpha()

def render_timer_screen(screen, clock):
	''' Renders a screen with Pygame timer stuff '''
	# Set up font
	font = pygame.font.Font(None, 36)
	time_display = font.render("Time: " + str(clock.get_time()), 1, (0, 0, 0))
	rawtime_display = font.render("Raw Time: " + str(clock.get_rawtime()), 1, (0, 0, 0))
	fps_display = font.render("FPS: " + str(clock.get_fps()), 1, (0, 0, 0))
	pygame_total_ticks_display = font.render("Pygame Ticks (total): " + str(pygame.time.get_ticks()), 1, (0, 0, 0))
	screen.blit(time_display, (10, 10))
	screen.blit(rawtime_display, (10, 35))
	screen.blit(fps_display, (10, 60))
	screen.blit(pygame_total_ticks_display, (10, 85))

# Initialize Pygame
pygame.init()
	
# Set up screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Demo') # Set the window bar title
screen = pygame.display.get_surface() # This is where images are displayed
screen_id = 0 # This keeps track of the screen we are displaying
	
# Set up clock
clock = pygame.time.Clock()
FPS = 30
	
while True: # for each frame
	clock.tick(FPS)

	# Clear the screen
	screen.fill((255, 255, 255))

	# screen_id = 0: Render the intro screen
	if screen_id == 0:
		intro = load_image("intro.png")
		screen.blit(intro, (0, 0))
		font = pygame.font.Font(None, 36)
		instructions = font.render("Press ENTER/RETURN to cycle through screens", 1, (0, 0, 0))
		screen.blit(instructions, (25, 400))
			
	# screen_id = 1: Render a screen with Pygame timer stuff
	elif screen_id == 1:
		render_timer_screen(screen, clock)

	# screen_id = 2: Render a screenshot of a fictitious game (thanks Milas Bowman)
	elif screen_id == 2:
		game_screen = load_image("game_screen.png")
		screen.blit(game_screen, (0, 0))
		
	# Event handling stuff
	for event in pygame.event.get():
		if event.type == QUIT:
			quit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				myquit()
			elif event.key == K_RETURN:
				if screen_id == 2:
					screen_id = 0
				else:
					screen_id += 1
	pygame.display.flip()
