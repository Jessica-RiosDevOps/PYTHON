# Script de manipulação de dados em arquivos

arquivo = open("dados.txt") # A função open é parar abrir um arquivo

print("Nome do arquivo:", arquivo.name) # O atributo name é para trazer o nome do arquivo
print("Modo do arquivo:", arquivo.mode) # O atributo mode é para trazer o modo do arquivo, se é 'r' leitura, 'w' escrita, 'a' acrescentar, 'b' binário, 'r+' leitura ou escrita.
print("Arquivo fechado?", arquivo.closed) # 

arquivo.close()

print("Arquivo fechado?", arquivo.closed)

