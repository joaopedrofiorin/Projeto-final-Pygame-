import pygame 
import os
import random
import time

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
imagem_vulcao = pygame.image.load('Imagens\Backgrounds\Vulcão.png').convert()
imagem_vulcao = pygame.transform.scale(imagem_vulcao, (WIDTH, HEIGHT))
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

#Obstáculos:

#Semaforo grande:  #largura,altura
semaforo = pygame.image.load ('Imagens\Obstáculos\Cidade\Semáforo_Pequeno.png')
semaforo = pygame.transform.scale(semaforo, (100, 190))
#Carro pequeno:
carro = pygame.image.load ('Imagens\Obstáculos\Cidade\Carro_Grande.png')
carro = pygame.transform.scale(carro, (120, 270))
#Arvore grande:
arvore_grande = pygame.image.load ('Imagens\Obstáculos\Floresta\Arvore_Grande.png')
arvore_grande = pygame.transform.scale(arvore_grande, (100, 180))
#Arvore pequena: 
arvore_pequena = pygame.image.load ('Imagens\Obstáculos\Floresta\Arvore_pequena.png')
arvore_pequena = pygame.transform.scale(arvore_pequena, (210, 290))
#Pedra grande:
pedra_grande =  pygame.image.load ('Imagens\Obstáculos\Vulcão\Pedras_Grande.png')
pedra_grande = pygame.transform.scale(pedra_grande, (140, 200))
#Dino pequeno:
dino_pequeno = pygame.image.load ('Imagens\Obstáculos\Vulcão\Dino_Pequeno.png')
dino_pequeno = pygame.transform.scale(dino_pequeno, (150, 230))
#Coqueiro grande: 
coqueiro_grande = pygame.image.load ('Imagens\Obstáculos\Praia\Coqueiro_Grande.png')
coqueiro_grande = pygame.transform.scale(coqueiro_grande, (150, 200))
#Bola pequena:
bola_pequena = pygame.image.load ('Imagens\Obstáculos\Praia\Bola_pequeno.png')
bola_pequena = pygame.transform.scale(bola_pequena, (80, 110))
#Cavalo grande:
cavalo_grande = pygame.image.load ('Imagens\Obstáculos\Velho Oeste\Cavalo_Grande.png')
cavalo_grande = pygame.transform.scale(cavalo_grande, (90, 200))
#Carrinho pequeno:
carrinho_pequeno =  pygame.image.load ('Imagens\Obstáculos\Velho Oeste\Carrinho_Pequeno.png')
carrinho_pequeno = pygame.transform.scale(carrinho_pequeno, (80, 100))

#Objetos voadores: 
largura = 100
altura = 100

#Avião Cidade:
aviao_cidade = pygame.image.load ('Imagens\Obstáculos\Objetos-Voadores\Aviao_Cidade.png')
aviao_cidade = pygame.transform.scale(aviao_cidade, (largura, altura))
#Avião Floresta:
aviao_floresta = pygame.image.load ('Imagens\Obstáculos\Objetos-Voadores\Aviao_Floresta.png')
aviao_floresta = pygame.transform.scale(aviao_floresta, (largura, altura))
#Avião Vulcao: 
aviao_vulcao = pygame.image.load ('Imagens\Obstáculos\Objetos-Voadores\Aviao_Vulcao.png')
aviao_vulcao = pygame.transform.scale(aviao_vulcao, (largura, altura))
#Avião Praia:
aviao_praia = pygame.image.load ('Imagens\Obstáculos\Objetos-Voadores\Aviao_Praia.png')
aviao_praia = pygame.transform.scale(aviao_praia, (120, 120))
#Avião Velho Oeste:
aviao_velho = pygame.image.load ('Imagens\Obstáculos\Objetos-Voadores\Aviao_Velho.Oeste.png')
aviao_velho = pygame.transform.scale(aviao_velho, (150, 150))

#Música
pygame.mixer.music.load ('Music\Dinomusic.ogg')
pygame.mixer.music.set_volume(0.4)

#Tela inicial e final
inicio = pygame.image.load('Imagens\Inicio-Fim\Inicial.jpg')
inicio = pygame.transform.scale(inicio, (1250, 400))
fim = pygame.image.load('Imagens\Inicio-Fim\Final.jpg')
fim = pygame.transform.scale(inicio, (1250, 400))

#Dicionário
cenarios = {
    'cidade':{
        'imagem': imagem_cidade, 
        'obstaculos': [
            carro,
            semaforo,
            aviao_cidade
        ]
    },
    'floresta':{
        'imagem': imagem_floresta,
        'obstaculos':[
            arvore_pequena,
            arvore_grande,
            aviao_floresta
        ]
    },
    'vulcao':{
        'imagem': imagem_vulcao,
        'obstaculos':[
            dino_pequeno,
            pedra_grande,
            aviao_vulcao
        ]
    },
    'praia':{
        'imagem': imagem_praia,
        'obstaculos':[
            bola_pequena,
            coqueiro_grande,
            aviao_praia
        ]
    },
    'velho oeste':{
        'imagem': imagem_velho,
        'obstaculos':[
            carrinho_pequeno,
            cavalo_grande,
            aviao_velho
        ]
    }
}

# Listas Zilla:
RUNNING = [zilla_run1,zilla_run2]
JUMPING = zilla_jump
DUCKING = [zilla_duck1,zilla_duck2]
STARTING = zilla_start
DEADING = zilla_dead


