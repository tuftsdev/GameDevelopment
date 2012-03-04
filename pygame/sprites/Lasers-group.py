import pygame, os, sys
from pygame.locals import *
from random import randint

class Laser(pygame.sprite.Sprite):
	''' A simple sprite that bounces off the walls '''
	
	def load_image(self, image_name):
		''' The proper way to load an image '''
		try:
			image = pygame.image.load(image_name)
		except pygame.error, message:
			print "Cannot load image: " + image_name
			raise SystemExit, message
		return image.convert_alpha()

	def __init__(self, init_x, init_y, init_y_speed):
		''' Create the LaserBolt at (x, y) moving up at a given speed '''
		pygame.sprite.Sprite.__init__(self) #call Sprite intializer
		
		# Load the image
		self.image = self.load_image('laser.gif')

		# Create a moving collision box
		self.rect = self.image.get_rect()
		self.rect.x = init_x
		self.rect.y = init_y
				
		# Set the default speed (dx, dy)
		self.dy = init_y_speed
				
	def update(self):
		''' Move the sprite '''
		self.rect.y += self.dy
		self.rect.move(self.rect.x, self.rect.y)
		
		# Remove sprite from group if it goes off the screen...
		if self.rect.y <= 0:
			self.kill() # see http://pygame.org/docs/ref/sprite.html#Sprite.kill
					
if __name__ == "__main__":
	# Check if sound and font are supported
	if not pygame.font:
		print "Warning, fonts disabled"
	if not pygame.mixer:
		print "Warning, sound disabled"
		
	# Constants
	FPS = 30
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	BACKGROUND_COLOR = (0, 0, 0)
	
	# Initialize Pygame, the clock (for FPS), and a simple counter
	pygame.init()
	pygame.display.set_caption('Pygame Sprite Group Demo')
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	clock = pygame.time.Clock()

	# Create the sprite group
	lasers = pygame.sprite.Group()

	# Game loop
	while True:
		time_passed = clock.tick(FPS)
		
		# Add a new laser at random x-coordinate with random speed
		lasers.add(Laser(randint(1, SCREEN_WIDTH), 550, randint(1, 10) * -1))
		
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
		lasers.update()
		lasers.draw(screen)
		
		# Draw the sprites
		pygame.display.update()
		
		# DEBUG: Print the size of the sprite group to console
		print len(lasers.sprites())
		
