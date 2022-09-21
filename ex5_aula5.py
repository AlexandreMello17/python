nota1 = float (input("Insira sua primeira nota..: "))
nota2 = float (input("Insira sua segunda nota..: "))

media = (nota1 + nota2 )/2

if (media > 7 and media < 10 ):
    print("Aprovado.")

elif (media < 7):
    print("Reprovado.")

elif (media == 10):
    print("Aprovado com distinção.")
