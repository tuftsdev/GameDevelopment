import pygame, os, sys, random
from pygame.locals import *
from const import *

__name__ = "items"

class Item(pygame.sprite.Sprite):

        def load_image(self, image_name):
                try:
                        image = pygame.image.load(image_name)
                except pygame.error, message:
                        print "Cannot load image: " + image_name
                        return None
                return image.convert_alpha()

        def __init__(self, screen, x, y, name):
                self.image = self.load_image("items/" + name + ".png")
                self.screen = screen
                self.rect = self.image.get_rect()
                self.x = 400 + x
                self.y = 300 + y
                self.image_w, self.image_h = self.image.get_size()
                self.interactionrect = pygame.Rect(self.x - 4,self.y - 4,self.image_w + 8, self.image_h + 8)
                self.rect.move(self.x, self.y)
                self.rect.topleft = (self.x, self.y)
                self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)  
                self.used = False
                self.name = name

        def draw(self,x,y):
                if self.used == False:
                         self.screen.blit(self.image, (x, y))

        def update(self,x,y,sleepy,items):
                self.used = True
                sleepy.items.append(self.name)
                msg = sleepy.font.render("You got " + self.name +".",True,CLR_BROWN,CLR_BLACK)
		self.pick_up()
                self.screen.blit(msg,MSG_SMALL)
                pygame.display.flip()
                pygame.time.wait(750)
                items.remove(self)
	
	def pick_up(self):
		try:
	   		pickup = pygame.mixer.Sound("sounds/item.wav")
		except:
			print "Cannot load sound: item.wav"
		pickup.play()

class Door(Item):

	def update(self,x,y,sleepy,items):
		self.used = True
		msg = sleepy.font.render(TXT_DOOROPEN,True,CLR_BROWN,CLR_BLACK)
		self.screen.blit(msg,MSG_SMALL)
		pygame.display.flip()
		try:
        		doorsound = pygame.mixer.Sound("sounds/door.ogg")
		except pygame.error, message:
        		print "Cannot load sound: door.wav"
		doorsound.play()
		pygame.time.wait(1000)
		items.remove(self)

class WingDoor(Item):

        def update(self,x,y,sleepy,items):
                for s in sleepy.items:
                        if(s=="wings"):
                                self.used = True
                                msg = sleepy.font.render(TXT_DOOROPEN,True,CLR_BROWN,CLR_BLACK)
                                self.screen.blit(msg,MSG_SMALL)
                                pygame.display.flip()
				pygame.time.wait(1000)
                                items.remove(self)
				sleepy.items.remove("wings")
				try:
        				doorsound = pygame.mixer.Sound("sounds/door.ogg")
				except pygame.error, message:
        				print "Cannot load sound: door.wav"
				doorsound.play()
                if(self.used == False):
                        msg = sleepy.font.render(TXT_DOORLOCKED + "is adorned with two wing impressions...",True,CLR_BROWN,CLR_BLACK)
                        self.screen.blit(msg,MSG_BIG)
                        pygame.display.flip()
                        pygame.time.wait(2000)

class FireDoor(Item):

	def update(self,x,y,sleepy,items):
		if(self.used == False):
			msg = sleepy.font.render(TXT_DOORLOCKED + "is adorned with the motif of a book...",True,CLR_BROWN,CLR_BLACK)
			self.screen.blit(msg,MSG_BIG)
			pygame.display.flip()
			pygame.time.wait(2000)
		else:
			msg = sleepy.font.render(TXT_DOORSOUND,True,CLR_BROWN,CLR_BLACK)
			self.screen.blit(msg,MSG_BIG)
			pygame.display.flip()
			try:
        			doorsound = pygame.mixer.Sound("sounds/door.ogg")
			except pygame.error, message:
        			print "Cannot load sound: door.wav"
			doorsound.play()
			pygame.time.wait(1000)
			items.remove(self)
			sleepy.firedoor = True

class KeyDoor(Item):

	def update(self,x,y,sleepy,items):
		for s in sleepy.items:
			if(s == "key"):
				self.used = True
				msg = sleepy.font.render(TXT_DOOROPEN,True,CLR_BROWN,CLR_BLACK)
                                self.screen.blit(msg,MSG_SMALL)
                                pygame.display.flip()
				pygame.time.wait(1000)
                                items.remove(self)
				try:
        				doorsound = pygame.mixer.Sound("sounds/door.ogg")
				except pygame.error, message:
        				print "Cannot load sound: door.wav"
				doorsound.play()
		if(self.used == False):
                        msg = sleepy.font.render(TXT_DOORLOCKED + "looks rusty and old...",True,CLR_BROWN,CLR_BLACK)
                        self.screen.blit(msg,MSG_BIG)
                        pygame.display.flip()
                        pygame.time.wait(2000)

