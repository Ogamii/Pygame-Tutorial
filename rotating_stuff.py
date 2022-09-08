from tkinter import CENTER
import pygame, sys


def rotate(surface,angle):
    rotated_surface = pygame.transform.rotozoom(surface,-angle,1)
    rotated_rect = rotated_surface.get_rect(center = (300,300))
    return rotated_surface, rotated_rect


#General setup
pygame.init()
clock = pygame.time.Clock()

#Create the display surface
screen = pygame.display.set_mode((600,600))
# pikachu = pygame.Surface((200,200),pygame.SRCALPHA)
# pikachu.fill((255,0,0))
pikachu = pygame.image.load("pikachu.png")
pikachu_rect = pikachu.get_rect(center = (300,300))
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    angle += 1
    screen.fill((255,255,255))
    pikachu_rotated, pikachu_rotated_rect = rotate(pikachu,angle)
    
    screen.blit(pikachu_rotated,pikachu_rotated_rect) 
    pygame.display.flip()
    clock.tick(60)