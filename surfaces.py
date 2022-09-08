import pygame, sys

#General setup
pygame.init()
clock = pygame.time.Clock()

#Create the display surface
screen = pygame.display.set_mode((640,640))
second_surface = pygame.Surface([100,200])
second_surface.fill((0,0,255))

kitten = pygame.image.load("kitten.png")
kitten_rect = kitten.get_rect(topleft = [100,200])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255,255,255))
    screen.blit(second_surface,(0,50))    
    screen.blit(kitten,kitten_rect)
    kitten_rect.right += 5
    
    pygame.display.flip()
    clock.tick(60)