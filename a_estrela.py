from celula import Celula
import math
from constants import *
from terreno import convert_map

def calcular_distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def heuristica(celula_atual, destino):
    return calcular_distancia(celula_atual.posicao, destino) * 10

def custo(celula_atual, vizinho):
    if vizinho in celula_atual.vizinhos:
        return celula_atual.custo + vizinho.custo
    else:
        return float('inf')

def a_estrela(ponto_start, destino):

    terreno_convertido = convert_map()

    # Criar as células do terreno
    celulas = [[Celula((linha, coluna), CUSTO[terreno_convertido[linha][coluna]])
                for coluna in range(COLUNAS)] for linha in range(LINHAS)]

    # Conectar as células aos seus vizinhos
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if linha > 0:
                celulas[linha][coluna].vizinhos.append(
                    celulas[linha-1][coluna])
            if linha < LINHAS-1:
                celulas[linha][coluna].vizinhos.append(
                    celulas[linha+1][coluna])
            if coluna > 0:
                celulas[linha][coluna].vizinhos.append(
                    celulas[linha][coluna-1])
            if coluna < COLUNAS-1:
                celulas[linha][coluna].vizinhos.append(
                    celulas[linha][coluna+1])

    # Inicializar as listas aberta e fechada
    aberta = []
    fechada = []

    # Adicionar o ponto de partida à lista aberta
    celula_atual = celulas[ponto_start[0]][ponto_start[1]]
    aberta.append(celula_atual)

    # Loop principal do algoritmo A*
    while aberta:
        # Encontrar a célula na lista aberta com o menor valor de f + h
        celula_atual = min(aberta, key=lambda celula: celula.f + celula.h)

        # Se a célula atual for o ponto de destino, retornar o caminho encontrado
        if celula_atual.posicao == destino:
            caminho = []
            custo_total = 0
            while celula_atual:
                caminho.append(celula_atual.posicao)
                celula_atual = celula_atual.pai
                if celula_atual:
                    custo_total += celula_atual.custo
            return (caminho[::-1], custo_total)

        # Remover a célula atual da lista aberta e adicioná-la à lista fechada
        aberta.remove(celula_atual)
        fechada.append(celula_atual)

        # Verificar todos os vizinhos da célula atual
        for vizinho in celula_atual.vizinhos:
            
            # Se o vizinho estiver na lista fechada, ignorá-lo
            if vizinho in fechada:
                continue

            # Calcular o custo do caminho da célula atual até o vizinho
            novo_g = celula_atual.g + custo(celula_atual, vizinho)

            # Se o vizinho não estiver na lista aberta, adicioná-lo
            if vizinho not in aberta:
                aberta.append(vizinho)
            # Se o novo caminho para o vizinho for mais longo do que o já calculado, ignorá-lo
            elif novo_g >= vizinho.g:
                continue

            # Atualizar os valores de g, h e f do vizinho
            vizinho.g = novo_g
            vizinho.h = heuristica(vizinho, destino)
            vizinho.f = vizinho.g + vizinho.h
            vizinho.pai = celula_atual

    return None
