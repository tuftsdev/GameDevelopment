import pygame #, sys, os
from pygame.locals import *
pygame.init()

window = pygame.display.set_mode((800, 600))#, pygame.FULLSCREEN)
screen = pygame.display.get_surface()

code = [K_UP, K_UP, K_DOWN, K_DOWN, K_LEFT, K_RIGHT, K_LEFT, K_RIGHT, K_b, K_a,
        K_RETURN]
streak = 0

while streak < len(code):
    events = pygame.event.get()
    for event in events:
        if event.type == KEYDOWN:
            if event.key == code[streak]:
                streak += 1
            else:
                streak = 0

print "YOU WIN!!!!"        

