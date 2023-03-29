def exer03():
    compras = open ('listamercado.txt', 'w' , encoding = 'UTF-8')
    itens = ['Carne\n', 'Leite\n', 'Batata\n', 'Limão\n']
    compras.writelines(itens)
    compras.close()

    
    
def add2():

    compras = open('listamercado.txt', 'a', encoding = 'UTF-8')
    additem = 1

    while additem!= 2:
        additem = str(input("Deseja adicionar algo na lista? Digite 1 para sim e 2 para nao.\n "))
        
        if additem == 1:
            additem = str(input("Digite o que quer adicionar.\n"))
        
        if additem == 2:
            break

        compras.writelines(additem+'\n')



add2()
exer03()
