import copy


def preencher_diagonais(tab, y, x):
    tab[y][x] = 2
    stop = False
    de1x = x
    de1y = y
    de2x = x
    de2y = y
    dd1x = x
    dd1y = y
    dd2x = x
    dd2y = y
    diagonais_preenchidas = [0, 0, 0, 0]  # conta as 4 direções das diagonais
    while True:
        if de1x > 0 and de1y > 0:
            de1x -= 1
            de1y -= 1
            tab[de1y][de1x] = 1
        else:
            diagonais_preenchidas[0] = 1
        if de2x < len(tab[0]) - 1 and de2y < len(tab) - 1:
            de2x += 1
            de2y += 1
            tab[de2y][de2x] = 1
        else:
            diagonais_preenchidas[1] = 1
        if dd1x < len(tab[0]) - 1 and dd1y > 0:
            dd1x += 1
            dd1y -= 1
            tab[dd1y][dd1x] = 1
        else:
            diagonais_preenchidas[2] = 1
        if dd2x > 0 and dd2y < len(tab) - 1:
            dd2x -= 1
            dd2y += 1
            tab[dd2y][dd2x] = 1
        else:
            diagonais_preenchidas[3] = 1
        if diagonais_preenchidas == [1, 1, 1, 1]:
            break


def preencher_vertical_horizontal(tab, y, x):
    # vertical
    for i in range(len(tab)):
        tab[i][x] = 1
    # horizontal
    for j in range(len(tab[0])):
        tab[y][j] = 1


def funcao_heuristica(tab):
    cont_vazia = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:
                cont_vazia += 1
    return cont_vazia


def printTab(tab):
    for i in range(len(tab)):
        print(tab[i])


tab = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

while True:
    maior_fe = 0
    melhor_filho = None
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:  # se for 0 -> filho
                filho = copy.deepcopy(tab)
                preencher_vertical_horizontal(filho, i, j)
                preencher_diagonais(filho, i, j)
                filho[i][j] = 2
                fe = funcao_heuristica(filho)
                if fe > maior_fe:
                    maior_fe = fe
                    melhor_filho = filho
    # depois do loop na matriz
    if maior_fe == 0:  # acabou preencheu tudo
        break
    tab = melhor_filho
    print("Melhor filho selecionado:")
    printTab(tab)
    print("fe", maior_fe)
