val1 = int(input("Quantidade de produtos..:"))
preco1 = float(input("Valor dos primeiros produtos..:"))
val2 = int(input("Quantidade do segundo produto..:"))
preco2 = float(input("Valor dos segundos produtos..:"))
subtotal1 = (val1*preco1)
subtotal2 = (val2*preco2)
somatotalG = (subtotal1+subtotal2)
somatotalG2 = (somatotalG*0.05) 

if (somatotalG > 200):
    print ("Você ganhou um desconto de 5%!!!")
    print ("Valor com desconto..:" , somatotalG2) 

else:
     print("Compre acima de 200,00 para ganhar um super desconto!!!")