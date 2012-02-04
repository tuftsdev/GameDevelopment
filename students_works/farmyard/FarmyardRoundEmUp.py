import pygame, os, sys
from pygame.locals import *
from random import *

class Chick(pygame.sprite.Sprite):
    ''' A sprite for a chick '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()
    
    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, init_x, init_y, init_x_speed, init_y_speed, mute):
        ''' Initialize the sprite '''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image_1 = self.load_image("images/Chick1.png")
        self.image_2 = self.load_image("images/Chick2.png")
        self.image = self.image_1
        self.x = init_x
        self.y = init_y
        self.dx = init_x_speed
        self.dy = init_y_speed
        self.count = 0 # every 10 frames, change images

        if mute == False:
            alive = self.load_sound("sounds/babychicken.wav")
            alive.play()

        self.rect = self.image.get_rect() 
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)          
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
                
    def update(self):
        ''' Move the sprite; bounce off the walls '''
        if ((self.y + self.dy) >= self.screen.get_size()[1] - 95): # bottom side
            self.dy = self.dy * -1

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        # Move the bounding box too!
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        self.count += 1
        if self.count % 20 == 0: 
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1
        
        miss = False
        if (self.x < -self.image_w-5): # left side
            miss = True
        elif (self.y < -self.image_h-5): # top side
            miss = True
        elif (self.x > self.screen.get_size()[0] + self.image_w+5): # right side
            miss = True
        return miss
    
    def isOrb(self):
        return False
    
    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.x, self.y))

class Chicken(pygame.sprite.Sprite):
    ''' A sprite for a chicken '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()
     
    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, init_x, init_y, init_x_speed, init_y_speed, mute):
        ''' Initialize the sprite '''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image_1 = self.load_image("images/Chicken1.png")
        self.image_2 = self.load_image("images/Chicken2.png")
        self.image = self.image_1
        self.x = init_x
        self.y = init_y
        self.dx = init_x_speed
        self.dy = init_y_speed
        self.count = 0 # every 10 frames, change images
        if mute == False:
            alive = self.load_sound("sounds/chicken.wav")
            alive.play()

        self.rect = self.image.get_rect() 
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)          
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
                
    def update(self):
        ''' Move the sprite; bounce off the walls '''
        if ((self.y + self.dy) >= self.screen.get_size()[1] - 95): # bottom side
            self.dy = self.dy * -1

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        self.count += 1
        if self.count % 20 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1
                
        miss = False
        if (self.x < -self.image_w-5): # left side 
            miss = True
        elif (self.y < -self.image_h-5): # top side                                     
            miss = True
        elif (self.x > self.screen.get_size()[0] + self.image_w+5): # right side
            miss = True
        return miss

    def isOrb(self):
        return False
    
    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.x, self.y))

class Cow(pygame.sprite.Sprite):
    ''' A sprite for a cow '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()

    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, init_x, init_y, init_x_speed, init_y_speed, mute):
        ''' Initialize the sprite '''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image_1 = self.load_image("images/Cow1.png")
        self.image_2 = self.load_image("images/Cow2.png")
        self.image = self.image_1
        self.x = init_x
        self.y = init_y
        self.dx = init_x_speed
        self.dy = init_y_speed
        self.count = 0 # every 10 frames, change images
        
        if mute == False:
            alive = self.load_sound("sounds/cow.wav")
            alive.play()

        self.rect = self.image.get_rect()
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def update(self):
        ''' Move the sprite; bounce off the walls '''
        if ((self.y + self.dy) >= self.screen.get_size()[1] - 95): # bottom side    
            self.dy = self.dy * -1

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        # Move the bounding box too!                                                    
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        self.count += 1
        if self.count % 20 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1

        miss = False 
        if (self.x < -self.image_w-5): # left side                                 
            miss = True
        elif (self.y < -self.image_h-5): # top side                         
            miss = True
        elif (self.x > self.screen.get_size()[0] + self.image_w+5): # right side
            miss = True
        return miss
    
    def isOrb(self):
        return False

    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.x, self.y))

class Duck(pygame.sprite.Sprite):
    ''' A sprite for a duck '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()

    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, init_x, init_y, init_x_speed, init_y_speed, mute):
        ''' Initialize the sprite '''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image_1 = self.load_image("images/Duck1.png")
        self.image_2 = self.load_image("images/Duck2.png")
        self.image = self.image_1
        self.x = init_x
        self.y = init_y
        self.dx = init_x_speed
        self.dy = init_y_speed
        self.count = 0 # every 10 frames, change images
        
        if mute == False:
            alive = self.load_sound("sounds/duck.wav")
            alive.play()
    
        self.rect = self.image.get_rect() 
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)          
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
                
    def update(self):
        ''' Move the sprite; bounce off the walls '''
        if ((self.y + self.dy) >= self.screen.get_size()[1] - 95):
            self.dy = self.dy * -1

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        self.count += 1
        if self.count % 20 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1

        miss = False
        if (self.x < -self.image_w-5): # left side
            miss = True
        elif (self.y < -self.image_h-5): # top side
            miss = True
        elif (self.x > self.screen.get_size()[0] + self.image_w+5): # right side
            miss = True
        return miss

    def isOrb(self):
        return False

    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.x, self.y))

