from tkinter import *


janela = Tk()
janela.title("Login")

def click_button():
    login = ed1.get()
    senha = ed2.get()
    if login == "alexandre.estacio123@gmail.com" and senha == "alexandre123":
        lb3 = Label(janela, text= "Login Efetuado!")
        lb3.grid(row=4, column=1)

    else: 
        lb4 = Label(janela, text= "Login ou senha incorretos!")
        lb4.grid(row=4, column=1)    



lb1 = Label(janela, text="Login: ")
lb1.grid(row=0, column=0)

lb2 = Label(janela, text="Senha: ")
lb2.grid(row=1, column=0)

ed1 = Entry(janela)
ed1.grid(row=0, column=1)

ed2 = Entry(janela, show = "*")
ed2.grid(row=1, column=1)

bt1 = Button(janela, text="ENTRAR", command=click_button)
bt1.grid(row=2, column=1)

janela.geometry("200x100")


janela.mainloop()



