
LINHAS = 42
COLUNAS = 42

ponto_partida = (19, 19)


LARGURA_TELA = 670
ALTURA_TELA = 670
TAMANHO_TILE = 16
cores = [
    (124, 252, 0),
    (244, 164, 96),
    (34, 139, 34),
    (139, 137, 137),
    (30, 144, 255),
    (0, 0, 0),
    (255, 255, 255),
    (255, 0, 0),
]   
  



# Definir as cores dos diferentes tipos de terreno
GRAMA = (124, 252, 0)
AREIA = (244, 164, 96)
FLORESTA = (34, 139, 34)
MONTANHA = (139, 137, 137)
AGUA = (30, 144, 255)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)


converte_variavel = {
    "GRAMA": GRAMA,
    "AREIA": AREIA,
    "FLORESTA": FLORESTA,
    "MONTANHA": MONTANHA,
    "AGUA": AGUA,
    "PRETO": PRETO,
    "BRANCO": BRANCO,
    "VERMELHO": VERMELHO
}

# Definir o custo de cada tipo de terrenocl
CUSTO = {
    GRAMA: 1,
    MONTANHA: 60,
    AGUA: 10
}




tipo_terreno = {
    "g": "GRAMA",
    "m": "MONTANHA",
    "w": "AGUA",
    "r": "VERMELHO"
}