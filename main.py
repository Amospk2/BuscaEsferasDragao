import pygame
from random import randint, choice
import math
from constants import *
from terreno import draw_map
from celula import Celula
from a_estrela import a_estrela
from time import sleep


pygame.init()
pygame.mixer.init()

sound_effect = pygame.mixer.Sound("Dragon Ball Z Opening 8 bit_0VmYKE4-HcM.mp3")
sound_effect.set_volume(0.2)
sound_effect.play()

esfera_found = pygame.mixer.Sound("game-bonus-144751.mp3")

screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

random_esfers = []
esferar_encontradas = []
desenhando_esferar = False


def desenhas_esferas():
    for esfers in random_esfers:
        rect = pygame.Rect(
            esfers[1] * TAMANHO_TILE, 
            esfers[0]*TAMANHO_TILE, TAMANHO_TILE-1, 
            TAMANHO_TILE-1
        )

        if (esfers[0], esfers[1]) not in esferar_encontradas:
            screen.fill((255, 255, 0), rect=rect)
        else:
            screen.fill((255, 0, 255), rect=rect)

        pygame.display.update()



def cria_matriz_radar(linha, coluna):

    vizinhos = [
        [linha-1, coluna], [linha+1, coluna], # baixo cima
        [linha-2, coluna], [linha+2, coluna], # baixo cima
        [linha-3, coluna], [linha+3, coluna], # baixo cima

        [linha, coluna-1], [linha, coluna+1], # baixo cima
        [linha, coluna-2], [linha, coluna+2], # baixo cima
        [linha, coluna-3], [linha, coluna+3], # baixo cima
        
        # Linha abaixo
        [linha+1, coluna+1], [linha+1, coluna+2], [linha+1, coluna+3],
        [linha-1, coluna-1], [linha-1, coluna-2], [linha-1, coluna-3],
                
        # Linha abaixo 1
        [linha+1, coluna+1], [linha+1, coluna+2], [linha+1, coluna+3],
        [linha+1, coluna-1], [linha+1, coluna-2], [linha+1, coluna-3],

        # Linha abaixo 2
        [linha+2, coluna+1], [linha+2, coluna+2], [linha+2, coluna+3],
        [linha+2, coluna-1], [linha+2, coluna-2], [linha+2, coluna-3],

        # Linha abaixo 3
        [linha+3, coluna+1], [linha+3, coluna+2], [linha+3, coluna+3],
        [linha+3, coluna-1], [linha+3, coluna-2], [linha+3, coluna-3],

        # Linha acima 1
        [linha-1, coluna+1], [linha-1, coluna+2], [linha-1, coluna+3],
        [linha-1, coluna-1], [linha-1, coluna-2], [linha-1, coluna-3],

        # Linha acima 2
        [linha-2, coluna+1], [linha-2, coluna+2], [linha-2, coluna+3],
        [linha-2, coluna-1], [linha-2, coluna-2], [linha-2, coluna-3],

        # Linha acima 3
        [linha-3, coluna+1], [linha-3, coluna+2], [linha-3, coluna+3],
        [linha-3, coluna-1], [linha-3, coluna-2], [linha-3, coluna-3],
    ]

    screen_copy = screen.copy()

    must_sleep = False
    for vizinho in vizinhos:

        if(
            vizinho[0] > -1 and vizinho[0] < 42
        ) and (
            vizinho[1] > -1 and vizinho[1] < 42
        ):
            if vizinho in random_esfers:

                if (vizinho[0], vizinho[1]) not in esferar_encontradas:
                    esferar_encontradas.append((vizinho[0], vizinho[1]))
                    esfera_found.play()

                    for v in vizinhos:
                        rect = pygame.Rect(
                            v[1] * TAMANHO_TILE, 
                            v[0]*TAMANHO_TILE, TAMANHO_TILE-1, 
                            TAMANHO_TILE-1
                        )
                        screen.fill((100, 100, 100), rect=rect)
                        pygame.display.update()

                    must_sleep = True
                else:
                    must_sleep = False

                rect = pygame.Rect(
                    vizinho[1] * TAMANHO_TILE, 
                    vizinho[0]*TAMANHO_TILE, TAMANHO_TILE-1, 
                    TAMANHO_TILE-1
                )
                screen.fill((255, 0, 255), rect=rect)
                pygame.display.update()

                if must_sleep:
                    sleep(1)


    screen.blit(screen_copy, (0, 0))
    pygame.display.flip()
        
