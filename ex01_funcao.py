print('Controle de Terrenos')
print('-' * 20)


def area(larg, comp):
    
    cal = (larg*comp)

    print(f'A área de um terreno {larg}x{comp} é de {cal}m². ')


l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))

area(l,c)


