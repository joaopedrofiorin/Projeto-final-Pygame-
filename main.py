import pygame 
import os
import random

pygame.init()

WIDTH = 1250
HEIGHT = 400

tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Zilla Game')

# BackGrounds:
imagem_cidade = pygame.image.load('Imagens\Backgrounds\Cidade.png').convert()
imagem_cidade = pygame.transform.scale(imagem_cidade, (WIDTH, HEIGHT))
imagem_floresta = pygame.image.load('Imagens\Backgrounds\Floresta.png').convert()
imagem_floresta = pygame.transform.scale(imagem_floresta, (WIDTH, HEIGHT))
imagem_inverno = pygame.image.load('Imagens\Backgrounds\Vulcão.png').convert()
imagem_inverno = pygame.transform.scale(imagem_inverno, (WIDTH, HEIGHT))
imagem_praia = pygame.image.load('Imagens\Backgrounds\Praia.png').convert()
imagem_praia = pygame.transform.scale(imagem_praia, (WIDTH, HEIGHT))
imagem_velho = pygame.image.load('Imagens\Backgrounds\Velho Oeste.png').convert()
imagem_velho = pygame.transform.scale(imagem_velho, (WIDTH, HEIGHT))

# Godzilla: 
zilla_run1 = pygame.image.load('Imagens\Dino\ZillaRun1.png')
zilla_run2 = pygame.image.load('Imagens\Dino\ZillaRun2.png')
zilla_duck1 = pygame.image.load('Imagens\Dino\ZillaDuck1.png')
zilla_duck2 = pygame.image.load('Imagens\Dino\ZillaDuck2.png')
zilla_jump = pygame.image.load('Imagens\Dino\ZillaJump.png')
zilla_start = pygame.image.load('Imagens\Dino\ZillaStart.png')
zilla_dead = pygame.image.load('Imagens\Dino\ZillaDead.png')

#obstáculos
obstaculos_grandes=[pygame.image.load ('Imagens\Obstáculos\Cidade\Carro_Grande.png'),
pygame.image.load ('Imagens\Obstáculos\Floresta\Arvore_Grande.png'),
pygame.image.load ('Imagens\Obstáculos\Praia\Coqueiro_Grande.png'),
pygame.image.load ('Imagens\Obstáculos\Velho Oeste\Cavalo_Grande.png'),
pygame.image.load ('Imagens\Obstáculos\Vulcão\Pedras_Grande.png')]
obstaculos_pequenos=[pygame.image.load ('Imagens\Obstáculos\Cidade\Semáforo_Pequeno.png'),
pygame.image.load ('Imagens\Obstáculos\Floresta\Arvore_pequena.png'),
pygame.image.load ('Imagens\Obstáculos\Praia\Bola_pequeno.png'),
pygame.image.load ('Imagens\Obstáculos\Velho Oeste\Carrinho_Pequeno.png'),
pygame.image.load ('Imagens\Obstáculos\Vulcão\Dino_Pequeno.png')]

# Listas Zilla:
RUNNING = [zilla_run1,zilla_run2]
JUMPING = zilla_jump
DUCKING = [zilla_duck1,zilla_duck2]
STARTING = zilla_start
DEADING = zilla_dead


