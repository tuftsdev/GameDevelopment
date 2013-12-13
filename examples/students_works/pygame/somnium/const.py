import pygame, os, sys, random
from pygame.locals import *
__name__ = "const"

# Size of the screen
SCREEN_SIZE = (800, 600)

# RGB Colors
#CLR_BROWN = (153,102,51)
CLR_BROWN = (90,55,20)
CLR_BLACK = (0,0,0)
CLR_WHITE = (255,255,255)

# Coordinates for printing text
MSG_HUGE = (5,560)
MSG_SMALL = MSG_HUGE #(250,560)
MSG_BIG = MSG_HUGE #(50,560)
MSG_LEFT = MSG_HUGE #(450,560)
MSG_TOPRIGHT = (20,20)
MSG_INVENTORY = MSG_HUGE #(20,20)

# Reusable message strings
TXT_DOORSOUND = "You hear the sound of a door opening.              "
TXT_DOORLOCKED = "This door is locked. It "
TXT_DOOROPEN = "You open the door."

TXT_BUCKETEMPTY = "The bucket is empty."
TXT_BUCKETFILL = "You fill the bucket with water."
TXT_BUCKETFULL = "The bucket is already full"

TXT_FIREOUT = "You toss the water from the bucket at the flames, dousing them."

TXT_NOUSE = "You can't use that item here."

TXT_SINK_INTERACT = "You turn the handle of the sink; water flows."

TXT_LOCK_ASHES = "There is a combination lock, with 'When the ashes were made' engraved on it. "
TXT_6CODE_INPUT = "Please enter 6 digit code and press Enter.                                                            "
