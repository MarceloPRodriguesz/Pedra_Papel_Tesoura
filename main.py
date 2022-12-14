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

# Adicionando opção escolhida pelo computador
opcao_computador = Label(frame_baixo, text="", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
opcao_computador.place(x=190, y=10)

linha_empate = Label(frame_cima, text="", width='255', anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
linha_empate.place(x=0, y=95)

# Configurando o frame inferior

# Configurando os botões, codigo abaixo tem como objetivo carregar imagem, alterar tamanho da imagem
#criar um botão e atribuir a imagem carregada a esse botão.

# Botões

# Funções do jogo
# Definindo variaveis globais
global jogador
global computador
global rodadas
global pontos_jogador
global pontos_computador
 # Atribuindo valores iniciais as variaveis
pontos_jogador = 0
pontos_computador = 0 
rodadas = 5 

# Iniciando a partida
def jogar(escolha_jogador):
    global rodadas  
    global pontos_jogador 
    global pontos_computador
    
    if rodadas > 0:
        #print(rodadas)
        opcoes= ['Pedra', 'Papel', 'Tesoura']  
        computador = random.choice(opcoes) 
        opcao_computador['text']= computador
        opcao_computador['fg']= co1
        
        # caso empate
        if escolha_jogador == computador :
            linha_empate['bg']= co3
            jogador1_vencedor['bg']= co0
            computador_vencedor['bg']= co0
                    
        # Jogador vitoria
        elif escolha_jogador == 'Pedra' and computador == 'Tesoura' : 
            linha_empate['bg']= co0
            jogador1_vencedor['bg']= co4
            computador_vencedor['bg']= co5
            pontos_jogador +=10     
            
        elif escolha_jogador == 'Papel' and computador == 'Pedra' : 
            linha_empate['bg']= co0
            jogador1_vencedor['bg']= co4
            computador_vencedor['bg']= co5
            pontos_jogador +=10
                        
        elif escolha_jogador == 'Tesoura' and computador == 'Papel' : 
            linha_empate['bg']= co0
            jogador1_vencedor['bg']= co4
            computador_vencedor['bg']= co5 
            pontos_jogador +=10  
            
        # Computador vitoria
        elif computador == 'Pedra' and escolha_jogador == 'Tesoura' : 
            linha_empate['bg']= co0
            jogador1_vencedor['bg']= co5
            computador_vencedor['bg']= co4 
            pontos_computador += 10  
            
        elif computador == 'Papel' and escolha_jogador == 'Pedra' : 
            linha_empate['bg']= co0
            jogador1_vencedor['bg']= co5
            computador_vencedor['bg']= co4
            pontos_computador += 10  
            
        elif computador == 'Tesoura' and escolha_jogador == 'Papel' : 
            linha_empate['bg']= co0
            jogador1_vencedor['bg']= co5
            computador_vencedor['bg']= co4
            pontos_computador += 10 
        
              # Atribuindo pontos ao placar 
        jogador1_pontos['text'] = pontos_jogador 
        computador_pontos['text'] = pontos_computador           
       
        
        # Atualizando o número de rodadas 
        rodadas = rodadas - 1
    else:
        jogador1_pontos['text'] = pontos_jogador 
        computador_pontos['text'] = pontos_computador
        
        encerra_jogo()         
    
# Habilitando botoes
def habilitar_botoes():
    global icone_papel
    global icone_pedra
    global icone_tesoura
    global botao_papel
    global botao_pedra
    global botao_tesoura
    
    botao_jogar.destroy()
    
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
    global rodadas  
    global pontos_jogador 
    global pontos_computador
    
    # Reiniciando variaveis
    pontos_jogador = 0
    pontos_computador = 0 
    rodadas = 5 
    
    # Destruindo botões 
    botao_papel.destroy()
    botao_tesoura.destroy()
    botao_pedra.destroy()
    
    # Definindo vencedor
    total_jogador = int(jogador1_pontos['text'])
    total_computador = int(computador_pontos['text'])
    
    if total_jogador > total_computador:
        vencedor = Label(frame_baixo, text="Parabéns, você ganhou!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co4)
        vencedor.place(x=5, y=60)
    elif total_computador > total_jogador:
        vencedor = Label(frame_baixo, text="Infelizmente, você perdeu!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        vencedor.place(x=5, y=60)
    else:
        vencedor = Label(frame_baixo, text="Esta partida terminou empatada!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co3)
        vencedor.place(x=5, y=60)
        
    def jogar_novamente():
        computador_pontos['text']= '0'
        jogador1_pontos['text'] = '0'
        vencedor.destroy()
        
        botao_jogar_novamente.destroy()
        
        habilitar_botoes()
        
    botao_jogar_novamente = Button(frame_baixo,command=jogar_novamente, width=30, text="JOGAR NOVAMENTE", bg=fundo, fg=co0, font=('Ivy 10 bold'),
                     anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    botao_jogar_novamente.place(x=5, y=151)
    
 
# Configurações do botão jogar     
botao_jogar = Button(frame_baixo,command=habilitar_botoes, width=30, text="JOGAR", bg=fundo, fg=co0, font=('Ivy 10 bold'),
                     anchor=CENTER, relief=RAISED, overrelief=RIDGE)
botao_jogar.place(x=5, y=151)

# janela executando infinitamente
janela.mainloop()