class FlyingPig(pygame.sprite.Sprite):
    ''' A sprite for a flying pig '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()

    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, init_x, init_y, init_x_speed, init_y_speed, mute):
        ''' Initialize the sprite '''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image_1 = self.load_image("images/FlyingPig1.png")
        self.image_2 = self.load_image("images/FlyingPig2.png")
        self.image = self.image_1
        self.x = init_x
        self.y = init_y
        self.dx = init_x_speed
        self.dy = init_y_speed
        self.count = 0 # every 10 frames, change images

        if mute == False:
            alive = self.load_sound("sounds/flyingpig.wav")
            alive.play()

        self.rect = self.image.get_rect() 
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)          
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
                
    def update(self):
        ''' Move the sprite; bounce off the walls '''
        if ((self.y + self.dy) >= self.screen.get_size()[1] - 95):
            self.dy = self.dy * -1

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        self.count += 1
        if self.count % 20 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1

        miss = False
        if (self.x < -self.image_w-5): # left side
            miss = True
        elif (self.y < -self.image_h-5): # top side
            miss = True
        elif (self.x > self.screen.get_size()[0] + self.image_w+5): # right side
            miss = True
        return miss

    def isOrb(self):
        return False

    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.x, self.y))

class Goose(pygame.sprite.Sprite):
    ''' A sprite for a goose '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()
    
    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, init_x, init_y, init_x_speed, init_y_speed, mute):
        ''' Initialize the sprite '''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image_1 = self.load_image("images/Goose1.png")
        self.image_2 = self.load_image("images/Goose2.png")
        self.image = self.image_1
        self.x = init_x
        self.y = init_y
        self.dx = init_x_speed
        self.dy = init_y_speed
        self.count = 0 # every 10 frames, change images

        if mute == False:
            alive = self.load_sound("sounds/goose.wav")
            alive.play()

        self.rect = self.image.get_rect() 
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)          
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)
                
    def update(self):
        ''' Move the sprite; bounce off the walls '''
        if ((self.y + self.dy) >= self.screen.get_size()[1] - 95):
            self.dy = self.dy * -1

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        self.count += 1
        if self.count % 20 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1

        miss = False
        if (self.x < -self.image_w-5): # left side
            miss = True
        elif (self.y < -self.image_h-5): # top side
            miss = True
        elif (self.x > self.screen.get_size()[0] + self.image_w+5): # right side
            miss = True
        return miss

    def isOrb(self):
        return False

    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.x, self.y))

