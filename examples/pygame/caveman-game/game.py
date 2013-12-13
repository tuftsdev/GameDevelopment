import pygame, os, sys, random
from pygame.locals import *

##################################################
# Game sprite                                    #
##################################################

class Caveman(pygame.sprite.Sprite):
	''' A sprite for the good guy in your game '''
	
	def load_image(self, image_name):
		''' The proper way to load an image '''
		try:
			image = pygame.image.load(image_name)
		except pygame.error, message:
			print "Cannot load image: " + image_name
			raise SystemExit, message
		return image.convert_alpha()

	def __init__(self, screen, x, y):
		''' Initialization '''
		self.image = self.load_image("caveman.png")
		self.screen = screen
		self.x = x
		self.y = y
		self.rect = self.image.get_rect()
		self.image_w, self.image_h = self.image.get_size()
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)		    
	
	def draw(self):
		''' Draw the sprite on the screen '''
		self.screen.blit(self.image, (self.x, self.y))

	def update(self, dir):
		''' Update the sprite; YOU COMPLETE (remove pass) '''
		if dir == "UP":
			self.y = self.y - 3
		elif dir == "DOWN":
			self.y = self.y + 3
		elif dir == "LEFT":
			self.x = self.x - 3
		elif dir == "RIGHT":
			self.x = self.x + 3
			
		# Move the bounding box too!
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)	

class Steak(pygame.sprite.Sprite):
	''' A sprite for the good guy in your game '''

	def load_sound(self, sound_name):
		try:
			sound = pygame.mixer.Sound(sound_name)
		except pygame.error, message:
			print "Cannot load sound: " + sound_name
			raise SystemExit, message
		return sound
		
	def load_image(self, image_name):
		''' The proper way to load an image '''
		try:
			image = pygame.image.load(image_name)
		except pygame.error, message:
			print "Cannot load image: " + image_name
			raise SystemExit, message
		return image.convert_alpha()

	def __init__(self, screen, x, y):
		''' Initialization '''
		self.image = self.load_image("steak.png")
		self.screen = screen
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect = self.image.get_rect()
		self.image_w, self.image_h = self.image.get_size()
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)	
		self.eaten = False
    
	def draw(self):
		''' Draw the sprite on the screen; draw the steak if it hasn't been eaten yet '''
		if self.eaten == False:
			self.screen.blit(self.image, (self.x, self.y))

	def is_eaten(self):
		''' Oh joy, the steak is eaten! '''
		self.eaten = True
		moo = self.load_sound("moo.wav")
		moo.play()
		
	def update(self):
		''' Meh, the steak does not move '''
		pass

##################################################
# The main component of your game                #
##################################################

def quit():
	''' Self explanatory '''
	pygame.quit()
	sys.exit(0)

# Initialize all imported Pygame modules (a.k.a., get things started)
pygame.init()

# Set the display's dimensions
screenDimensions = (800, 600)
window = pygame.display.set_mode(screenDimensions, pygame.RESIZABLE)
pygame.display.set_caption('My Game') # Set the window bar title

# Get the drawing surface and background
screen = pygame.display.get_surface() # This is where images are displayed
background = pygame.Surface(screen.get_size())

# Keep track of which arrow key was pressed
pressed = None

# Set up our two sprites: the caveman and the steak
cman = Caveman(screen, 10, 10)
st = Steak(screen, random.randint(50, 750), random.randint(50, 550))
score = 0

# The game loop
while True:

	# Clear the screen (to white)
	screen.fill((255, 255, 255))

	# Draw the sprites
	cman.draw()
	st.draw()
	cman.update(pressed) # Send the update() method of the caveman the direction of arrow press
	
	# Check for collisions
	if pygame.sprite.collide_rect(cman, st) and st.eaten == False:
		st.is_eaten() # If the caveman hit the steak, change the state of the steak to eaten and play sound
		score = score + 1
		print "Score: " + str(score)
		st = Steak(screen, random.randint(50, 750), random.randint(50, 550))

	# Update the entire drawing surface
	pygame.display.flip()

	# Process events via input function
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				quit()
			elif event.key == K_UP:
				pressed = "UP"
			elif event.key == K_DOWN:
				pressed = "DOWN"
			elif event.key == K_LEFT:
				pressed = "LEFT"
			elif event.key == K_RIGHT:
				pressed = "RIGHT"
			else:
				pressed = None
