import tkinter
from tkinter import *
from tkinter import ttk 

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


# janela executando infinitamente
janela.mainloop()