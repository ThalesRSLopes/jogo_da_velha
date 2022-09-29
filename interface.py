from tkinter import *


def jogada(pos):
    global jogador, texto_vencedor
    if not jogo_encerrado:
        if pos['text'] == '.':
            if jogador == 1:
                pos['text'] = 'X'
                jogador = 2
            else:
                pos['text'] = 'O'
                jogador = 1
        if verifica_jogo():
            if jogador == 1:
                texto_vencedor['text'] = 'O jogador 2 venceu!!!'
            else:
                texto_vencedor['text'] = 'O jogador 1 venceu!!!'


# Verifica as possíveis combinações onde um dos jogadores venceu a partida
def verifica_jogo():
    global p00, p01, p02, p10, p11, p12, p20, p21, p22, jogo_encerrado, texto_vencedor
    if (p00['text'] == p01['text'] == p02['text'] and p00['text'] != '.') or \
            (p00['text'] == p10['text'] == p20['text'] and p00['text'] != '.') or \
            (p00['text'] == p11['text'] == p22['text'] and p00['text'] != '.') or \
            (p01['text'] == p11['text'] == p21['text'] and p01['text'] != '.') or \
            (p02['text'] == p12['text'] == p22['text'] and p02['text'] != '.') or \
            (p02['text'] == p11['text'] == p20['text'] and p02['text'] != '.') or \
            (p10['text'] == p11['text'] == p12['text'] and p10['text'] != '.') or \
            (p20['text'] == p21['text'] == p22['text'] and p20['text'] != '.'):
        jogo_encerrado = True
        return True

    if p00['text'] != '.' and p01['text'] != '.' and p02['text'] != '.' and \
            p10['text'] != '.' and p11['text'] != '.' and  p12['text'] != '.' and \
            p20['text'] != '.' and p21['text'] != '.' and  p22['text'] != '.':
        texto_vencedor['text'] = 'Deu velha! Reinicie o jogo!'


def reseta_jogo():
    global p00, p01, p02, p10, p11, p12, p20, p21, p22, jogo_encerrado, texto_vencedor, jogador
    jogo_encerrado = False
    p00['text'] = '.'
    p01['text'] = '.'
    p02['text'] = '.'
    p10['text'] = '.'
    p11['text'] = '.'
    p12['text'] = '.'
    p20['text'] = '.'
    p21['text'] = '.'
    p22['text'] = '.'
    texto_vencedor['text'] = ' '
    jogador = 1


# Variáveis para manter o estado do jogo
jogador = 1  # Alterna o jogador entre 1 e 2. O jogador 1 joga com o 'X' e o 2 com o 'O'
jogo_encerrado = False  # Define se o jogo acabou ou não. É verdadeiro quando alguem ganha ou quando da velha

# --- Configurando a interface ---
font_titulo = ("Comic Sans MS", 20, "bold")  # Fonte do título
font_texto = ("Comic Sans MS", 15, "bold")  # Fonte do subtítulo

janela = Tk()  # Cria uma janela de interface
janela.title('Jogo da velha')  # Nome da janela
janela.geometry('440x480')  # Tamanho da janela
janela.resizable(False, False)  # Não permite que seja possível mudar o tamanho da janela
janela.iconbitmap('icon.ico')  # Altera o icone do app

texto_titulo = Label(janela, text='JOGO DA VELHA', font=font_titulo)
texto_titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=3)

texto_subtitulo = Label(janela, text='Bem vindo(a) ao jogo da velha. Divirta-se!', font=font_texto)
texto_subtitulo.grid(column=0, row=1, padx=10, pady=10, columnspan=3)

# Desenha as linhas do tabuleiro
canva = Canvas(janela, width=300, height=300)
canva.grid(column=0, row=2, padx=0, pady=0, columnspan=3, rowspan=3)
canva.create_line(0, 100, 300, 100, width=3)
canva.create_line(100, 0, 100, 300, width=3)
canva.create_line(200, 0, 200, 300, width=3)
canva.create_line(0, 200, 300, 200, width=3)

# Escreve as posições
# Posição (0,0)
p00 = Label(janela, text='.', font=font_titulo)
p00.grid(column=0, row=2, padx=0, pady=0, sticky='e')

# Posição (0,1)
p01 = Label(janela, text='.', font=font_titulo)
p01.grid(column=1, row=2, padx=0, pady=0)

# Posição (0,2)
p02 = Label(janela, text='.', font=font_titulo)
p02.grid(column=2, row=2, padx=0, pady=0, sticky='w')

# Posição (1,0)
p10 = Label(janela, text='.', font=font_titulo)
p10.grid(column=0, row=3, padx=0, pady=0, sticky='e')

# Posição (1,1)
p11 = Label(janela, text='.', font=font_titulo)
p11.grid(column=1, row=3, padx=0, pady=0)

# Posição (1,2)
p12 = Label(janela, text='.', font=font_titulo)
p12.grid(column=2, row=3, padx=0, pady=0, sticky='w')

# Posição (2,0)
p20 = Label(janela, text='.', font=font_titulo)
p20.grid(column=0, row=4, padx=0, pady=0, sticky='e')

# Posição (2,1)
p21 = Label(janela, text='.', font=font_titulo)
p21.grid(column=1, row=4, padx=0, pady=0)

# Posição (2,2)
p22 = Label(janela, text='.', font=font_titulo)
p22.grid(column=2, row=4, padx=0, pady=0, sticky='w')

# definindo os clicáveis para execução do jogo
p00.bind('<Button-1>', lambda e: jogada(p00))
p01.bind('<Button-1>', lambda e: jogada(p01))
p02.bind('<Button-1>', lambda e: jogada(p02))
p10.bind('<Button-1>', lambda e: jogada(p10))
p11.bind('<Button-1>', lambda e: jogada(p11))
p12.bind('<Button-1>', lambda e: jogada(p12))
p20.bind('<Button-1>', lambda e: jogada(p20))
p21.bind('<Button-1>', lambda e: jogada(p21))
p22.bind('<Button-1>', lambda e: jogada(p22))

texto_vencedor = Label(janela, text=' ', font=font_texto)
texto_vencedor.grid(column=0, row=5, padx=10, pady=10, columnspan=2)

botao_reset = Button(janela, text='Reiniciar!', font=font_texto, command=reseta_jogo)
botao_reset.grid(column=2, row=5, columnspan=2)

janela.mainloop()  # Deixa a janela em loop para ser exibida
