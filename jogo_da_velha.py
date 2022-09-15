############################################
#       DESENVOLVIDO POR THALES LOPES      #
# GitHub: https://github.com/ThalesRSLopes #
############################################

import numpy as np


# Gera um numpy array 3x3, onde serão armazenados os valores que serão utilizados
# para definir as jogadas
def cria_jogo():
    tabuleiro = np.zeros((3, 3))
    return tabuleiro


# Mostra o tabuleiro, substituindo os valores numéricos pelos valores corretos.
# Se uma posição está vazia, é mostrado o número dela, que será utilizado pelo jogador.
# Se a posição já foi escolhida, é mostrado um X (para o jogador 1) ou O (para o jogador 2).
def printa_tabuleiro(tabuleiro):
    l, c = tabuleiro.shape
    print("\n\n\n")
    for i in range(l):
        aux = '|'
        for j in range(c):
            if tabuleiro[i, j] == 0:
                aux += f' {(i*3)+j+1} |'
            elif tabuleiro[i, j] == 1:
                aux += ' X |'
            else:
                aux += ' O |'
        print(aux)


# Verifica as possíveis combinações onde um dos jogadores venceu a partida
def verifica_jogo(tabuleiro):
    if (tabuleiro[0, 0] == tabuleiro[0, 1] == tabuleiro[0, 2] and tabuleiro[0, 0] != 0) or \
            (tabuleiro[0, 0] == tabuleiro[1, 0] == tabuleiro[2, 0] and tabuleiro[0, 0] != 0) or \
            (tabuleiro[0, 0] == tabuleiro[1, 1] == tabuleiro[2, 2] and tabuleiro[0, 0] != 0) or \
            (tabuleiro[0, 1] == tabuleiro[1, 1] == tabuleiro[2, 1] and tabuleiro[0, 1] != 0) or \
            (tabuleiro[0, 2] == tabuleiro[1, 2] == tabuleiro[2, 2] and tabuleiro[0, 2] != 0) or \
            (tabuleiro[0, 2] == tabuleiro[1, 1] == tabuleiro[2, 0] and tabuleiro[0, 2] != 0) or \
            (tabuleiro[1, 0] == tabuleiro[1, 1] == tabuleiro[1, 2] and tabuleiro[1, 0] != 0) or \
            (tabuleiro[2, 0] == tabuleiro[2, 1] == tabuleiro[2, 2] and tabuleiro[2, 0] != 0):
        return True


# Gera uma lista que guarda as posições relativas de cada possível jogada
# por exemplo: a posição "1" do jogo é a posição (0, 0) do numpy array.
# Isso facilita ao encontrar a posição onde o jogador escolheu.
def gera_lista_pos():
    lista_pos = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    return lista_pos


if __name__ == '__main__':
    print('\tBEM VINDO AO JOGO DA VELHA!'
          '\no jogador 1 será o X e o jogador 2 será O')

    print('\nO jogo vai começar!!\n')
    tabuleiro = cria_jogo()
    printa_tabuleiro(tabuleiro)
    ganhou = False  # Variável de parada para quando alguém vencer
    velha = False  # Variável de parada caso todas as posições tenham sido usadas e ninguém ganhou
    jogador = 1  # Variável que verifica qual jogador deve jogar em seguida
    lista_pos = gera_lista_pos()
    jogadas = 0  # Guarda a quantidade de jogadas feitas. Caso seja igual e 9 e ninguém ganhou, é empate

    while(not ganhou and not velha):
        if jogadas == 9:
            print('\n\tDEU VELHA! EMPATE!')
            break
        error = True
        pos = int(input(f'\nVez do jogador {jogador}. Escolha uma posição: '))
        while error:
            if pos < 1 or pos > 9:
                pos = int(input('A posição digitada não é valida. Escolha uma posição válida entre 1 e 9: '))
            else:
                pos_jogada = lista_pos[pos-1]
                if tabuleiro[pos_jogada[0], pos_jogada[1]] != 0:
                    pos = int(input('A posição digitada já foi escolhida. Escolha outra posição: '))
                else:
                    tabuleiro[pos_jogada[0], pos_jogada[1]] = jogador
                    if jogador == 1:
                        jogador = 2
                    else:
                        jogador = 1
                    error = False
                    jogadas += 1

        printa_tabuleiro(tabuleiro)
        ganhou = verifica_jogo(tabuleiro)
        if ganhou:
            print(f'\nParabéns, o jogador {int(tabuleiro[pos_jogada[0], pos_jogada[1]])} venceu!')
