import py_compile
import pygame, sys, pymunk


def create_apple(space,pos):
    body = pymunk.Body(1,100,body_type=pymunk.Body().DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,80)
    space.add(body,shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center = (pos_x,pos_y))
        screen.blit(apple_surface,apple_rect)
        

def static_ball(space,pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,5)
    space.add(body,shape)
    return shape


def draw_static_ball(balls):
    for ball in balls:
        pygame.draw.circle(screen,(217,98,119),ball.body.position,50)


pygame.init()
screen_width,screen_height = 640,640
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Physics')
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,500)
apple_surface = pygame.image.load('apple.png')
apples = []


balls = []
balls.append(static_ball(space,(380,500)))
balls.append(static_ball(space,(220,360)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space,event.pos))    
        
            
    screen.fill((217,217,217))
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/50)   
    pygame.display.update()
    clock.tick(60)