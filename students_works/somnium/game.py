import pygame, os, sys, random
from pygame.locals import *
from const import *
from monster import *
from sleepy import *
from items import *
from walls import *

def quit():
        #It really DOES quit the program. Sometimes.
        pygame.quit()
        sys.exit(0)

# Initializes the pygame modules
def level1():
        sleepy = Sleepy(screen,1080,2620) # Game start spawn
        #sleepy = Sleepy(screen,800,700) # Toy room spawn, for testing
        #sleepy = Sleepy(screen,2140,1780) # Storage hall spawn, for testing
        #sleepy = Sleepy(screen,1660,1420) # Fire room spawn, for testing
        
        nodes = [] # Invisible nodes, for guiding the movement of the AI
        nodes.append([450,210])   # Node 0
        nodes.append([450,2830])  # Node 1
        nodes.append([450,2050])  # Node 2
        nodes.append([1540,2020]) # Node 3
        nodes.append([1540,1790]) # Node 4
        nodes.append([2280,1790]) # Node 5
        nodes.append([2280,210])  # Node 6

        walls=[] #Invisible walls, we decided not to have every object at the background as a sprite. But the player should still bump into them.
        walls.append(Wall(screen,328,44,2052,60))
        walls.append(Wall(screen,2380,103,60,442))
        walls.append(Wall(screen,2380,546,556,2))
        walls.append(Wall(screen,2936,546,2,198))
        walls.append(Wall(screen,2380,744,556,60))
        walls.append(Wall(screen,2380,744,60,1156))
        walls.append(Wall(screen,328,2930,204,60))
        walls.append(Wall(screen,268,100,60,2830))
        walls.append(Wall(screen,1895,2495,490,60))     # Storage room bottom
        walls.append(Wall(screen,1785,1895,105,660))    # Storage room left
        walls.append(Wall(screen,2385,2000,55,555))     # Storage room right
        walls.append(Wall(screen,1890,1895,200,110))    # Bottom corridor bottom right / Storage room top left
        walls.append(Wall(screen,2185,1895,255,110))    # Bottom corridor bottom far right / Storage room top right
        walls.append(Wall(screen,655,2150,1130,280))    # Bottom corridor bottom left
        walls.append(Wall(screen,525,2150,130,435))     # Left corridor right upper / Kitchen left upper
        walls.append(Wall(screen,525,2675,130,310))     # Left corridor right lower / Kitchen left lower
        walls.append(Wall(screen,1200,2430,60,390))     # Kitchen right
        walls.append(Wall(screen,655,2810,545,60))      # Kitchen bottom
        walls.append(Wall(screen,710,300,928,120))      # Toy room top / Paints room top left
        walls.append(Wall(screen,1735,300,335,120))     # Paintings room top right
        walls.append(Wall(screen,2070,300,120,675))     # Paintings room right
        walls.append(Wall(screen,1205,975,590,120))     # Paintings room bottom left / Fire room top left
        walls.append(Wall(screen,1910,975,275,120))     # Paintings room bottom right / Fire room top right
        walls.append(Wall(screen,590,300,120,660))      # Toy room left upper
        walls.append(Wall(screen,585,1030,120,130))     # Toy room left lower
        walls.append(Wall(screen,1205,420,120,215))     # Toy room right upper / Paintings room right upper
        walls.append(Wall(screen,1205,740,120,235))     # Toy room right lower / Paintings room right lower
        walls.append(Wall(screen,640,1150,565,120))     # Toy room bottom / Surreal Room top
        walls.append(Wall(screen,2070,1095,120,490))    # Fire room right
        walls.append(Wall(screen,1205,975,120,610))     # Fire room left / Surreal room upper right
        walls.append(Wall(screen,1205,1585,980,120))    # Fire room bottom
        walls.append(Wall(screen,1205,1705,120,230))    # Surreal room lower right
        walls.append(Wall(screen,525,1160,120,350))     # Surreal room upper left
        walls.append(Wall(screen,525,1595,120,340))     # Surreal room lower left
        walls.append(Wall(screen,645,1810,560,120))     # Surreal room bottom
        walls.append(Wall(screen,1090,420,110,110))     # Clown
        walls.append(Wall(screen,700,680,50,115))       # Bookcase
        walls.append(Wall(screen,1150,840,60,75))       # Puzzle Chest
        walls.append(Wall(screen,1080,1040,130,120))    # Toy Chest
        walls.append(Wall(screen,800,2560,220,125))     # Kitchen Table
        walls.append(Wall(screen,1020,2425,190,70))     # Kitchen Cabinet
        walls.append(Wall(screen,1165,2560,45,125))     # Kitchen Fridge
        walls.append(Wall(screen,1980,1995,95,145))     # Crates 1
        walls.append(Wall(screen,2220,1995,170,95))     # Crates 2
        walls.append(Wall(screen,2100,2210,95,295))     # Crates 3
        walls.append(Wall(screen,2170,2225,80,55))      # Crates 4
        walls.append(Wall(screen,2300,2395,90,105))     # Crates 5
        walls.append(Wall(screen,1402,1218,56,70))      # Static flames 1
        walls.append(Wall(screen,1908,1368,60,60))      # Static flames 2
        walls.append(Wall(screen,2022,1528,60,60))      # Static flames 3
        walls.append(Wall(screen,2625,540,120,200))     # Final Door

        items=[]

        # Items for paintings puzzle
        items.append(FireDoor(screen,1781,974,"firedoor"))      # Door with book motif - MUST BE FIRST ITEM APPENDED
        items.append(Popup(screen,880,700,120,60,"book"))       # Toy room book - Christmas Stories
        items.append(Door(screen,584,942,"toydoor"))            # Door to toy room - left
        items.append(Door(screen,1622,298,"playdoor"))          # Door to play room - top
        items.append(Button(screen,1512,376,80,45,6))           # Painting: Flames
        items.append(Button(screen,2064,706,60,60,2))           # Painting: grabs matches
        items.append(Button(screen,1302,774,30,40,1))           # Painting: playing with toys
        items.append(Button(screen,1495,975,35,20,5))           # Painting: sirens
        items.append(Button(screen,2064,908,20,50,4))           # Painting: sees fire
        items.append(Button(screen,1818,378,40,40,3))           # Painting: lights matches

        # Items for kitchen puzzle
        items.append(WingDoor(screen,525,2570,"wingdoor"))      # Door with wing impressions
        items.append(Item(screen,1080,2720,"cleaver"))          # Cleaver
        items.append(Crate(screen,1069,2709,"crate"))           # Crate
        items.append(Oven(screen,725,2456,120,35))              # The oven
        items.append(Sink(screen,650,2425,75,60))               # Kitchen sink

        # Items for the fire puzzle
        items.append(Door(screen,2080,1892,"storagedoor"))      # Door to storage room - top
        items.append(Popup(screen,1660,1575,50,20,"nyt"))       # Fire room newspaper - New York Times
        items.append(Fire(screen,1805,1055,"fire"))             # Wall of fire
        items.append(Item(screen,2232,2302,"bucket"))           # Bucket
        items.append(Sink(screen,1880,2350,40,70))              # Storage sink

        # Items for cage puzzle
        items.append(KeyDoor(screen,524,1498,"keydoor"))                        # Door that needs key
        items.append(Teddypart(screen,900,1542,"teddy's head"))         # Teddy's head - in cage
        items.append(Cage(screen,870,1508,"cage"))                      # Cage containing teddy's head
        items.append(Item(screen,1626,1295,"key"))                      # Key to open key door
        items.append(Teddypart(screen,1899,2029,"teddy's torso"))       # Teddy's torso
        items.append(Teddypart(screen,1708,1542,"teddy's right arm"))   # Teddy's right arm
        items.append(Teddypart(screen,2022,422,"teddy's left arm"))     # Teddy's left arm
        items.append(Teddypart(screen,1092,1295,"teddy's leg"))         # Teddy's leg
        items.append(Crib(screen,783,428,110,60))
        items.append(EndGate(screen,2620,590,120,110))                  # The final gate, yay!


        monster = Monster(screen, nodes[0][0], nodes[0][1],"bear") #Our monsters.
        bg = pygame.image.load("levels/floor.png").convert() #Background image.
        fog = pygame.image.load("fog3.png").convert_alpha() #This causes the lighting effect.
        eye = pygame.image.load("items/eye.png").convert_alpha()
        eyeBlit = False

        try: #Background music is loaded here.
                sound = pygame.mixer.Sound("sounds/ambient-2.ogg")
                sound.play(loops = -1)
        except pygame.error, message:
                print "Cannot load sound: " + sound_name
                raise SystemExit, message
                        
        dead = False
        # The game loop
        while not dead:
                #The actual game starts here.
                screen.fill((0, 0, 0)) #Fills all the parts without an image black.
                sleepy.update() #Updates the player sprite first.
                screen.blit(bg,(400-sleepy.posx,300-sleepy.posy)) #Displays the background relative to the player, making it a panning background image.
                monster.move(nodes,sleepy.x + sleepy.posx,sleepy.y + sleepy.posy) #Monster chases the player. Basic AI is here Seth.
                monster.draw((monster.x-sleepy.posx),(monster.y-sleepy.posy)) #Monster gets drawn.
                for s in items:
                        s.draw((s.x-sleepy.posx),(s.y-sleepy.posy)) #Draws the items.
                        if((s.interactionrect).colliderect(sleepy.rect)):
                                eyeBlit = True
                                if pygame.sprite.collide_rect(sleepy,s): # Checks if the player hit any of the items.
                                
                                        if(sleepy.dir=="left"):
                                                sleepy.posx += 4
                                        elif(sleepy.dir=="right"):
                                                sleepy.posx -= 4
                                        elif(sleepy.dir=="up"):
                                                sleepy.posy += 4
                                        else:
                                                sleepy.posy -= 4

                sleepy.draw()

                if(sleepy.buttons == [6,5,4,3,2,1]):
                        monster.fibonacci = True
                else:
                        monster.fibonacci = False

                for w in walls:
                        if pygame.sprite.collide_rect(sleepy, w):
                                if(sleepy.dir=="left"):
                                        sleepy.posx += 4
                                elif(sleepy.dir=="right"):
                                        sleepy.posx -= 4
                                elif(sleepy.dir=="up"):
                                        sleepy.posy += 4
                                else:
                                        sleepy.posy -= 4

                screen.blit(fog, (0,0)) #Puts the lighting mask on top.
                if(eyeBlit):
                        screen.blit(eye, (30,20))
                        eyeBlit = False
                pygame.display.flip() #Updates the display.

                for event in pygame.event.get():
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE or event.key == K_CAPSLOCK: #Escape sometimes doesn't work on my computer, so I use CAPS LOCK.
                                        quit()
                                elif event.key == K_UP:
                                        sleepy.dir = "up"
                                        sleepy.imageCount=0
                                        sleepy.movement = True
                                elif event.key == K_DOWN:
                                        sleepy.dir = "down"
                                        sleepy.imageCount=0
                                        sleepy.movement = True
                                elif event.key == K_LEFT:
                                        sleepy.dir = "left"
                                        sleepy.imageCount=0
                                        sleepy.movement = True
                                elif event.key == K_RIGHT:
                                        sleepy.dir = "right"
                                        sleepy.imageCount=0
                                        sleepy.movement = True
                                elif event.key == K_SPACE:
                                        sleepy.movement = False
                                        for s in items:
                                                if((s.interactionrect).colliderect(sleepy.rect)): #Checks if the player is next to the item.
                                                        s.update((s.x-sleepy.posx),(s.y-sleepy.posy),sleepy,items)      
                                elif event.key == K_i: #Prints out the inventory.
                                        inventory = "You have "
                                        for item in sleepy.items:
                                                inventory += "(" + str(item[0]) + ") " + str(item) + ', '
                                        if(sleepy.teddyCount > 0):
                                                inventory += "and " + str(sleepy.teddyCount) + "/5 teddy parts "
                                        inventory += "with you."
                                        msg = sleepy.font.render(inventory,True,CLR_BROWN,CLR_BLACK)
                                        screen.blit(msg,MSG_HUGE)
                                        pygame.display.flip()
                                        pygame.time.wait(1200)
                                elif event.key == K_c:
                                        for s in sleepy.items:
                                                if(s == "cleaver"):
                                                        for m in items:
                                                                if(m.name == "pig" and (m.interactionrect).colliderect(sleepy.rect)):
                                                                        if(m.dead==False):
                                                                                try:
                                                                                        pigdead = pygame.mixer.Sound("sounds/stab.wav")
                                                                                except:
                                                                                        print "Cannot load sound: stab.wav"
                                                                                pigdead.play()
                                                                                sleepy.items.append("wings")
                                                                                msg = sleepy.font.render("You got pig wings!",True,CLR_BROWN,CLR_BLACK)
                                                                                screen.blit(msg,MSG_SMALL)
                                                                                pygame.display.flip()
                                                                                pygame.time.wait(750)
                                                                                m.isDead()

                                elif event.key == K_b:
                                        for s in sleepy.items:
                                                if(s == "bucket"):
                                                        for m in items:
                                                                if(m.name == "sink" and (m.interactionrect).colliderect(sleepy.rect)):
                                                                        sleepy.bucketfull = True
                                                                        msg = sleepy.font.render(TXT_BUCKETFILL,True,CLR_BROWN,CLR_BLACK)
                                                                        screen.blit(msg,MSG_SMALL)
                                                                        pygame.display.flip()
                                                                        pygame.time.wait(750)
                                                                elif(m.name == "fire" and (m.interactionrect).colliderect(sleepy.rect)):
                                                                        if(m.dead == False):
                                                                                try:
                                                                                        fireout = pygame.mixer.Sound("sounds/splash.wav")
                                                                                except:
                                                                                        print "Cannot load sound: splash.wav"
                                                                                fireout.play()
                                                                                msg = sleepy.font.render(TXT_FIREOUT,True,CLR_BROWN,CLR_BLACK)
                                                                                screen.blit(msg,MSG_BIG)
                                                                                pygame.display.flip()
                                                                                pygame.time.wait(2000)
                                                                                sleepy.bucketfull = False
                                                                                m.isDead()

                        else:
                                        sleepy.movement = False #Makes sure the player doesn't move if no button is pressed.

                if pygame.sprite.collide_rect(sleepy, monster) and monster.dead == False: #Checks if monster caught the player
                        sound.stop()
                        scream = pygame.mixer.Sound("sounds/scream.wav")
                        scream.play()
                        screen.fill((0, 0, 0))
                        pygame.display.flip()
                        pygame.time.wait(3500)
                        fail = pygame.image.load("cards/gameover.png").convert() #Intro screen image.
                        screen.blit(fail,(0,0))
                        pygame.display.flip()
                        pygame.time.wait(3500)
                        dead = True
pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE)
pygame.display.set_caption('Somnium') #Our game's name is Somnium!
screen = pygame.display.get_surface() #Setting up the screen
pygame.font.init()
screen_id = 0 #Enables us to have an intro screen.
intro = pygame.image.load("cards/menu.png").convert() #Intro screen image.
instructions = pygame.image.load("cards/instructions.png").convert() # Instruction screen image

try:
        intro_music = pygame.mixer.Sound("sounds/intro.ogg")
except:
        print "Cannot load sound: intro.ogg"
intro_music.play(loops = -1)

while(screen_id == 0):
        #Putting the initial screen up.
        screen.blit(intro, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_1 or event.key == K_RETURN:
                                screen_id = 1
                        if event.key == K_2:
                                screen_id = 2
                        if event.key == K_ESCAPE or event.key == K_3:
                                quit()
                else:
                        pass
if screen_id == 2:
        while(screen_id == 2):
                screen.blit(instructions, (0, 0))
                pygame.display.flip()
                for event in pygame.event.get():
                        if event.type == KEYDOWN:
                                if event.key == K_RETURN:
                                        screen_id = 1
                                else:
                                        pass
                        else:
                                pass

intro_music.stop()

if screen_id == 1:
        while(True):
                level1()