# Classe Zilla: 
class Zilla(pygame.sprite.Sprite):

    X_position = 10 # posição X do zilla
    Y_position = 290 # posição Y do zilla
    y_duck_position = 320 #posicao y do zilla agachando

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.run_image = RUNNING # puxa as imagens de run 
        self.duck_image = DUCKING # puxa as imagens de duck
        self.jump_image = JUMPING # puxa as imagens de jump

        self.run_zilla = True # True porque o jogo começa com só o Zilla correndo
        self.duck_zilla = False # False porque não ocorre no começo 
        self.jump_zilla = False # False porque não ocorre no começo

        self.step_index = 0 # Vai servir para animar o Zilla
        self.image = self.run_image[0] # Serve para inicializar a primeira imagem
        self.rect = self.image.get_rect() # Faz o hitbox do Zilla
        self.rect.x = self.X_position # Posição do hitbox
        self.rect.y = self.Y_position # Posição do hitbox

    
    def update(self): # Funçao para atualizar o Zilla
        if self.duck_zilla: # Atualiza o abaixar
            self.duck()
        if self.run_zilla: # Atualiza o correr
            self.run()
        if self.jump_zilla: # Atualiza o pulo
            self.jump()

        if self.step_index >= 10: # Conta os passos, para animar o Zilla
            self.step_index = 0 

    def duck(self): 
        self.image = self.duck_image[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_position # Posição do hitbox
        self.rect.y = self.y_duck_position # Posição do hitbox
        self.step_index += 1

    def run(self):
        self.image = self.run_image[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_position # Posição do hitbox
        self.rect.y = self.Y_position # Posição do hitbox
        self.step_index += 1

    def jump(self):
        self.image = self.jump_image
        if self.jump_zilla:
            self.rect.y -= self.v_jump * 4
            self.v_jump -= 0.8
        if self.rect.y >= self.Y_position:
            self.jump_zilla = False
            self.rect.y = self.Y_position
    
    def draw(self,tela):
        tela.blit(self.image, (self.rect.x,self.rect.y))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x= WIDTH
    
    def update(self):
        self.rect.x -= speed_bg
        if self.rect.x < -self.rect.width:
            self.kill()
        if self.image == carro:
            self.rect.y = 220
        elif self.image == semaforo:
            self.rect.y = 210
        elif self.image == arvore_pequena:
            self.rect.y = 180
        elif self.image == arvore_grande: 
            self.rect.y = 200
        elif self.image == dino_pequeno:
            self.rect.y = 215
        elif self.image == pedra_grande: 
            self.rect.y = 210
        elif self.image == bola_pequena:
            self.rect.y = 280
        elif self.image == coqueiro_grande:
            self.rect.y = 210
        elif self.image == carrinho_pequeno:
            self.rect.y = 290
        elif self.image == cavalo_grande:
            self.rect.y = 200
        elif self.image in [aviao_cidade,aviao_vulcao,aviao_praia]:
            self.rect.y = 215
        else: 
            self.rect.y = 200
        
    
i = 0 #Responsável pelas transições
limite = WIDTH #limite da tela para começar uma nova imagem 
muda_fundo = 0 #marca de transição
game = True 
points = 0 #Score do Jogo
fonte = pygame.font.Font('Fontes\PressStart2P.ttf', 20) # Fonte usada na letra

# Lista Background:
lista_bg = list(cenarios.keys())
index_bg = 0
speed_bg = 12 #velocidade do jogo
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()

player = Zilla()
all_sprites.add(player)

sheesh = True 
while sheesh:
    tela.blit(inicio, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sheesh = False
            game = False
        if event.type == pygame.KEYDOWN:
            sheesh = False

    pygame.display.update()

pygame.mixer.music.play(loops=-1)# Loop da música

while game:
    clock.tick(30)
    
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            game = False 

    Teclas = pygame.key.get_pressed()

    if Teclas[pygame.K_UP] and not player.jump_zilla: # Pula com a seta pra cima pressionada
        player.run_zilla = False
        player.duck_zilla = False 
        player.jump_zilla = True 
        player.v_jump = 9.2
    elif Teclas[pygame.K_DOWN] and not player.jump_zilla: # Abaixa com a seta pra baixo pressionada
        player.run_zilla = False
        player.duck_zilla = True 
        player.jump_zilla = False
    elif not (player.jump_zilla or Teclas[pygame.K_DOWN]): # Zilla continua a correr
        player.run_zilla = True
        player.duck_zilla = False 
        player.jump_zilla = False

    # Manipulação do Background
    if muda_fundo % 1000 == 0 and muda_fundo != 0:
        index_bg = (index_bg + 1) % len(lista_bg)
        speed_bg += 2

    cenario = cenarios[lista_bg[index_bg]]
    image_bg = cenario['imagem']

    while len(all_obstacles) < 2:
        tipo = random.randint(0,2)
        obstaculo = Obstacle(cenario['obstaculos'][tipo])
        all_obstacles.add(obstaculo)
        all_sprites.add(obstaculo)

        if len(all_obstacles) < 2: 
            obstaculo.rect.x += 800 + (speed_bg//12)*1000

    tela.fill((255,255,255))
    

    tela.blit(image_bg, (i,0))
    tela.blit(image_bg, (limite+i,0))
    if i <= -limite:
        i = 0
    i -= speed_bg

    muda_fundo += 1 #tempo de transição
    
    # Verifica se houve colisão entre nave e meteoro
    hits = pygame.sprite.spritecollide(player, all_obstacles, True, collided=pygame.sprite.collide_mask)

    if hits:
       time.sleep(1)
       game = False
    
    all_sprites.draw(tela) # Desenha o Zilla na tela
    all_sprites.update() # Atualiza posição do Zilla
    # Score
    points += int(speed_bg/5)
    text = fonte.render('Points: ' + str(points), False, (0,255,0) )
    textRect = text.get_rect()
    textRect.center = (1100, 40)
    tela.blit(text, textRect)

    pygame.display.update()

pygame.quit()