class Pig(pygame.sprite.Sprite):
    ''' A sprite for a pig '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()

    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, init_x, init_y, init_x_speed, init_y_speed, mute):
        ''' Initialize the sprite '''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image_1 = self.load_image("images/Pig1.png")
        self.image_2 = self.load_image("images/Pig2.png")
        self.image = self.image_1
        self.x = init_x
        self.y = init_y
        self.dx = init_x_speed
        self.dy = init_y_speed
        self.count = 0 # every 10 frames, change images

        if mute == False:
            alive = self.load_sound("sounds/pig.wav")
            alive.play()
            
        self.rect = self.image.get_rect() 
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)          
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def update(self):
        ''' Move the sprite; bounce off the walls '''
        if ((self.y + self.dy) >= self.screen.get_size()[1] - 95):
            self.dy = self.dy * -1

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        self.count += 1
        if self.count % 20 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1

        miss = False
        if (self.x < -self.image_w-5): # left side
            miss = True
        elif (self.y < -self.image_h-5): # top side
            miss = True
        elif (self.x > self.screen.get_size()[0] + self.image_w+5): # right side
            miss = True
        return miss
        
    def isOrb(self):
        return False

    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.x, self.y))

class Orb(pygame.sprite.Sprite):
    ''' A sprite for an orb power up '''

    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()

    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, init_x, init_y, init_x_speed, init_y_speed, mute):
        ''' Initialize the sprite '''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = self.load_image("images/Orb.png")
        self.x = init_x
        self.y = init_y
        self.dx = init_x_speed
        self.dy = init_y_speed
        self.dy = init_y_speed

        self.rect = self.image.get_rect()
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def update(self):
        ''' Move the sprite; bounce off the walls '''
        if ((self.y + self.dy) >= self.screen.get_size()[1] - 95):
            self.dy = self.dy * -1

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        miss = False
        if (self.x < -self.image_w-5): # left side
            miss = True
        elif (self.y < -self.image_h-5): # top side
            miss = True
        elif (self.x > self.screen.get_size()[0] + self.image_w+5): # right side
            miss = True
        return miss

    def isOrb(self):
        return True

    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.x, self.y))

class LeftFarmer(pygame.sprite.Sprite):
    ''' A sprite for the left Farmer '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()

    def rectBox(self):
        self.rect = self.image.get_rect()
        self.image_w, self.image_h  = self.image.get_size()
        self.rect.move(self.x, self.y)          
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def __init__(self, screen, x, y):
        ''' Initialization '''
        self.image_1reg  = self.load_image("images/FarmerLeft1.png")
        self.image_2reg  = self.load_image("images/FarmerLeft2.png")
        self.image_1pwr  = self.load_image("images/FarmerLeft1pwr.png")
        self.image_2pwr  = self.load_image("images/FarmerLeft2pwr.png")
        
        self.image_1 = self.image_1reg
        self.image_2 = self.image_2reg
        self.image   = self.image_1
        self.screen  = screen
        self.x = x
        self.y = y
        self.count = 0 # every 10 frames, change images
        self.rectBox()
        self.powerup = False
        self.poweruptimer = 0

    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.rect.left, self.rect.top))

    def update(self, SCREEN_HEIGHT):
        #self.rectBox()

        ''' Correct farmer positions if it's going out of window '''
        if self.rect.top < self.image_w:
            self.rect.top = self.image_w
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        
        if self.powerup:
            if self.poweruptimer > 0:
                self.poweruptimer -= 1
            else:
                self.powerup = False

    def powerUp(self):
        self.poweruptimer = 400
        self.powerup = True

    def mouseMotion(self, event):
        ''' Detect Mouse Motion '''
        self.rect.centery  = event.pos[1]

        if self.powerup == True:
            self.image_1 = self.image_1pwr
            self.image_2 = self.image_2pwr
        else:
            self.image_1 = self.image_1reg
            self.image_2 = self.image_2reg

        self.count += 1
        if self.count % 3 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1

class RightFarmer(pygame.sprite.Sprite):
    ''' A sprite for the left Farmer '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()

    def rectBox(self):
        self.rect = self.image.get_rect()
        self.image_w, self.image_h  = self.image.get_size()
        self.rect.move(self.x, self.y)          
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def __init__(self, screen, x, y):
        ''' Initialization '''
        self.image_1reg = self.load_image("images/FarmerRight1.png")
        self.image_2reg = self.load_image("images/FarmerRight2.png")
        self.image_1pwr = self.load_image("images/FarmerRight1pwr.png")
        self.image_2pwr = self.load_image("images/FarmerRight2pwr.png")

        self.image_1 = self.image_1reg
        self.image_2 = self.image_2reg
        self.image  = self.image_1
        self.screen = screen
        self.x = x
        self.y = y
        self.count = 0 # every 10 frames, change images
        self.rectBox()
        self.powerup = False
        self.poweruptimer = 0

    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.rect.left, self.rect.top))

    def update(self, SCREEN_HEIGHT):
        #self.rectBox()

        ''' Correct farmer position if it's going out of window '''
        if self.rect.top < self.image_w:
            self.rect.top = self.image_w
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        
        if self.powerup:
            if self.poweruptimer > 0:
                self.poweruptimer -= 1
            else:
                self.powerup = False

    def powerUp(self):
        self.poweruptimer = 400
        self.powerup = True

    def mouseMotion(self, event):
        ''' Detect Mouse Motion '''
        self.rect.centery = event.pos[1]

        if self.powerup == True:
            self.image_1 = self.image_1pwr
            self.image_2 = self.image_2pwr
        else:
            self.image_1 = self.image_1reg
            self.image_2 = self.image_2reg

        self.count += 1
        if self.count % 3 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1

