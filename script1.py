import os # importando o módulo sistema operacional

# Para o arquivo dados1.txt
arquivo1 = open("dados1.txt")  # Caminho relativo
arquivo2 = open("C:/Users/jessi/Desktop/EAD/dados1.txt")  # Caminho absoluto

# Para o arquivo dados2.txt
arquivo3 = open("documentos/dados2.txt")  # Caminho relativo
arquivo4 = open("C:/Users/jessi/Desktop/EAD/documentos/dados2.txt")  # Caminho absoluto

print(os.path.relpath(arquivo1.name)) # relpath imprime o caminho relativo
print(os.path.abspath(arquivo2.name)) # abspath imprime o caminho absoluto
print(os.path.relpath(arquivo3.name))
print(os.path.abspath(arquivo4.name))

print(arquivo1)
print(arquivo2)
print(arquivo3)
print(arquivo4)

