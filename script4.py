arquivo = open("dados.txt", "r")

conteúdo = arquivo.read() # Foi utilizado o método read() do objeto arquivo para ler o conteúdo de dados.txt e armazená-lo na variável conteúdo.

print("Tipo do conteúdo:", type(conteúdo)) # Verificamos o tipo do conteúdo retornado pelo método read(), utilizando a função interna type.

print("Conteúdo retornado pelo read:")
print(repr(conteúdo)) # Foi utilizado a função interna repr para mostrar o conteúdo real da variável conteúdo.

arquivo.close()
