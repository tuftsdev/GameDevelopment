# A simple game class using pygame
import pygame
from pygame.locals import * # Import all constants into namespace
import sys, os

class GAME:
	def __init__(self):
		''' Called when game object is instantiated '''
		self._running = True
		self._surf_display = None
		self._surf_image = None
 
	def on_init(self):
		''' Set up the display '''
		pygame.init()
		self._display_surf = pygame.display.set_mode((640,400))
		self._running = True
		
	def on_event(self, event):
		''' Monitor the different events '''
		if event.type == QUIT:
			self._running = False
			
	def on_loop(self):
		''' Update stuff here '''
		pass
		
	def on_render(self):
		''' Draw stuff '''
		pass
				
	def on_cleanup(self):
		''' Executed on quitting the game '''
		pygame.quit()
	
	def run(self):
		''' Calls on_init() and contains the game loop '''
		if self.on_init() == False:
			self._running = False
		
		# The game loop
		while( self._running ):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()
 
if __name__ == "__main__" :
	test = GAME()
	test.run()
