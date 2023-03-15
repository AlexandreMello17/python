from time import sleep 


def maior(*num):
    cont = maior = 0
    tam = len(num)
    print('-' * 20)
    print('ANALISANDO OS VALORES INFORMADOS...')
    for valor in num:
        print(f'{valor} ', end='' , flush = True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram inseridos os números {num} e são ao todo {tam} números. ')
    
    if 10 > 8 > 5 > 3:
        print(f'O maior número é..: {maior}')


#Programa de fato
maior(5, 3, 8 , 10)
maior(3, 2, 9, 8, 6)
maior(8)
maior()