def desenhar_caminho(caminho_recente, ponto_start, ponto_dest):
    # Desenhar o ponto de partida
    pygame.draw.rect(screen, (0, 255, 242), (ponto_start[1] *
                                             TAMANHO_TILE, ponto_start[0]*TAMANHO_TILE, TAMANHO_TILE-1, TAMANHO_TILE-1))
    # Preencher o caminho com a cor vermelha


    if(desenhando_esferar):
        cor = choice(cores)
        cores.remove(cor)
    else:
        cor = (255, 0, 0)

    clock = pygame.time.Clock()
    for celula in caminho_recente:
        x, y = celula
        rect = pygame.Rect(y * TAMANHO_TILE, x * TAMANHO_TILE,
                           TAMANHO_TILE-1, TAMANHO_TILE-1)
        screen.fill(cor, rect=rect)
        pygame.display.update()
        clock.tick(25 if not desenhando_esferar else 75)

        if(not desenhando_esferar):
            cria_matriz_radar(x, y)


def get_random_esfers():

    for i in range(7):
        random_esfers.append([
            randint(0, 41),
            randint(0, 41)
        ])



def desenha_caminhos_destinos(destinos_d, old_as_start=False):
    partida = ponto_partida
    old = ponto_partida
    caminho_atual = []
    portaaberta = False


    for destino in destinos_d:

        # Obter o caminho encontrado pelo algoritmo A*
        caminho, custo_total = a_estrela(
            partida, destino,
        )
        caminho_atual = caminho

        
        if not old_as_start:
            caminho_str = ' -> '.join(str(i) for i in caminho)
            print(f'custo: {custo_total}')
            print(f'caminho: {caminho_str}')
    
        desenhar_caminho(caminho_atual, partida, destino)

        partida = ponto_partida if not old_as_start else old
        old = destino

        desenhas_esferas()


    desenhas_esferas()
    pygame.time.delay(500)


pygame.init()


screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))



for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()


draw_map(
    TAMANHO_TILE, screen
)

pygame.draw.rect(
    screen, (255, 0, 0), 
    (
    ponto_partida[1] * TAMANHO_TILE, ponto_partida[0]*TAMANHO_TILE, TAMANHO_TILE-1,
    TAMANHO_TILE-1,
    )
)

pygame.display.update()

pygame.time.delay(2500)

get_random_esfers()
desenhas_esferas()

# Destino iniciais
destinos = [
    (25, 5),
    (21, 0),
    (30, 12),
    (24, 12),
    (41, 0),
    (35, 0),
    (41, 41),
    (0, 0),
    (31, 41),
    (9, 0),
    (30, 35),
    (0, 20),
    (21, 41),
    (0, 41),
    (0, 32)
]

desenha_caminhos_destinos(destinos, True)

# Definir o terreno manualmente
screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

draw_map(
    TAMANHO_TILE, screen
)


if(len(esferar_encontradas) == 7):
    print("Todas as esferar encontradas!")
else:
    print("Fazendo hard-search")
    dests = [
        [(0, 0), (0, 41)],
        [(6, 0), (6, 41)],
        [(12, 0), (12, 41)],
        [(18, 0), (18, 41)],
        [(24, 0), (24, 41)],
        [(30, 0), (30, 41)],
        [(36, 0), (36, 41)],
        [(40, 0), (40, 41)],
    ]

    for d in dests:
        caminho = []
        ponto_inicio = d[0]
        i_caminhi = 0

        while i_caminhi < d[1][1]:
            caminho.append((d[0][0], i_caminhi))
            i_caminhi += 3
    
        desenhas_esferas()

        desenhar_caminho(caminho, ponto_inicio, d[1])


    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

    draw_map(
        TAMANHO_TILE, screen
    )


desenhando_esferar = True
desenha_caminhos_destinos(esferar_encontradas)

print("Todas as esferas foram encontradas.")
sound_effect.fadeout(1)
esfera_found.play()
input()


