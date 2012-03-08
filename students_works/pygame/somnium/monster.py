import pygame, os, sys, random
from pygame.locals import *
from const import *
from math import *

__name__ = "monster"

class Monster(pygame.sprite.Sprite):

        def load_image(self, image_name):
                try:
                        image = pygame.image.load(image_name)
                except pygame.error, message:
                        return None
                return image.convert_alpha()

        def __init__(self, screen, x, y, name):
                self.image = self.load_image("sprites/"+name+"1down.png")
                self.screen = screen
                self.rect = self.image.get_rect()
                self.x = 400 + x
                self.y = 300 + y
                self.image_w, self.image_h = self.image.get_size()
                self.rect.move(self.x, self.y)
                self.rect.topleft = (self.x, self.y)
                self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
                self.interactionrect = pygame.Rect(self.x-4,self.y-4,self.image_w+8,self.image_h+8)
                self.dead = False
                self.imageCount = 0
		self.pigCount = 0
                self.name = name
                self.down = [self.load_image(   "sprites/" + self.name + "1down.png"  ),
                               self.load_image( "sprites/" + self.name + "2down.png"  ),
                             self.load_image(   "sprites/" + self.name + "3down.png"  ),
                             self.load_image(   "sprites/" + self.name + "4down.png"  )]
                self.up = [self.load_image(     "sprites/" + self.name + "1up.png"    ),
                               self.load_image( "sprites/" + self.name + "2up.png"    ),
                             self.load_image(   "sprites/" + self.name + "3up.png"    ),
                             self.load_image(   "sprites/" + self.name + "4up.png"    )]
                self.right = [self.load_image(  "sprites/" + self.name + "1right.png" ),
                               self.load_image( "sprites/" + self.name + "2right.png" ),
                             self.load_image(   "sprites/" + self.name + "3right.png" ),
                             self.load_image(   "sprites/" + self.name + "4right.png" )]
                self.left = [self.load_image(   "sprites/" + self.name + "1left.png"  ),
                               self.load_image( "sprites/" + self.name + "2left.png"  ),
                             self.load_image(   "sprites/" + self.name + "3left.png"  ),
                             self.load_image(   "sprites/" + self.name + "4left.png"  )]
		self.state = "s"
		self.timer = 0
		self.dirx = 0
		self.diry = 0
		self.nxt = 1
		self.direction = 1
		self.fibonacci = False
		self.playing = False
		try:
			self.goodmusic = pygame.mixer.Sound("sounds/ambient-3.ogg")
		except:
			print "FIND THE FIBONACCI NUMBERS"
    
        def draw(self, x, y):
                temp = []
                if(self.diry >= 0):
                        temp = self.down
                elif(self.diry < 0):
                        temp = self.up
                if(self.dirx > 0 and self.direction==0):
                        temp = self.right
		elif(self.dirx <= 0 and self.direction == 0):
                        temp = self.left
                if(temp[self.imageCount/30]!=None and self.imageCount < 119):
                        self.image = temp[self.imageCount/30]
                else:
                        self.imageCount = -1
                self.imageCount +=1
                
                if(self.dead == False):
                         self.screen.blit(self.image, (x, y))

        def isDead(self): #Will be changed so it ends the game.
                self.dead = True
                
	def move(self,nodes,x,y):
		diffx = (self.x + self.image_w / 2) - x
		diffy = (self.y + self.image_h / 2) - y
		nxt = self.nxt % 7
		if(self.state == "s"): # "Search" state: cycle through nodes
			if(fabs(diffx) < 120 and fabs(diffy) < 120): # Check to switch out search state
				self.state = "h"
				try:
        				doorsound = pygame.mixer.Sound("sounds/roar.wav")
				except pygame.error, message:
        				print "Cannot load sound: roar.wav"
				doorsound.play()
				if(self.fibonacci and not self.playing):
					self.goodmusic.play(loops = -1)
					self.playing = True
			if(self.x - (nodes[nxt][0] + 400) > 0):
				self.dirx = -1
				self.direction = 0
			elif(self.x - (nodes[nxt][0] + 400) < 0):
				self.dirx = 1
				self.direction = 0
			else:
				self.dirx = 0
			if(self.y - (nodes[nxt][1] + 300) > 0):
				self.diry = -1
				self.direction = 1
			elif(self.y - (nodes[nxt][1] + 300) < 0):
				self.diry = 1
				self.direction = 1
			else:
				self.diry = 0
			self.x = self.x + (self.dirx)
			self.y = self.y + (self.diry)
		elif(self.state == "h"): # "Hunt" state: charge at player
			if(self.timer >= 100 ): # Check to switch out of hunt state
				self.state = "s"
				self.timer = 0
			if(diffx < 0):
				self.dirx = 1
			elif(diffx > 0):
				self.dirx = -1
			else:
				self.dirx = 0
			if(diffy < 0):
				self.diry = 1
			elif(diffy > 0):
				self.diry = -1
			else:
				self.diry = 0
			self.x += self.dirx * 3
			self.y += self.diry * 3
			if(fabs(diffx) > fabs(diffy)):
				self.direction = 0
			else:
				self.direction = 1
			self.timer = self.timer + 1
		self.rect.move(self.x, self.y)
                self.rect.topleft = (self.x, self.y)
                self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
		if(self.x == nodes[nxt][0] + 400 and self.y == nodes[nxt][1] + 300):
			self.nxt = self.nxt + 1
		pass

