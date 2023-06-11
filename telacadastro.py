from tkinter import *
from tkinter import Tk, ttk
 
# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters
 
janela = Tk()
janela.title('Cadastro Salão Espaço Vip')
janela.geometry('310x470')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)
 
frame_superior = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_superior.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
 
frame_inferior = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_inferior.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
 
l_nome = Label(frame_superior, text='CADASTRO', anchor=NE, font=('Ivy 25'), bg=co1, fg= co4)
l_nome.place(x=5, y=5)
 
l_linha = Label(frame_superior, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg= co4)

l_linha.place(x=0, y=45)
 
l_nome = Label(janela, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)

l_nome.place(x=10, y=60)
e_nome = Entry(janela, width=20, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=10, y=85)
 

l_senha = Label(janela, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
l_senha.place(x=10, y=120)

e_senha = Entry(janela, width=20, show='*', justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_senha.place(x=10, y=145)

l_cpf = Label(janela, text='CPF *', anchor = NW, font=('Ivy 10'), bg=co1, fg=co4)
l_cpf.place(x=10, y=185)

e_cpf = Entry(janela, width=20, justify = 'left', font=("", 15), highlightthickness=1, relief='solid')
e_cpf.place(x=10, y=210)

b_entrar = Button(janela, text='ENTRAR', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg= co1, relief=RAISED)
b_entrar.place(x=15, y=400)

l_email = Label(janela, text='E-Mail *', anchor = NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=10, y=250)

e_email = Entry(janela, width=20, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_email.place(x=10, y=275)

l_celular = Label(janela, text='Celular *', anchor = NW, font=('Ivy 10'), bg=co1, fg=co4)
l_celular.place(x=10, y= 310)

e_celular = Entry(janela, width=20, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_celular.place(x=10, y=340 )
 
janela.mainloop()