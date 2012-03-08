import pygame, os, sys, random
from pygame.locals import *

__name__ = "nodes"

class Node:
	''' A node for AI navigation '''

	def __init__(self,name,nodes,x,y):
		''' Initialize name and nodes '''
		self.x = x
		self.y = y
