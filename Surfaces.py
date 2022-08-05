import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()
r = 0
g = 0
b = 0
color_mode = 0
screen = pygame.display.set_mode((800,800))
seventh_surface = pygame.Surface((100,100))
second_surface = pygame.Surface([100,100])
third_surface = pygame.Surface([100,100])
fourth_surface = pygame.Surface([100,100])
fifth_surface = pygame.Surface([100,100])
sixth_surface = pygame.Surface([100,100])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            color_mode = color_mode + 1
            if color_mode > 8:
                color_mode = 0
            
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)

    if color_mode == 0:
        screen.fill((0,0,0))
    elif color_mode == 1:
        screen.fill((255,255,255))
    elif color_mode == 2:
        screen.fill((r,0,0))
    elif color_mode == 3:
        screen.fill((0,g,0))
    elif color_mode == 4:
        screen.fill((0,0,b))
    elif color_mode == 5:
        screen.fill((r,g,0))
    elif color_mode == 6:
        screen.fill((r,0,b))
    elif color_mode == 7:
        screen.fill((0,g,b))
    elif color_mode == 8:
        screen.fill((r,g,b))
    

    second_surface.fill((r, g, b))
    third_surface.fill((r,b,g))
    fourth_surface.fill((b,r,g))
    fifth_surface.fill((b,g,r))
    sixth_surface.fill((g,r,b))
    seventh_surface.fill((g,b,r))


    screen.blit(second_surface, (50,50))
    screen.blit(third_surface, (150,150))
    screen.blit(fourth_surface, (250,250))    
    screen.blit(fifth_surface, (350,350))
    screen.blit(sixth_surface, (450,450))
    screen.blit(seventh_surface, (550,550))
    pygame.display.flip()
    clock.tick(10)
