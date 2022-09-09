import pygame, sys


class Rectangles(pygame.sprite.Sprite):
    
    def __init__(self,pos_x,pos_y,width,height,color,x_speed,y_speed, other_rect = None):
        super().__init__()
        self.color = pygame.Color(color)
        self.surface = pygame.Surface((width,height))
        self.surface.fill(self.color)
        self.rect= self.surface.get_rect(center =(pos_x,pos_y))
        self.x_speed = x_speed
        self.y_speed = y_speed
        
    
    def bouncing_rect(self):
        
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
        #Collision with screen borders
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.x_speed *= -1 
    
        if self.rect.bottom >= screen_height or self.rect.top <= 0:
            self.y_speed *= -1        
        
        screen.blit(self.surface,self.rect)


def collision(rectan1,rectan2):
    collision_tolerance = 10
    if rectan1.colliderect(rectan2):
        if abs(rectan2.top - rectan1.bottom) < collision_tolerance and rect1.y_speed > 0:
            rect1.y_speed *= -1
            
        if abs(rectan2.bottom - rectan1.top) < collision_tolerance and rect1.y_speed < 0:
            rect1.y_speed *= -1
            
        if abs(rectan2.left - rectan1.right) < collision_tolerance and rect1.x_speed > 0:
            rect1.x_speed *= -1
            
        if abs(rectan2.right - rectan1.left) < collision_tolerance and rect1.x_speed < 0:
            rect1.x_speed *= -1
        # print('collision')        
        

# def bouncing_rect():
#     moving_rect.x += x_speed
#     moving_rect.y += y_speed
    
#     #Collision with screen borders
#     if moving_rect.right >= screen_width or moving_rect.left <= 0:
#         x_speed *= -1 
    
#     if moving_rect.bottom >= screen_height or moving_rect.top <= 0:
#         y_speed *= -1
    
#     pygame.draw.rect(screen,(255,255,255),moving_rect)
#     pygame.draw.rect(screen,(255,0,0),other_rect)


#General Setup
pygame.init()
clock = pygame.time.Clock()

#Game Screen 
screen_width, screen_height = 640, 640
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Collisions")

#Rectangles
# moving_rect = pygame.Rect(270,270,100,100)
# x_speed, y_speed = 5, 4
# other_rect = pygame.Rect(220,500,200,100)
# other_speed = 2
rect1 = Rectangles(320,320,100,100,'white',5,4)
rect2 = Rectangles(320,540,200,50,'red2',0,1)

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
     #Drawing
    screen.fill((30,30,30))
    
    rect1.bouncing_rect()
    rect2.bouncing_rect()
    collision(rect1.rect,rect2.rect)
    
    pygame.display.flip()
    clock.tick(60)