class Crate(Item):

        def update(self,x,y,sleepy,items):
                if(self.used==False):
                        self.x+=60
                        self.used=True
                        self.rect = self.rect.move(60,0)
                        self.interactionrect = self.interactionrect.move(60,0)
                        msg = sleepy.font.render("You moved the crate.",True,CLR_BROWN,CLR_BLACK)
                        self.screen.blit(msg,MSG_SMALL)
                        pygame.display.flip()
                        pygame.time.wait(500)
        def draw(self,x,y):
                self.screen.blit(self.image, (x,y))

class StaticItem(Item):

        def update(self,x,y,sleepy,items):
                pass

class Popup(Item):

        def __init__(self,screen,x,y,w,h,name):
                self.image = self.load_image("items/" + name + ".png")
                self.screen = screen
                self.rect = pygame.Rect(400 + x,300 + y,w,h)
                self.x = 400 + x
                self.y = 300 + y
                self.image_w, self.image_h = self.image.get_size()
                self.drawx = (800 - self.image_w) / 2
                self.drawy = (600 - self.image_h) / 2
                self.interactionrect = pygame.Rect(self.x - 4,self.y - 4,w + 8, h + 8)
                self.rect.move(self.x,self.y)
                self.used = False
                self.name = name

        def draw(self,x,y):
                pass

        def update(self,x,y,sleepy,items):
                if(self.used == False):
                        self.used = True
			try:
	        		sound = pygame.mixer.Sound("sounds/popup.wav")
			except pygame.error, message:
        			print "Cannot load sound: popup.wav"
			sound.play()
                        while(self.used):
                                self.screen.blit(self.image,(self.drawx,self.drawy))
                                msg = sleepy.font.render("Press enter to continue.",True,CLR_BROWN,CLR_BLACK)
                                self.screen.blit(msg,MSG_TOPRIGHT)
                                pygame.display.flip() #Updates the display.
                                for event in pygame.event.get():
					if(event.type == KEYDOWN):
	                                        if(event.key == K_RETURN):
	       	                                        self.used = False
						else:
							pass
					else:
						pass

class Sink(Item):

	def __init__(self,screen,x,y,w,h):
		self.image = None
		self.screen = screen
		self.rect = pygame.Rect(400 + x,300 + y,w,h)
		self.x = 400 + x
		self.y = 300 + y
		self.image_w,self.image_h = (None,None)
		self.interactionrect = pygame.Rect(self.x - 4,self.y - 4,w + 8, h + 8)
		self.rect.move(self.x,self.y)
		self.used = False
		self.name = "sink"
	
	def draw(self,x,y):
		pass
	
	def update(self,x,y,sleepy,items):
		try:
	        	sound = pygame.mixer.Sound("sounds/faucet.wav")
		except pygame.error, message:
        		print "Cannot load sound: faucet.wav"
		sound.play()
		msg = sleepy.font.render(TXT_SINK_INTERACT,True,CLR_BROWN,CLR_BLACK)
		self.screen.blit(msg,MSG_BIG)
		pygame.display.flip()
		pygame.time.wait(750)

class Cage(Item):

        def update(self,x,y,sleepy,items):
                triedNumber = False
                numbers = [K_1,K_2,K_2,K_5,K_9,K_2]
                temp = [K_4,K_2,K_4,K_2,K_4,K_2]
                msg = sleepy.font.render(TXT_LOCK_ASHES,True,CLR_BROWN,CLR_BLACK)
                self.screen.blit(msg,MSG_HUGE)
                pygame.display.flip()
                pygame.time.wait(2800)
                msg = sleepy.font.render(TXT_6CODE_INPUT,True,CLR_BROWN,CLR_BLACK)
                self.screen.blit(msg,MSG_HUGE)
                pygame.display.flip() #Updates the display.
                count = 0
                while(not triedNumber):
                        for event in pygame.event.get():
                                if(event.type==KEYDOWN):
                                        if (event.key == K_RETURN):
                                                triedNumber=True
                                                if(temp==numbers):
                                                        msg = sleepy.font.render("You would remember that day.                             ",True,CLR_BROWN,CLR_BLACK)
                                                        self.screen.blit(msg,MSG_HUGE)
                                                        pygame.display.flip() # Updates the display
                                                        pygame.time.wait(1000)
                                                        items.remove(self)
                                                else:
                                                        msg = sleepy.font.render("How can you forget?                                  ",True,CLR_BROWN,CLR_BLACK)
                                                        self.screen.blit(msg,MSG_HUGE)
                                                        pygame.display.flip() # Updates the display
                                                        pygame.time.wait(1000)
                                        temp.pop(0)
                                        temp.append(event.key)
                                        count = 0
                                else:
                                        pass

class Teddypart(Item):

        def update(self,x,y,sleepy,items):
                self.used = True
                msg = sleepy.font.render("You got " + self.name +".",True,CLR_BROWN,CLR_BLACK)
		self.pick_up()
                self.screen.blit(msg,MSG_SMALL)
                pygame.display.flip()
                sleepy.teddyCount += 1
                pygame.time.wait(750)
                items.remove(self)
