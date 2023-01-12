import pygame

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("Baghchal")
icon = pygame.image.load('tiger.png')
pygame.display.set_icon(icon)


#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
#screen colour
screen.fill((128,128,128))
pygame.display.update()


