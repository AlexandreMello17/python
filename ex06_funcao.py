def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento


    if idade >= 18:
        print(f'Você possui {idade} anos, logo seu voto é OBRIGATÓRIO.')


    if idade >= 65:
        print(f'Você possui {idade} anos, logo seu voto é OPCIONAL.')   


    if idade < 16:
        print(f'Você possui {idade} anos, logo seu voto é NEGADO.')

    if 16 <= idade < 18:
        print(f'Você possui {idade} anos, logo seu voto é OPCIONAL.')  

ano_nascimento = int(input('Digite o seu ano de nascimento:  '))
voto(ano_nascimento)







