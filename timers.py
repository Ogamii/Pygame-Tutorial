import pygame, sys

#Setting up Pygame
pygame.init()
screen = pygame.display.set_mode((568,320)) 
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            screen.fill((255,255,255))
    
    current_time = pygame.time.get_ticks()
    
    if current_time - button_press_time > 2033:
        screen.fill((0,0,0))
    
    print(f'current time: {current_time} button press time: {button_press_time}')
    
    pygame.display.flip()
    clock.tick(60)