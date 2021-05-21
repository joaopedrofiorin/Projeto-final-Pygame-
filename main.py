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
muda_fundo = 0 #marca de transição
game = True 
clock = pygame.time.Clock() #Velocidade dos backgrounds

while game:
 
    if muda_fundo >= 0 and  muda_fundo <= 20000:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                game = False 
        
        tela.fill((255,255,255))
        
        tela.blit(imagem_cidade, (i,0))
        tela.blit(imagem_cidade, (limite+i,0))
        if i == -limite:
            i = 0
        i -= 1

        muda_fundo += 8 #tempo de transição
        clock.tick(450)
        pygame.display.update()
    
    elif muda_fundo > 20000 and muda_fundo <= 40000:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                game = False 
        
        tela.fill((255,255,255))
        
        tela.blit(imagem_floresta, (i,0))
        tela.blit(imagem_floresta, (limite+i,0))
        if i == -limite:
            i = 0
        i -= 1

        muda_fundo += 8
        clock.tick(550)
        pygame.display.update()

    elif muda_fundo > 40000 and muda_fundo <= 60000:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                game = False 
        
        tela.fill((255,255,255))
        
        tela.blit(imagem_inverno, (i,0))
        tela.blit(imagem_inverno, (limite+i,0))
        if i == -limite:
            i = 0
        i -= 1

        muda_fundo += 8
        clock.tick(1000)
        pygame.display.update()

    elif muda_fundo > 60000 and muda_fundo <= 80000:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                game = False 
        
        tela.fill((255,255,255))
        
        tela.blit(imagem_praia, (i,0))
        tela.blit(imagem_praia, (limite+i,0))
        if i == -limite:
            i = 0
        i -= 1

        muda_fundo += 8
        clock.tick(700)
        pygame.display.update()

    elif muda_fundo > 80000 and muda_fundo <= 100000:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                game = False 
        
        tela.fill((255,255,255))
        
        tela.blit(imagem_velho, (i,0))
        tela.blit(imagem_velho, (limite+i,0))
        if i == -limite:
            i = 0
        i -= 1

        muda_fundo += 8
        clock.tick(750)
        pygame.display.update()

    else:
        muda_fundo = 0

pygame.quit()