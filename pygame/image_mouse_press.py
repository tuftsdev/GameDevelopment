import pygame, sys
from pygame.locals import *

# If an image is clicked on, move it diagonally

class SimpleSprite(pygame.sprite.Sprite):
	''' A container for a simple sprite '''
	
	def load_image(self, image_name):
		''' The proper way to load an image '''
		try:
			image = pygame.image.load(image_name)
		except pygame.error, message:
			print "Cannot load image: " + image_name
			raise SystemExit, message
		return image.convert_alpha()

	def __init__(self, screen, img_file, x, y, label):
		self.screen = screen
		self.image = self.load_image(img_file)
		self.x = x
		self.y = y
		self.label = label
		self.rect = self.image.get_rect()
		self.image_w, self.image_h = self.image.get_size()
		self.clicked = False
		
	def clicked_on(self, a, b):
		if (a >= self.x and a <= self.x + self.image_w and b >= self.y and b <= self.y + self.image_h):
			print "You clicked on " + self.label
			# Toggle
			if (self.clicked == True):
				self.clicked = False
			else:
				self.clicked = True
				
	def draw(self):
		self.screen.blit(self.image, (self.x, self.y))
		pass
		
	def update(self):
		if self.clicked == True:
			self.x += 1
			self.y += 1

def myquit():
	''' Self explanatory '''
	pygame.quit()
	sys.exit(0)

def check_inputs(events, sprites):
	''' Function to handle events, particularly quitting the program '''
	for event in events:
		if event.type == QUIT:
			quit()
		elif event.type == MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			for s in sprites: # Go through every sprite
				s.clicked_on(mouse_x, mouse_y)
		else:
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					myquit()

def main():
	# Initialize Pygame
	pygame.init()
	
	# Set up screen
	SCREEN_WIDTH = 600
	SCREEN_HEIGHT = 480
	window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Rotate Image') # Set the window bar title
	screen = pygame.display.get_surface() # This is where images are displayed
	sprites = [SimpleSprite(screen, "awesome.png", 200, 90, "Awesome (right)!"),
				SimpleSprite(screen, "boom.gif", 300, 300, "BOOM!"),
				SimpleSprite(screen, "awesome.png", 20, 20, "Awesome (left)!"),
				SimpleSprite(screen, "smiley.gif", 60, 60, "Smiley")]
	
	while True: # for each frame
		screen.fill((255, 255, 255))
		check_inputs(pygame.event.get(), sprites)
		for elem in sprites:
			elem.draw() # essentially redraw
			elem.update()
		pygame.display.flip()

main()
