arquivo = open('textoaleatorio.txt' , 'w' , encoding = 'UTF-8')

texto1 = 'texto para adicionar no txt já feito. '

arquivo.writelines(texto1)

arquivo.close()

