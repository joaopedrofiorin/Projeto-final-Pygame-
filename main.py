import pygame 

pygame.init()

tela = pygame.display.set_mode((1250,400))
pygame.display.set_caption('T-rex Game')

game = True 

while game:
    
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            game = False 
    
    tela.fill((255,255,255))

    pygame.display.update()

pygame.quit()