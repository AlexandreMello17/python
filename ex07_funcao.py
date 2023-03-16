def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é igual a {fatorial(numero)}')
