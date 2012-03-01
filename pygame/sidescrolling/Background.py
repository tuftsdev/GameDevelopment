import pygame, os, sys
from pygame.locals import *

class ScrollingBackground(pygame.sprite.Sprite):
	''' A simple sprite that scrolls down the screen '''
	
	def __init__(self, screen, scroll_speed):
		''' Remember to pass the surface to the sprite for updating and drawing! '''
		pygame.sprite.Sprite.__init__(self) #call Sprite intializer
		self.screen = screen
		self.scrolling = True
		
		# Load the image
		try:
			self.image = pygame.image.load('mario-1-1.gif').convert_alpha()
			self.rect = self.image.get_rect()

			# Get the image's width and height
			self.image_w, self.image_h = self.image.get_size()

			# Get the screen's width and height
			self.screen_w = self.screen.get_size()[0]
			self.screen_h = self.screen.get_size()[1]
				
			# Set the (x, y)
			self.x = 0
			self.y = 0
		
			# Set the scroll speed
			self.dx = scroll_speed
			
		except pygame.error, message:
			print "Cannot load background image!"
			raise SystemExit, message
				
	def update(self):
		''' Move the sprite if it still has room '''
		if ((self.x * -1) > self.image_w - self.screen_w) and self.scrolling == True:
			self.scrolling = False
		else:
			self.x -= self.dx
		
	def draw(self):
		''' Draw the sprite on the screen '''
		if self.scrolling == True:
			draw_pos = self.image.get_rect().move(self.x, self.y)
			self.screen.blit(self.image, draw_pos)
                        
if __name__ == "__main__":
	# Check if sound and font are supported
	if not pygame.font:
		print "Warning, fonts disabled"
	if not pygame.mixer:
		print "Warning, sound disabled"
		
	# Constants
	FPS = 60
	SCREEN_WIDTH, SCREEN_HEIGHT = 500, 210
	SCROLL_SPEED = 3
	
	# Initialize Pygame, the clock (for FPS), and a simple counter
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	pygame.display.set_caption('Scrolling Background Demo')
	clock = pygame.time.Clock()
	
	# Create the background
	sprites = []
	sprites.append(ScrollingBackground(screen, SCROLL_SPEED))
	
	# Game loop
	while True:
		time_passed = clock.tick(FPS)
		
		# Event handling here (to quit)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
		
		# Update and redraw all sprites
		for sprite in sprites:
			sprite.update()
			sprite.draw()
		
		# Draw the sprites
		pygame.display.flip()
