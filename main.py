import pygame 
import os 

pygame.init()

tela = pygame.display.set_mode((1250,400))
pygame.display.set_caption('T-rex Game')

imagem_cidade = pygame.image.load('Imagens\Cidade.png')
imagem_cidade = pygame.transform.scale(imagem_cidade, (1250, 400))
imagem_floresta = pygame.image.load('Imagens\Floresta.png')
imagem_floresta = pygame.transform.scale(imagem_floresta, (1250, 400))
imagem_inverno = pygame.image.load('Imagens\Vulcão.png')
imagem_inverno = pygame.transform.scale(imagem_inverno, (1250, 400))
imagem_praia = pygame.image.load('Imagens\Praia.png')
imagem_praia = pygame.transform.scale(imagem_praia, (1250, 400))
imagem_velho = pygame.image.load('Imagens\Velho Oeste.png')
imagem_velho = pygame.transform.scale(imagem_velho, (1250, 400))

i = 0 #Responsável pelas transições
limite = 1250 #limite da tela para começar uma nova imagem 
muda_fundo = 1 #marca de transição
game = True 
clock = pygame.time.Clock() #Velocidade dos backgrounds

lista_bg = [imagem_cidade,imagem_floresta,imagem_inverno,imagem_praia,imagem_velho]
index_bg = 0
speed_bg = 2

while game:

    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            game = False 

    # Manipulação do Background
    if muda_fundo % 2500 == 0:
        index_bg = (index_bg + 1) % len(lista_bg)
        speed_bg += 1
    
    image_bg = lista_bg[index_bg]

    tela.fill((255,255,255))

    tela.blit(image_bg, (i,0))
    tela.blit(image_bg, (limite+i,0))
    if i <= -limite:
        i = i + limite
    i -= speed_bg

    muda_fundo += 1 #tempo de transição
        
    pygame.display.update()

pygame.quit()