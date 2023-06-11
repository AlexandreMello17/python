def somaImposto (taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo

taxa = float(input("Digite a taxa de impostos..: "))
c = float(input("Digite o custo..: "))

print ("Valor com imposto..: " , somaImposto(taxa,c))