class TopFarmer(pygame.sprite.Sprite):
    ''' A sprite for the left Farmer '''
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()

    def rectBox(self):
        self.rect = self.image.get_rect()
        self.image_w, self.image_h  = self.image.get_size()
        self.rect.move(self.x, self.y)          
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def __init__(self, screen, x, y):
        ''' Initialization '''
        self.image_1reg = self.load_image("images/FarmerTop1.png")
        self.image_2reg = self.load_image("images/FarmerTop2.png")
        self.image_1pwr = self.load_image("images/FarmerTop1pwr.png")
        self.image_2pwr = self.load_image("images/FarmerTop2pwr.png")
        
        self.image_1 = self.image_1reg
        self.image_2 = self.image_2reg
        self.image   = self.image_1
        self.screen  = screen
        self.x = x
        self.y = y
        self.count = 0 # every 10 frames, change images
        self.rectBox()
        self.powerup = False
        self.poweruptimer = 0

    def draw(self):
        ''' Draw the sprite on the screen '''
        self.screen.blit(self.image, (self.rect.left, self.rect.top))

    def update(self, SCREEN_WIDTH):
        #self.rectBox()

        ''' Correct farmer position if it's going out of window '''
        if self.rect.left < self.image_h:
            self.rect.left = self.image_h
        elif self.rect.right >= SCREEN_WIDTH - self.image_h:
            self.rect.right = SCREEN_WIDTH - self.image_h
        
        if self.powerup:
            if self.poweruptimer > 0:
                self.poweruptimer -= 1
            else:
                self.powerup = False

    def powerUp(self):
        self.poweruptimer = 400
        self.powerup = True

    def mouseMotion(self, event):
        ''' Detect Mouse Motion '''
        self.rect.centerx  = event.pos[0]

        if self.powerup == True:
            self.image_1 = self.image_1pwr
            self.image_2 = self.image_2pwr
        else:
            self.image_1 = self.image_1reg
            self.image_2 = self.image_2reg

        self.count += 1
        if self.count % 3 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            else:
                self.image = self.image_1

##################################################
# The main component of the game                 #
##################################################

def quit():
    ''' Self explanatory '''
    pygame.quit()
    sys.exit(0)

def pause():
    drawpause()
    while 1:
        ''' Pause Until Input is Given '''
        e = pygame.event.wait()
        if e.type in (pygame.QUIT, pygame.KEYDOWN):
            return

def drawpause():
    ''' Display Paused Text '''
    font = pygame.font.Font(None, 48)
    text1 = font.render("PAUSED", 1, (10, 10, 10))
    text1pos = text1.get_rect()
    text1pos.centerx = screen.get_rect().centerx
    text1pos.centery = screen.get_rect().centery
    screen.blit(text1, text1pos)
    font = pygame.font.Font(None, 36)
    text2 = font.render("Press Any Key to Continue", 1, (10, 10, 10))
    text2pos = text2.get_rect()
    text2pos.centerx = screen.get_rect().centerx
    text2pos.centery = screen.get_rect().centery + 50
    screen.blit(text2, text2pos)
    pygame.display.flip()

