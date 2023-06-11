from functools import partial
from tkinter import FALSE
from tkinter import Tk, ttk
from tkinter import messagebox
import sqlite3 
from tkinter import Frame
from tkinter import NSEW
from tkinter import Entry
from tkinter import Label
from tkinter import NW
from tkinter import Button
from tkinter import NE
import re
import tkinter as tk


# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters
 

janela = Tk()
janela.title('Login')
janela.geometry('500x400')
janela.configure(background=co1)
janela.resizable(width= FALSE, height= FALSE)


def criar_tabela_usuarios():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (nome TEXT, email TEXT, celular TEXT, senha TEXT)''')
    conn.commit()
    conn.close()


def criar_tabela_produtos():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS produtos
                 (nome TEXT, quantidade INTEGER, marca TEXT)''')
    conn.commit()
    conn.close()

criar_tabela_produtos()
criar_tabela_usuarios()



def cadastro_usuario():

    for widget in janela.winfo_children():
        widget.destroy()

    janela.title('Cadastro')
    janela.geometry('400x500')
    janela.configure(background=co1)
    janela.resizable(width=FALSE, height=FALSE)

    frame_superior = Frame(janela, width=310, height=50, bg=co1, relief='flat')
    frame_superior.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frame_inferior = Frame(janela, width=310, height=50, bg=co1, relief='flat')
    frame_inferior.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    l_cadastro = Label(frame_superior, text='CADASTRO', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
    l_cadastro.place(x=5, y=5)

    l_linha = Label(frame_superior, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=0, y=45)

    l_novo_login = Label(janela, text='Login *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_novo_login.place(x=10, y=60)
    
    e_novo_login = Entry(janela, width=20, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    e_novo_login.place(x=10, y=85)

    l_nova_senha = Label(janela, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nova_senha.place(x=10, y=120)

    e_nova_senha = Entry(janela, width=20, show='*', justify='left', font=("", 15), highlightthickness=1, relief='solid')
    e_nova_senha.place(x=10, y=145)

    l_novo_cpf = Label(janela, text='CPF *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_novo_cpf.place(x=10, y=185)

    e_novo_cpf = Entry(janela, width=20, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    e_novo_cpf.place(x=10, y=210)

    l_novo_celular = Label(janela, text='Celular *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_novo_celular.place(x=10, y=250)

    e_novo_celular = Entry(janela, width=20, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    e_novo_celular.place(x=10, y=275)

    l_novo_email = Label(janela, text='E-Mail *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_novo_email.place(x=10, y=323)

    e_novo_email = Entry(janela, width=20, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    e_novo_email.place(x=10, y=345)

    b_cadastrar = Button(janela, text='CADASTRAR', command=lambda: cadastro_database(e_novo_login, e_novo_cpf, e_novo_email, e_nova_senha, e_novo_celular), width=15, height=1, font=('Ivy 8 bold'), bg=co1, fg=co4)
    b_cadastrar.place(x=10, y=400)

    b_voltar_login = Button(janela, text='VOLTAR PARA LOGIN', command= voltar_login, width=20, height=1, font=('Ivy 8 bold'), bg=co1, fg=co4)
    b_voltar_login.place(x=200, y=400)


def cadastro_database(e_novo_login, e_novo_cpf, e_novo_email, e_nova_senha, e_novo_celular):
    
    login = e_novo_login.get()
    cpf = e_novo_cpf.get()
    email = e_novo_email.get()
    senha = e_nova_senha.get()
    celular = e_novo_celular.get()

    if not re.match("^[a-zA-Z ]+$", login):
        messagebox.showerror("Erro", "Nome inválido")
        return
    
    if not re.match("^\d{11}$", cpf):
        messagebox.showerror("Erro", "CPF inválido")
        return
    
    if not re.match("^[a-zA-Z0-9]{1,8}$", senha):
        messagebox.showerror("Erro", "Senha inválida")
        return
    
    if not re.match("^\d{11}$", celular):
        messagebox.showerror("Erro", "Celular inválido")
        return


    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?)", (login, email, cpf, senha))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso")




def voltar_login():
        
    for widget in janela.winfo_children():
        widget.destroy()

    janela.title('Login')
    janela.geometry('500x400')
    janela.configure(background=co1)
    janela.resizable(width=FALSE, height=FALSE)

    l_linha = Label(janela, text='', width=275, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=100, y=45)

    l_login = Label(janela, text='LOGIN', anchor=NE, font=('Ivy 15'), bg=co1, fg=co4)
    l_login.place(x=195, y=5)

    l_linha = Label(janela, text='', width=275, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=80, y=45)

    l_usuario = Label(janela, text='Login ', width=20, font=('Ivy 10'), bg=co1, fg=co4)
    l_usuario.place(x=130, y=80)

    e_cpf = Entry(janela, width=20, font=('', 15), highlightthickness=1, relief='solid')
    e_cpf.place(x=110, y=100)

    l_senha = Label(janela, text='Senha', font=('Ivy 10'), bg=co1, fg=co4)
    l_senha.place(x=190, y=150)

    e_senha = Entry(janela, width=20, font=('', 15), show='*', highlightthickness=1, relief='solid')
    e_senha.place(x=110, y=170)

    b_entrar = Button(janela, text='ENTRAR', command=cadastro_produtos, width=20, height=1, font=('Ivy 10 bold'), bg=co1, fg=co4)
    b_entrar.place(x=20, y=260)

    b_cadastrar = Button(janela, text='CADASTRAR', command=cadastro_usuario,  width=20, height=1, font=('Ivy 10 bold'), bg=co1, fg=co4)
    b_cadastrar.place(x=270, y=260)

    l_cadastrar = Label(janela, text='Quer se cadastrar?', font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_cadastrar.place(x=283, y=230)
    

def cadastro_produtos():
     
    for widget in janela.winfo_children():
        widget.destroy()

    janela.title('Cadastro de Produtos')
    janela.geometry('500x400')
    janela.configure(background=co1)
    janela.resizable(width=FALSE, height=FALSE)

    l_linha = Label(janela, text='', width=275, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=100, y=45)

    l_produtos = Label(janela, text='Produtos', anchor=NE, font=('Ivy 15'), bg=co1, fg=co4)
    l_produtos.place(x=195, y=5)

    l_linha = Label(janela, text='', width=275, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=100, y=45)

    l_tipo = Label(janela, text='Tipo do Produto ', width=20, font=('Ivy 10'), bg=co1, fg=co4)
    l_tipo.place(x=130, y=85)

    e_tipo = Entry(janela, width=20, font=('', 15), highlightthickness=1, relief='solid')
    e_tipo.place(x=110, y=110)

    l_marca = Label(janela, text='Marca do Produto ', width=20, font=('Ivy 10'), bg=co1, fg=co4)
    l_marca.place(x=130, y=150)

    e_marca = Entry(janela, width=20, font=('', 15), highlightthickness=1, relief='solid')
    e_marca.place(x=110, y=170)

    l_qnt = Label(janela, text='Quantidade ', width=20, font=('Ivy 10'), bg=co1, fg=co4)
    l_qnt.place(x=130, y=210)

    e_qnt = Entry(janela, width=20, font=('', 15), highlightthickness=1, relief='solid')
    e_qnt.place(x=110, y=230)

    b_confirmar = Button(janela, width = 20, text = 'CONFIRMAR', command= lambda: produtos_database(e_tipo, e_qnt, e_marca), height = 1, font=('Ivy 10 bold'), bg = co1, fg = co4)
    b_confirmar.place (x = 35, y = 300)

    b_atualizar = Button(janela, width = 20, text = 'ATUALIZAR PRODUTOS', command=partial(atualizar_produtos, e_tipo), height = 1, font=('Ivy 10 bold'), bg = co1, fg = co4)
    b_atualizar.place (x = 270, y = 300 )



def produtos_database(e_tipo, e_qnt, e_marca):
    
    produto = e_tipo.get()
    quantidade = e_qnt.get()
    marca = e_marca.get()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO produtos VALUES (?, ?, ?)", (produto, quantidade, marca))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso")



def atualizar_produtos(e_tipo):
    
    nome_produto = e_tipo.get()
    
    if not nome_produto:
        messagebox.showerror('Error', 'Insira o nome do produto que deseja editar.')
        return
    
    def salvar_edicao():
        novo_nome = e_novo_nome.get()
        nova_quantidade = e_nova_quantidade.get()
        nova_marca = e_nova_marca.get()

        if not novo_nome or not nova_quantidade or not nova_marca:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE produtos SET nome = ?, quantidade = ?, marca = ? WHERE nome = ?",
                 (novo_nome, nova_quantidade, nova_marca, nome_produto))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso.")
        edicao_janela.destroy()

    edicao_janela = tk.Toplevel(janela)
    edicao_janela.title("Editar Produto")
    edicao_janela.geometry("500x400")
    edicao_janela.resizable(height=False, width=False)

    nome_janela_produto_label = tk.Label(edicao_janela, text="Modificação de Produtos", font="Ivy 10")
    nome_janela_produto_label.pack()

    l_novo_nome = tk.Label(edicao_janela, text="Novo Nome:")
    l_novo_nome.pack()
    e_novo_nome = tk.Entry(edicao_janela)
    e_novo_nome.pack()

    l_nova_quantidade = tk.Label(edicao_janela, text="Nova Quantidade:")
    l_nova_quantidade.pack()
    e_nova_quantidade = tk.Entry(edicao_janela)
    e_nova_quantidade.pack()

    l_nova_marca = tk.Label(edicao_janela, text="Nova Marca:")
    l_nova_marca.pack()
    e_nova_marca = tk.Entry(edicao_janela)
    e_nova_marca.pack()

    b_salvar = tk.Button(edicao_janela, text="SALVAR", command=salvar_edicao)
    b_salvar.pack()
               

def fazer_login():
    email = e_email.get()
    senha = e_senha.get()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    resultado = c.fetchone()
    conn.close()

    if resultado:
        cadastro_produtos()
    
    else:
        messagebox.showinfo('ERROR', 'Login Inválido')               

l_linha = Label(janela, text='', width=275, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=100, y=45)

l_login = Label(janela, text='LOGIN', anchor=NE, font=('Ivy 15'), bg=co1, fg=co4)
l_login.place(x=195, y=5)

l_linha = Label(janela, text='', width=275, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=80, y=45)

l_email = Label(janela, text='EMAIL ', width=20, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=130, y=80)

e_email = Entry(janela, width=20, font=('', 15), highlightthickness=1, relief='solid')
e_email.place(x=110, y=100)

l_senha = Label(janela, text='Senha', font=('Ivy 10'), bg=co1, fg=co4)
l_senha.place(x=190, y=150)

e_senha = Entry(janela, width=20, font=('', 15), show='*', highlightthickness=1, relief='solid')
e_senha.place(x=110, y=170)

b_entrar = Button(janela, text='ENTRAR', command= fazer_login, width=20, height=1, font=('Ivy 8 bold'), bg=co1, fg=co4)
b_entrar.place(x=20, y=260)

b_cadastrar = Button(janela, text='CADASTRAR', command=cadastro_usuario,  width=20, height=1, font=('Ivy 8 bold'), bg=co1, fg=co4)
b_cadastrar.place(x=270, y=260)

l_cadastrar = Label(janela, text='Quer se cadastrar?', font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cadastrar.place(x=283, y=230)



janela.mainloop()

