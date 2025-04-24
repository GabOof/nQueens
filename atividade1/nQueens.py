import copy


# Função que preenche as diagonais de uma casa ocupada por uma rainha
def preencherDiagonais(tabuleiro, y, x):
    tabuleiro[y][x] = 2  # Rainha

    # Define as diagonais
    diagonalEsquerdaSuperiorX = x
    diagonalEsquerdaSuperiorY = y
    diagonalEsquerdaInferiorX = x
    diagonalEsquerdaInferiorY = y
    diagonalDireitaSuperiorX = x
    diagonalDireitaSuperiorY = y
    diagonalDireitaInferiorX = x
    diagonalDireitaInferiorY = y

    diagonaisPreenchidas = [0, 0, 0, 0]  # Conta as 4 direções das diagonais

    # Preenche todas as diagonais referentes a casa ocupada por uma rainha
    while True:
        if diagonalEsquerdaSuperiorX > 0 and diagonalEsquerdaSuperiorY > 0:
            diagonalEsquerdaSuperiorX -= 1
            diagonalEsquerdaSuperiorY -= 1
            tabuleiro[diagonalEsquerdaSuperiorY][diagonalEsquerdaSuperiorX] = 1
        else:
            diagonaisPreenchidas[0] = 1
        if (
            diagonalEsquerdaInferiorX < len(tabuleiro[0]) - 1
            and diagonalEsquerdaInferiorY < len(tabuleiro) - 1
        ):
            diagonalEsquerdaInferiorX += 1
            diagonalEsquerdaInferiorY += 1
            tabuleiro[diagonalEsquerdaInferiorY][diagonalEsquerdaInferiorX] = 1
        else:
            diagonaisPreenchidas[1] = 1
        if (
            diagonalDireitaSuperiorX < len(tabuleiro[0]) - 1
            and diagonalDireitaSuperiorY > 0
        ):
            diagonalDireitaSuperiorX += 1
            diagonalDireitaSuperiorY -= 1
            tabuleiro[diagonalDireitaSuperiorY][diagonalDireitaSuperiorX] = 1
        else:
            diagonaisPreenchidas[2] = 1
        if (
            diagonalDireitaInferiorX > 0
            and diagonalDireitaInferiorY < len(tabuleiro) - 1
        ):
            diagonalDireitaInferiorX -= 1
            diagonalDireitaInferiorY += 1
            tabuleiro[diagonalDireitaInferiorY][diagonalDireitaInferiorX] = 1
        else:
            diagonaisPreenchidas[3] = 1
        if diagonaisPreenchidas == [1, 1, 1, 1]:
            break


# Função que preenche as linhas e colunas de uma casa ocupada por uma rainha
def preencherVerticalHorizontal(tabuleiro, y, x):
    # Preenche a vertical
    for i in range(len(tabuleiro)):
        tabuleiro[i][x] = 1
    # Preenche a horizontal
    for j in range(len(tabuleiro[0])):
        tabuleiro[y][j] = 1


# Função que conta quantas casas vazias existem na tabuleiro (ou seja, quantas rainhas ainda podem ser colocadas)
def funcaoHeuristica(tabuleiro):
    contadorCasasVazias = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 0:
                contadorCasasVazias += 1
    return contadorCasasVazias


# Função que imprime a tabuleiro
def printTabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        print(tabuleiro[i])


# Monta o tabuleiro vazio
tabuleiro = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# Preenche o tabuleiro com as rainhas
while True:
    maiorFuncaoHeuristica = 0
    melhorFilho = None

    # Busca posições vazias no tabuleiro, simula a colocação de uma rainha e seleciona o melhor tabuleiro filho com base na heurística
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 0:  # se for 0 -> filho
                filho = copy.deepcopy(tabuleiro)
                preencherVerticalHorizontal(filho, i, j)
                preencherDiagonais(filho, i, j)
                filho[i][j] = 2
                funcaoHeuristicaUtilizada = funcaoHeuristica(filho)
                if funcaoHeuristicaUtilizada > maiorFuncaoHeuristica:
                    maiorFuncaoHeuristica = funcaoHeuristicaUtilizada
                    melhorFilho = filho

    # Se não houver mais filhos, encerra o loop e imprime o tabuleiro final

    print("Melhor filho selecionado:")
    printTabuleiro(tabuleiro)
    print("Função Heurística", maiorFuncaoHeuristica)

    if maiorFuncaoHeuristica == 0:  # Acabou a busca, não há mais filhos

        print("Tabuleiro final:")
        printTabuleiro(tabuleiro)

        break

    tabuleiro = melhorFilho