def drawmute():
    ''' Display Muted Text '''
    font = pygame.font.Font(None, 24)
    text = font.render("MUTED (M to unmute)", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.topright = (screen.get_rect().topright[0] - 10, screen.get_rect().topright[1] + 10)
    screen.blit(text, textpos)
    pygame.display.flip()

def load_image(image_name):
    ''' The proper way to load an image '''
    try:
        image = pygame.image.load(image_name)
    except pygame.error, message:
        print "Cannot load image: " + image_name
        raise SystemExit, message
    return image.convert_alpha()

def load_sound(sound_name):
    try:
        sound = pygame.mixer.Sound(sound_name)
    except pygame.error, message:
        print "Cannot load sound: " + sound_name
        raise SystemExit, message
    return sound

def addSprite(sprites, screen, init_x, init_y, speed_x, speed_y, mute):
    animal = choice(range(21))
    if animal in range(0,3):   # chick
        sprites.append(Chick(screen, init_x, init_y, speed_x, speed_y, mute))
    elif animal in range(3,6): # chicken
        sprites.append(Chicken(screen, init_x, init_y, speed_x, speed_y, mute))
    elif animal in range(6,9): # cow
        sprites.append(Cow(screen, init_x, init_y, speed_x, speed_y, mute))
    elif animal in range(9,12): # duck
        sprites.append(Duck(screen, init_x, init_y, speed_x, speed_y, mute))
    elif animal in range(12,14): # flying pig
        sprites.append(FlyingPig(screen, init_x, init_y, 1.5*speed_x, 1.5*speed_y, mute))
    elif animal in range(14,17): # goose
        sprites.append(Goose(screen, init_x, init_y, speed_x, speed_y, mute))
    elif animal in range(17,20): # pig
        sprites.append(Pig(screen, init_x, init_y, speed_x, speed_y, mute))
    elif animal == 20: # orb
        sprites.append(Orb(screen, init_x, init_y, .5*speed_x, .5*speed_y, mute))
    return sprites

def printScores(scores):
    font = pygame.font.Font(None, 75)
    COLOR = (225,225,225)
    length = len(scores)
    curScore = str(scores[length-1])
    curScore_text = font.render(curScore, True, COLOR)
    screen.blit(curScore_text,(580, 100))
    temp = []
    for i in range(length):
        temp.append(scores[i])
    temp.sort()
    temp.reverse()
    font = pygame.font.Font(None, 35)
    first = True
    scoreFile = open('.highscores', 'w')
    for i in range(min(length,9)):
        highScore = str(temp[i])
        scoreFile.write(highScore + '\n')
        if highScore == curScore and first:
            COLOR = (40,40,40)
            first = False
        else:
            COLOR = (115,115,115)
        highScore_text = font.render(highScore, True, COLOR)
        screen.blit(highScore_text,(550, 230 + 33.55*i))
    scoreFile.close()
    font = pygame.font.Font(None, 28)
    
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SPEED = 5
BALL_WIDTH_HEIGHT = 16
BACKGROUND_COLOR = (255, 255, 255)
SPRITE_IMAGES = ['images/Goose1.png', 'images/Pig1.png', 'images/Chick1.png',
                 'images/Chicken1.png', 'images/Cow1.png', 'images/Duck1.png',
                 'images/FlyingPig1.png']
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Farmer Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)
counter = 0
lives = 10
INTRO_IMAGE = load_image("images/FarmIntro.png")
BACKGROUND_IMAGE = load_image("images/Farmbg.png")
HIGHSCORE_IMAGE = load_image("images/HighScore.png")

screen_id = 0

#Score file input
scores = []
checker = 0
try:
    file = open('.highscores', 'r+')
    for line in file:
        score = line.split()
        score = score[0]
        scores.append(int(score))
    file.close()
    checker = 1
except IOError:
    print 'A .highscores file did not exist! A new highscores file will be created at the completion of this game.'
if checker == 0:
    for x in range(8):
        scores.append(0)

# Create the sprites
sprites = []
LFarmer = LeftFarmer (screen,   8, 200)
RFarmer = RightFarmer(screen, 780, 200)
TFarmer = TopFarmer  (screen, 358,   8)

# Create sounds
breakout = load_sound("sounds/dooropen.wav")
intro = load_sound("sounds/titlesong.wav")
gameover = load_sound("sounds/gameover.wav")
soundcheck = 0
mute = False

pygame.time.set_timer(USEREVENT + 1, 1000) # Custom event
pygame.time.set_timer(USEREVENT + 2, 5000) # Custom event

