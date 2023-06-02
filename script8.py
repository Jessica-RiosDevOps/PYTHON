arquivo = open("dados.txt", "r")

conteudo = arquivo.read() # Lemos todo seu conteúdo utilizando o método read, que é impresso na linha 5. 
print("Todo o conteúdo do arquivo")
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read() #Utilizamos o método read para ler novamente o conteúdo do arquivo e atribuímos o valor retornado à variável conteudo_releitura
print("Releitura de todo o conteúdo do arquivo")
print(repr(conteudo_releitura), '\n') # imprimimos o conteúdo dessa variável, que, conforme exibido no console, é uma string vazia ('').

arquivo.close() # fechou o arquivo 


arquivo_reaberto = open("dados.txt", "r") # abriu novamente o arquivo

conteudo_reaberto = arquivo_reaberto.read() # utilizamos novamente o método read e imprimimos o conteúdo retornado na linha 18
print("Todo o conteúdo do arquivo novamente")
print(repr(conteudo_reaberto), '\n')

arquivo_reaberto.seek(0) # Para demonstrar a utilização do método seek, no mesmo arquivo que já estava aberto, arquivo_reaberto, utilizamos o método seek(0), 
conteudo_seek = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo após o SEEK")
print(repr(conteudo_seek))

arquivo_reaberto.close()
