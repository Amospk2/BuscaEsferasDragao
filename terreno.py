import pygame
from constants import *


def cria_terreno():
    terreno = []
    
    with open("./terreno.txt", "r") as arquivo:
        mapa = arquivo.readlines()
        for linha in mapa:
            temp = []
            for caracter in linha:
                if caracter != '\n':
                    temp.append(tipo_terreno[caracter])
            terreno.append(temp)
    return terreno


def convert_map():
    terreno = cria_terreno()
    terreno_convertido= []
    for linha in terreno:
        linha_convertida = []
        for item in linha:
            linha_convertida.append(converte_variavel[item])
        terreno_convertido.append(linha_convertida)
    return terreno_convertido

    
def draw_map(
    TAMANHO_TILE, screen
):

    terreno_convertido = convert_map()

    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            # Define a cor da célula com base no valor de custo
            if terreno_convertido[linha][coluna] == GRAMA:
                cor = (140, 211, 70)  # Verde para a grama
            elif terreno_convertido[linha][coluna] == AREIA:
                cor = (196, 188, 148)  # Amarelo para a areia
            elif terreno_convertido[linha][coluna] == FLORESTA:
                cor = (1, 115, 53)  # Verde escuro para a floresta
            elif terreno_convertido[linha][coluna] == MONTANHA:
                cor = (82, 70, 44)  # Cinza para a montanha
            elif terreno_convertido[linha][coluna] == AGUA:
                cor = (45, 72, 181)  # Azul para a água
            elif terreno_convertido[linha][coluna] == PRETO:
                cor = (0, 0, 0)  # PRETO
            elif terreno_convertido[linha][coluna] == BRANCO:
                cor = (255, 255, 255)  # BRANCO
            elif terreno_convertido[linha][coluna] == VERMELHO:
                cor = (255, 0, 0)  # VERMELHO

            # Desenhar o tile na tela
            pygame.draw.rect(screen, cor, (coluna * TAMANHO_TILE,
                                           linha * TAMANHO_TILE, TAMANHO_TILE-1, TAMANHO_TILE-1))