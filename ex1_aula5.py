nota = int (input("Digite sua nota..: "))

while (nota < 0 or nota > 10):
    print("Digite uma nota válida.")
    break
else:
    print("Sua nota é..: " , nota)
    
