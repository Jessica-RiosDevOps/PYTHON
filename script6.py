arquivo = open("dados.txt", "r")

conteudo = arquivo.readlines() # Retorna uma lista em que cada item da lista é uma linha do arquivo.

print("Tipo do conteúdo:", type(conteudo))

print("Conteúdo retornado pelo readlines:")
print(repr(conteudo))

arquivo.close()
