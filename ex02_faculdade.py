def exer02():
    arquivo = 'lista.txt'
    with open(arquivo, 'a') as agenda:
        agenda.write('\nMatheus')
    with open(arquivo, 'r') as agenda:
        for nome in agenda:
            print(nome, end='')
