print('==== MENU ====')

print('0 - Sair')
print('1 - Adicionar pessoas')
print('2 - Listar pessoas')
print('3 - Atualizar informações')
print('4 - Excluir pessoa')

escolha = int(input('Defina o que quer fazer: '))

def add_pessoas():

    while escolha == 1:
        nome = str(input('Digite o nome: '))
        idade = (input('Digite a idade: '))
        
        with open('pessoas.txt', 'a') as arquivo:
            arquivo.write(f'{nome}, {idade}\n')
        

        if escolha == 0:
            break
    
add_pessoas()

def listar_pessoas():
    with open ('pessoas.txt' , 'r') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(',')
            print(f'Nome: {nome}, Idade: {idade}')

listar_pessoas()

def mudar_info():
    nome_antigo = input('Digite o nome da pessoa que quer alterar os dados: ')
    with open ('pessoas.txt' , 'r') as arquivo:
        ler = arquivo.readlines()
    
    for i, ler in (ler):
        nome, idade = ler.strip().split(',')

        if nome == nome_antigo:
            nome_novo = str(input('Digite o novo nome: '))
            idade_nova = int(input('Digite a nova idade: '))

            ler[i] = f'{nome_novo}, {idade_nova}\n'

            with open('pessoas.txt' , 'w') as arquivo:
                arquivo.writelines(ler)
        print('Dados alterados!')

mudar_info()
    
def remover_pessoa():
    print('Digite o nome que quer remover: ')

    with open ('pessoas.txt' , 'r') as arquivo:
        remover = arquivo.readlines()
    
    for i in remover:
        del remover[i]

        with open ('pessoas.txt', 'w') as arquivo:
            arquivo.writelines(remover)
        print('Pessoa removida!')




