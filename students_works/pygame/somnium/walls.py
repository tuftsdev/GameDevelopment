import pygame, os, sys, random
from pygame.locals import *
from const import *
from items import *
from monster import *

__name__ = "walls"

class Wall(pygame.sprite.Sprite): #Invisible wall sprite.
        def __init__(self, screen, x, y, w, h):
		self.name = "wall"
                self.screen = screen
                self.rect = pygame.Rect(x,y,w,h)
                self.x = 400 + x
                self.y = 300 + y
                self.interactionrect = pygame.Rect(self.x - 4,self.y - 4,w + 8,h + 8)
                self.rect.move(self.x, self.y)
                self.rect.topleft = (self.x, self.y)
                self.rect.bottomright = (self.x + w, self.y + h)

class Button(Wall):

	def __init__(self, screen, x, y, w, h,num):
		self.name = "button"
                self.screen = screen
                self.rect = pygame.Rect(x,y,w,h)
                self.x = 400 + x
                self.y = 300 + y
                self.interactionrect = pygame.Rect(self.x - 4,self.y - 4,w + 8,h + 8)
                self.rect.move(self.x, self.y)
                self.rect.topleft = (self.x, self.y)
                self.rect.bottomright = (self.x + w, self.y + h)
                self.interactionrect = pygame.Rect(self.x - 4,self.y - 4,w + 8,h + 8)
                self.number = num

        def update(self,x,y,sleepy,items):
                msg = sleepy.font.render("You pushed the button next to the picture.",True,CLR_BROWN,CLR_BLACK)
                self.screen.blit(msg,MSG_BIG)
                pygame.display.flip() #Updates the display.
                pygame.time.wait(800)
                sleepy.buttons.append(self.number)
                sleepy.buttons.pop(0)
                dooropened = True
		bennyhill = True
                for i in range(0, 5):
                        if(sleepy.buttons[i] != i + 1):
                                dooropened = False
		if(dooropened and not sleepy.firedoor):
			items[0].used = dooropened
			items[0].update(x,y,sleepy,items)

        def draw(self,x,y):
                pass

class Oven(Wall):
        def __init__(self, screen, x, y, w, h):
		self.name = "oven"
                self.screen = screen
                self.rect = pygame.Rect(x,y,w,h)
                self.x = 400 + x
                self.y = 300 + y
                self.rect.move(self.x, self.y)
                self.rect.topleft = (self.x, self.y)
                self.rect.bottomright = (self.x + w, self.y + h)
                self.used = False
                self.interactionrect = pygame.Rect(self.x-4,self.y-4,w+8,h+8)

        def update(self,x,y,sleepy,items):
                if(self.used==False):
                        self.used=True
			try:
		        	sound = pygame.mixer.Sound("sounds/oven.wav")
			except pygame.error, message:
        			print "Cannot load sound: oven.wav"
			sound.play()
                        items.append(StaticItem(self.screen,739,2480,"ovendoor"))
                        items.append(Pig(self.screen,739,2580,"pig"))
                        
        def draw(self,x,y):
                        pass

class Crib(Wall):

        def update(self,x,y,sleepy,items):
                if(sleepy.teddyCount<5):
                        msg = sleepy.font.render("Teddy wants to be complete, you only have " + str(sleepy.teddyCount) + " parts of him.",True,CLR_BROWN,CLR_BLACK)
                        self.screen.blit(msg,MSG_BIG)
                        pygame.display.flip() #Updates the display.
                        pygame.time.wait(2000)
		elif(sleepy.teddyCount == 42):
			msg = sleepy.font.render("Teddy is asleep.",True,CLR_BROWN,CLR_BLACK)
			self.screen.blit(msg,MSG_BIG)
			pygame.display.flip()
			pygame.time.wait(500)
                else:
                        msg = sleepy.font.render("Teddy is alive again! A distant path has been opened.",True,CLR_BROWN,CLR_BLACK)
			sleepy.teddyCount = 42
                        self.screen.blit(msg,MSG_BIG)
                        items.append(StaticItem(self.screen,800,431,"teddy"))
                        pygame.display.flip() #Updates the display.
                        pygame.time.wait(2000)
                        while(len(sleepy.items)!=0):
                                sleepy.items.pop()

        def draw(self,x,y):
                pass

class EndGate(Wall):
	
	def update(self,x,y,sleepy,items):
		if(sleepy.teddyCount != 42):
			msg = sleepy.font.render("Rebuild what has been destroyed and the path will open.",True,CLR_BROWN,CLR_BLACK)
			self.screen.blit(msg,MSG_HUGE)
			pygame.display.flip()
			pygame.time.wait(2500)
		else:
			end1 = pygame.image.load("cards/rain.png").convert() #Intro screen image.
			self.screen.blit(end1,(0,0))
			pygame.display.flip()
			pygame.time.wait(4000)
			end1 = pygame.image.load("cards/leaves.png").convert() #Intro screen image.
			self.screen.blit(end1,(0,0))
			pygame.display.flip()
			pygame.time.wait(5000)
			end1 = pygame.image.load("cards/sparkle.png").convert() #Intro screen image.
			self.screen.blit(end1,(0,0))
			pygame.display.flip()
			pygame.time.wait(8000)
			end1 = pygame.image.load("cards/office_blur_big.png").convert() #Intro screen image.
			self.screen.blit(end1,(0,0))
			pygame.display.flip()
			pygame.time.wait(4000)
			pygame.quit()
			sys.exit(0)
	
	def draw(self,x,y):
		pass
