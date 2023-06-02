arquivo = open("dados.txt", "r")

conteudo = arquivo.readline() # READLINE retorna uma linha de arquivo incluindo caracteres de final (\n ou \r\n) e avança o cursor para a próxima

print("Tipo do conteúdo:", type(conteudo)) # Verificamos o tipo do conteúdo retornado pelo método readline(), utilizando a função interna type.

print("Conteúdo retornado pelo readline:")
print(repr(conteudo)) # Foi utilizado a função interna repr para mostrar o conteúdo real da variável conteúdo.

proximo_conteudo = arquivo.readline()

print("Próximo Conteúdo retornado:")
print(repr(proximo_conteudo))

arquivo.close()
