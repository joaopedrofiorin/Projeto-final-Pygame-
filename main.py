import pygame 

pygame.init()

tela = pygame.display.set_mode((1250,400))
pygame.display.set_caption('T-rex Game')

imagem = pygame.image.load('Imagens\Velho Oeste 2.jpg').convert()
imagem = pygame.transform.scale(imagem, (1250, 400))

game = True 

while game:
    
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            game = False 
    
    tela.fill((255,255,255))
    tela.blit(imagem, (0,0))

    pygame.display.update()

pygame.quit()