# Classe Zilla: 
class Zilla:

    X_position = 10 # posição X do zilla
    Y_position = 290 # posição Y do zilla
    y_duck_position = 320 #posicao y do zilla agachando

    def __init__(self):
        self.run_image = RUNNING # puxa as imagens de run 
        self.duck_image = DUCKING # puxa as imagens de duck
        self.jump_image = JUMPING # puxa as imagens de jump

        self.run_zilla = True # True porque o jogo começa com só o Zilla correndo
        self.duck_zilla = False # False porque não ocorre no começo 
        self.jump_zilla = False # False porque não ocorre no começo

        self.step_index = 0 # Vai servir para animar o Zilla
        self.image = self.run_image[0] # Serve para inicializar a primeira imagem
        self.zilla_rect = self.image.get_rect() # Faz o hitbox do Zilla
        self.zilla_rect.x = self.X_position # Posição do hitbox
        self.zilla_rect.y = self.Y_position # Posição do hitbox

    
    def update(self,Teclas): # Funçao para atualizar o Zilla
        if self.duck_zilla: # Atualiza o abaixar
            self.duck()
        if self.run_zilla: # Atualiza o correr
            self.run()
        if self.jump_zilla: # Atualiza o pulo
            self.jump()

        if self.step_index >= 10: # Conta os passos, para animar o Zilla
            self.step_index = 0 

        if Teclas[pygame.K_UP] and not self.jump_zilla: # Pula com a seta pra cima pressionada
            self.run_zilla = False
            self.duck_zilla = False 
            self.jump_zilla = True 
            self.v_jump = 9.2
        elif Teclas[pygame.K_DOWN] and not self.jump_zilla: # Abaixa com a seta pra baixo pressionada
            self.run_zilla = False
            self.duck_zilla = True 
            self.jump_zilla = False
        elif not (self.jump_zilla or Teclas[pygame.K_DOWN]): # Zilla continua a correr
            self.run_zilla = True
            self.duck_zilla = False 
            self.jump_zilla = False

    def duck(self): 
        self.image = self.duck_image[self.step_index // 5]
        self.zilla_rect = self.image.get_rect()
        self.zilla_rect.x = self.X_position # Posição do hitbox
        self.zilla_rect.y = self.y_duck_position # Posição do hitbox
        self.step_index += 1

    def run(self):
        self.image = self.run_image[self.step_index // 5]
        self.zilla_rect = self.image.get_rect()
        self.zilla_rect.x = self.X_position # Posição do hitbox
        self.zilla_rect.y = self.Y_position # Posição do hitbox
        self.step_index += 1

    def jump(self):
        self.image = self.jump_image
        if self.jump_zilla:
            self.zilla_rect.y -= self.v_jump * 4
            self.v_jump -= 0.8
        if self.zilla_rect.y >= self.Y_position:
            self.jump_zilla = False
            self.zilla_rect.y = self.Y_position
    
    def draw(self,tela):
        tela.blit(self.image, (self.zilla_rect.x,self.zilla_rect.y))

class obstacle:

    def __init__(self,image,type):
        self.image=image
        self.type=type
        self.rect=self.image[self.type].get_rect()
        self.rect.x= WIDTH
    
    def update(self):
        self.rect.x -= speed_bg
        if self.rect.x < -self.rect.width:
            obstacle.pop()

    def draw(self,tela):
        tela.blit(self.image[self.type],self.rect)

class big_and_small_objects(obstacle):

i = 0 #Responsável pelas transições
limite = WIDTH #limite da tela para começar uma nova imagem 
muda_fundo = 0 #marca de transição
game = True 
points = 0 #Score do Jogo
fonte = pygame.font.Font('Fontes\PressStart2P.ttf', 20) # Fonte usada na letra

# Lista Background:
lista_bg = [imagem_cidade,imagem_floresta,imagem_inverno,imagem_praia,imagem_velho]
index_bg = 0
speed_bg = 10 #velocidade do jogo
clock = pygame.time.Clock()

player = Zilla()

imagem_classe=[]
while game:
    clock.tick(30)
    
    
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            game = False 

    # Manipulação do Background
    if muda_fundo % 1000 == 0 and muda_fundo != 0:
        index_bg = (index_bg + 1) % len(lista_bg)
        speed_bg += 5

    image_bg = lista_bg[index_bg]
    imagem_classe.append=(image_bg)

    tela.fill((255,255,255))
    Teclas = pygame.key.get_pressed()

    tela.blit(image_bg, (i,0))
    tela.blit(image_bg, (limite+i,0))
    if i <= -limite:
        i = 0
    i -= speed_bg

    muda_fundo += 1 #tempo de transição

    player.draw(tela) # Desenha o Zilla na tela
    player.update(Teclas) # Atualiza posição do Zilla
    # Score
    points += int(speed_bg/5)
    text = fonte.render('Points: ' + str(points), False, (0,255,0) )
    textRect = text.get_rect()
    textRect.center = (1100, 40)
    tela.blit(text, textRect)

    imagem_classe.clear()

    pygame.display.update()

pygame.quit()