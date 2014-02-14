import pygame, os, sys
from pygame.locals import *
from random import randint

class SimpleSprite(pygame.sprite.Sprite):
	''' A simple sprite that bounces off the walls '''
	
	def load_image(self, image_name):
		''' The proper way to load an image '''
		try:
			image = pygame.image.load(image_name)
		except pygame.error, message:
			print "Cannot load image: " + image_name
			raise SystemExit, message
		return image.convert_alpha()

	def __init__(self, screen, img_filename, init_x, init_y, init_x_speed, init_y_speed):
		''' Remember to pass the surface to the sprite for updating and drawing! '''
		pygame.sprite.Sprite.__init__(self) #call Sprite intializer
		self.screen = screen
		
		# Load the image
		self.image = self.load_image(img_filename)
		self.rect = self.image.get_rect() # Set the rect attribute for the sprite (absolutely necessary for collision detection)

		# Get the image's width and height
		self.image_w, self.image_h = self.image.get_size()
				
		# Set the (x, y)
		self.x = init_x
		self.y = init_y
		
		# Set the default speed (dx, dy)
		self.dx = init_x_speed
		self.dy = init_y_speed
				
	def update(self):
		''' Move the sprite; bounce off the walls '''
		if ((self.x + self.dx) <= 0):
			self.dx = self.dx * -1
		if ((self.x + self.dx) >= self.screen.get_size()[0]):
			self.dx = self.dx * -1
		if ((self.y + self.dy) <= 0):
			self.dy = self.dy * -1
		if ((self.y + self.dy) >= self.screen.get_size()[1]):
			self.dy = self.dy * -1
		self.x = self.x + self.dx
		self.y = self.y + self.dy
	
	def draw(self):
		''' Draw the sprite on the screen '''
		draw_pos = self.image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h / 2)
		self.screen.blit(self.image, draw_pos)

if __name__ == "__main__":
	# Check if sound and font are supported
	if not pygame.font:
		print "Warning, fonts disabled"
	if not pygame.mixer:
		print "Warning, sound disabled"
		
	# Constants
	FPS = 60
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	MAX_SPEED = 10
	BACKGROUND_COLOR = (255, 255, 255)
	SPRITE_IMAGES = ['bluecreep.png', 'pinkcreep.png', 'graycreep.png']
	NUM_SPRITES = 1
	COUNTER_LOCATION = (10, 10)
	
	# Initialize Pygame, the clock (for FPS), and a simple counter
	pygame.init()

	#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	
	# For fullscreen mode...
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN, 32)
	pygame.display.set_caption('Simple Sprite Demo')
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 28)
	counter = 0
	
	# Create the sprites; choose random sprite image, starting location, and starting speed for each sprite
	sprites = []
	for i in range(NUM_SPRITES):
		sprites.append(SimpleSprite(screen, SPRITE_IMAGES[randint(0, len(SPRITE_IMAGES) - 1)], randint(1, SCREEN_WIDTH), randint(1, SCREEN_HEIGHT), randint(1, MAX_SPEED), randint(1, MAX_SPEED)))
	
	# Game loop
	while True:
		time_passed = clock.tick(FPS)
		text = font.render("Time: " + str(counter) + " (at " + str(FPS) + " FPS)", 1, (0, 0, 0))
		
		# Event handling here (to quit)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()					
		
		# Redraw the background
		screen.fill(BACKGROUND_COLOR)
		
		# Update and redraw all sprites
		for sprite in sprites:
			sprite.update()
			sprite.draw()
		
		# Draw the counter on surface
		screen.blit(text, COUNTER_LOCATION)
		
		# Update the counter
		counter+=1
		
		# Draw the sprites
		pygame.display.flip()