class Pig(Monster):

        def draw(self,x,y):
                if(self.dead==False):
                        temp = []
                        if(self.diry > 0):
                                temp = self.down
                        elif(self.diry < 0):
                                temp = self.up
                        elif(self.dirx >= 0):
                                temp = self.right
                        elif(self.dirx < 0):
                                temp = self.left
                        if(temp[self.imageCount/30]!=None and self.imageCount < 119):
                                self.image = temp[self.imageCount/30]
                        else:
                                self.imageCount = -1
                        self.imageCount += 1
                        self.pigCount += 1 
                        if(self.pigCount<600):
                                self.x += self.dirx * 0.5
                                self.dirx = 1
                        elif(self.pigCount<1200):
                                self.x += self.dirx * 0.5
                                self.dirx = -1
                        else:
                                self.pigCount = 0
                        self.rect.move(self.x,self.y)
                        self.rect.topleft = (self.x,self.y)
                        self.rect.bottomright = (self.x + self.image_w,self.y + self.image_h)
                        self.interactionrect.move(self.x-4,self.y-4)
                        self.interactionrect.topleft = (self.x,self.y)
                        self.interactionrect.bottomright = (self.x+self.image_w+8,self.y+self.image_h+8)
                self.screen.blit(self.image,(x,y))

	def isDead(self):
		self.pick_up()
                self.image = self.load_image("sprites/deadpig.png")
		self.rect = pygame.Rect(0,0,0,0)
		self.interactionrect = self.rect
                self.dead = True
	
	def pick_up(self):
		try:
			pickup = pygame.mixer.Sound("sounds/item.wav")
		except:
			print "Cannot load sound: item.wav"
		pickup.play()

class Fire(Monster):

	def draw(self,x,y):
		temp = self.up
		if(temp[self.imageCount/30] != None and self.imageCount < 119):
			self.image = temp[self.imageCount/30]
		else:
			self.imageCount = -1
		self.imageCount += 1
		if(not self.dead):
			self.screen.blit(self.image,(x - 50,y))
			self.screen.blit(self.image,(x + 50,y))
			self.screen.blit(self.image,(x,y))
			self.screen.blit(self.image,(x - 75,y + 35))
			self.screen.blit(self.image,(x + 25,y + 35))
			self.screen.blit(self.image,(x - 25,y + 35))
			self.screen.blit(self.image,(x + 75,y + 35))
		else:
			pass

	def isDead(self):
		self.image = None
		self.rect = pygame.Rect(0,0,0,0)
		self.interactionrect = self.rect
		self.dead = True
