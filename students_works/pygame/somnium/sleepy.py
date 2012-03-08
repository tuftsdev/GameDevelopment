import pygame, os, sys, random
from const import *
from pygame.locals import *

__name__ = "sleepy"

class Sleepy(pygame.sprite.Sprite):
#SSSSSSSSSSSSLLLLLLLLEEEEEEEEEEEEEEEEEEEEEEEPPPPPPYYYYYYYYYY!        
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
                self.image = self.load_image("sprites/chardown.png")
                self.imageCount = 0
                self.screen = screen
                self.posx = x #The movement from the initial location of the player.
                self.posy = y
                self.movement = False
                self.x = 400
                self.y = 300
                self.items = []
                self.rect = self.image.get_rect()
                self.image_w, self.image_h = self.image.get_size()
                self.rect.move(self.x, self.y)
                self.rect.topleft = (self.x, self.y)
                self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
                self.dir = "down"
                #Loads the images here so that they don't get loaded every time, the sprite is updated.
                self.down = [self.load_image("sprites/char1down.png"),
                               self.load_image("sprites/chardown.png"),
                             self.load_image("sprites/char2down.png"),
                             self.load_image("sprites/chardown.png")]
                self.up = [self.load_image("sprites/char1up.png"),
                               self.load_image("sprites/charup.png"),
                             self.load_image("sprites/char2up.png"),
                             self.load_image("sprites/charup.png")]
                self.left = [self.load_image("sprites/char1left.png"),
                               self.load_image("sprites/charleft.png"),
                             self.load_image("sprites/char2left.png"),
                             self.load_image("sprites/charleft.png")]
                self.right = [self.load_image("sprites/char1right.png"),
                               self.load_image("sprites/charright.png"),
                             self.load_image("sprites/char2right.png"),
                             self.load_image("sprites/charright.png")]
		self.font = pygame.font.Font(None,30)
		self.buttons = [0,0,0,0,0,0]
		self.firedoor = False
		self.bucketfull = False
		self.teddyCount = 0

        def draw(self):
                self.screen.blit(self.image, (self.x, self.y)) #Draws the sprite.
                temp = []
                if(self.dir=="down"):
                        temp = self.down
                elif(self.dir=="up"):
                        temp = self.up
                elif(self.dir=="right"):
                        temp = self.right
                elif(self.dir=="left"):
                        temp = self.left
                if(self.movement==True):
                        if(temp[self.imageCount/30]!=None and self.imageCount < 119):
                                self.image = temp[self.imageCount/30]
                        else:
                                self.imageCount = -1
                        self.imageCount +=1
                else:
                        self.image = temp[1] #Load standard image if no movement occurs.
                        self.imageCount = 0

        def update(self):
                if(self.movement):
                        if self.dir == "up":
                                self.posy = self.posy - 4
                        elif self.dir == "down":
                                self.posy = self.posy + 4
                        elif self.dir == "left":
                                self.posx = self.posx - 4
                        elif self.dir == "right":
                                self.posx = self.posx + 4
                #This probably should be 2 or there will be collision issues. Consult me if you want to change.
                self.rect.move(self.posx + self.x, self.posy + self.y)
                self.rect.topleft = (self.posx+ self.x, self.posy + self.y)
                self.rect.bottomright = (self.posx + self.x + self.image_w, self.posy + self.y + self.image_h)

