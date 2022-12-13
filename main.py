import tkinter
import random
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

fundo = "#3b3b3b"

# definindo tamanho de janela 
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)




# dividindo a janela 
frame_cima = Frame(janela, width=260, height=100,bg=co1, relief='raised')
frame_cima.grid(row= 0, column= 0, sticky= NW)

frame_baixo = Frame(janela, width=260, height=300,bg=co0, relief='flat')
frame_baixo.grid(row= 1, column= 0, sticky= NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Criando labels do frame de cima
# Jogador 1 
jogador1_nome = Label(frame_cima, text="Voce", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
jogador1_nome.place(x=25, y=70)

jogador1_vencedor = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
jogador1_vencedor.place(x=0, y=0)

jogador1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
jogador1_pontos.place(x=50, y=20)

# Separador
separador = Label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
separador.place(x=120, y=20)

# Computador
computador_pontos = Label(frame_cima, text="0", anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
computador_pontos.place(x=170, y=20)

computador_vencedor = Label(frame_cima, text="", height='10', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
computador_vencedor.place(x=255, y=0)

computador_nome = Label(frame_cima, text="PC", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
computador_nome.place(x=205, y=70)


linha_empate = Label(frame_cima, text="", width='255', anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
linha_empate.place(x=0, y=95)

# Configurando o frame inferior

#**Configurando os botões, codigo abaixo tem como objetivo carregar imagem, alterar tamanho da imagem
#criar um botão e atribuir a imagem carregada a esse botão.

# Botões


# Funções do jogo
# definindo variaveis globais
global jogador
global computador
global rodadas
global pontos_jogador
global pontos_computador
# atribuindo valores iniciais as variaveis
pontos_jogador = 0
pontos_computador = 0 
rodadas = 5 

# Iniciando a partida
def jogar(escolha_jogador):
    rodadas
    pontos_computador
    pontos_jogador
    
    if rodadas > 0:
        print(rodadas)
        opcoes= ['Pedra', 'Papel', 'Tesoura']  
        computador = random.choice(opcoes) 
        
        jogador = escolha_jogador
        print(f"Computador escolhe:",computador)
        print(f"Jogador escolhe: ",escolha_jogador)
    else:
        encerra_jogo()   
  
    
# Habilitando botoes
def habilitar_botoes():
    global icone_papel
    global icone_pedra
    global icone_tesoura
    global botao_papel
    global botao_pedra
    global botao_tesoura
    
    icone_pedra = Image.open('C:/Users/USUARIO/OneDrive/Documentos/Projetos/PedraPapelTesoura/Imagens/pedra.png')
    icone_pedra = icone_pedra.resize((50,50), Image.ANTIALIAS)
    icone_pedra = ImageTk.PhotoImage(icone_pedra)
    botao_pedra = Button(frame_baixo,command=lambda: jogar('Pedra'), width=50, image=icone_pedra, compound=CENTER, bg=co0, fg=co0,
                        font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    botao_pedra.place(x=15, y=60)

    icone_papel = Image.open('C:/Users/USUARIO/OneDrive/Documentos/Projetos/PedraPapelTesoura/Imagens/papel.png')
    icone_papel = icone_papel.resize((50,50), Image.ANTIALIAS)
    icone_papel = ImageTk.PhotoImage(icone_papel)
    botao_papel = Button(frame_baixo,command=lambda: jogar('Papel'), width=50, image=icone_papel, compound=CENTER, bg=co0, fg=co0,
                        font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    botao_papel.place(x=95, y=60)

    icone_tesoura = Image.open('C:/Users/USUARIO/OneDrive/Documentos/Projetos/PedraPapelTesoura/Imagens/tesoura.png')
    icone_tesoura = icone_tesoura.resize((50,50), Image.ANTIALIAS)
    icone_tesoura = ImageTk.PhotoImage(icone_tesoura)
    botao_tesoura = Button(frame_baixo,command=lambda: jogar('Tesoura'), width=50, image=icone_tesoura, compound=CENTER, bg=co0, fg=co0,
                        font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    botao_tesoura.place(x=180, y=60)
    
# Termina partida
def encerra_jogo():
    pass  


botao_jogar = Button(frame_baixo,command=habilitar_botoes, width=30, text="JOGAR", bg=fundo, fg=co0, font=('Ivy 10 bold'),
                     anchor=CENTER, relief=RAISED, overrelief=RIDGE)
botao_jogar.place(x=5, y=151)


# janela executando infinitamente
janela.mainloop()