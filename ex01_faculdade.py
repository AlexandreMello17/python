def exercicio01():
    agenda = open('lista.txt' , 'x')
    nome = ['Alexandre, Ana Julia, Alison, Luiza']
    agenda.writelines(nome)
    agenda.close()

exercicio01()