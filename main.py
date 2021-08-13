import sys
import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500,500))

r, g, b = 0, 255, 0

clock = pygame.time.Clock()
fps = 60

fade_speed = 1
brightness = 100

while 1:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if (r > 0 and b == 0):
        r -= fade_speed
        g += fade_speed
    
    elif (g > 0 and r == 0):
        g -= fade_speed
        b += fade_speed

    elif (b > 0 and g == 0):
        r += fade_speed
        b -= fade_speed

    # clamp
    if r > brightness : r = brightness
    if g > brightness : g = brightness
    if b > brightness : b = brightness
    if r < 0 : r = 0
    if g < 0 : g = 0
    if b < 0 : b = 0
    

    window.fill((r, g, b))
    pygame.display.update()