# Game loop
while True:
    # Redraw the background
    screen.fill(BACKGROUND_COLOR)

    if screen_id == 0: # intro screen
        if soundcheck != 1:
            intro.play()
            soundcheck = 1
        screen.blit(INTRO_IMAGE, (0,0))
    elif screen_id == 1: # game screen
        if soundcheck != 2:
            breakout.play()
            soundcheck = 2
        screen.blit(BACKGROUND_IMAGE, (0,0))
        # Update and redraw all sprites
        for sprite in sprites:
            missed = sprite.update()
            if missed:    
                sprites.remove(sprite)
                lives -= 1
                if lives == 0:
                    screen_id = 2
            sprite.draw()
            if pygame.sprite.collide_rect(LFarmer, sprite):
                powerup = sprite.isOrb()
                sprites.remove(sprite)
                scores[len(scores)-1] += 1
                if powerup:
                    LFarmer.powerUp()
            if pygame.sprite.collide_rect(RFarmer, sprite):
                powerup = sprite.isOrb()
                sprites.remove(sprite)
                scores[len(scores)-1] += 1
                if powerup:
                    RFarmer.powerUp()
            if pygame.sprite.collide_rect(TFarmer, sprite):
                powerup = sprite.isOrb()
                sprites.remove(sprite)
                scores[len(scores)-1] += 1
                if powerup:
                    TFarmer.powerUp()
        
        # correct paddle position if it's going out of window
        LFarmer.update(SCREEN_HEIGHT)
        RFarmer.update(SCREEN_HEIGHT)
        TFarmer.update(SCREEN_WIDTH)
        
        LFarmer.draw()
        RFarmer.draw()
        TFarmer.draw()

        lives_str = "Lives: " + str(lives)
        score_str = "Score: " + str(scores[len(scores)-1])
        lives_text = font.render(lives_str, True, (255,255,255))
        score_text = font.render(score_str, True, (255, 255, 255))
        screen.blit(score_text,((SCREEN_WIDTH/2)-2*font.size(lives_str)[0]/2 - 10,
                                 SCREEN_HEIGHT - 40))
        screen.blit(lives_text,((SCREEN_WIDTH/2)+2*font.size(score_str)[0]/2 - 10,
                                 SCREEN_HEIGHT - 40))
    
    elif screen_id == 2: # high score screen
        if soundcheck != 3:
            gameover.play()
            soundcheck = 3
        screen.blit(HIGHSCORE_IMAGE, (0,0))
        printScores(scores)
    
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:          
            quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
            elif event.key == K_p:
                pause()
            elif event.key == K_m:
                if breakout.get_volume() != 0:
                    breakout.set_volume(0)
                    intro.set_volume(0)
                    gameover.set_volume(0)
                    mute = True
                else:
                    breakout.set_volume(1)
                    intro.set_volume(1)
                    gameover.set_volume(1)
                    mute = False
            elif event.key == K_SPACE:
                if screen_id == 0 or screen_id == 2:
                    MIN_SPEED = 3.0
                    MAX_SPEED = 6.0
                    lives = 3
                    scores.append(0)
                    screen_id = 1
                    intro.stop()
                    for sprite in sprites:
                        sprites.remove(sprite)
                else:
                    pause()
        
        # Control the paddles with the mouse
        elif event.type == pygame.MOUSEMOTION:
            LFarmer.mouseMotion(event)
            RFarmer.mouseMotion(event) 
            TFarmer.mouseMotion(event)
        elif screen_id == 1:
            if event.type == USEREVENT + 1:
                mult_x = choice([-1,1])
                mult_y = choice([-1,1])
                speed_x = mult_x*uniform(MIN_SPEED, MAX_SPEED)
                speed_y = mult_y*uniform(MIN_SPEED, MAX_SPEED)
                init_x = SCREEN_WIDTH/2
                init_y = SCREEN_HEIGHT/2
                sprites = addSprite(sprites, screen, init_x, init_y,
                                    speed_x, speed_y, mute)
            if event.type == USEREVENT + 2:
                MIN_SPEED = MIN_SPEED + .2
                MAX_SPEED = MAX_SPEED + .2
    
    if mute:
        drawmute()

    # Update screen and wait 20 milliseconds
    pygame.display.flip()
    pygame.time.delay(20)
