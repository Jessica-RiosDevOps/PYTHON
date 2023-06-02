arquivo = open("dados.txt", "r")

print("Iterando sobre o arquivo")
for linha in arquivo: # Foi utilizado o laço for para iterar diretamente sobre a variável arquivo.
    print(repr(linha)) #Para cada iteração, recebemos uma nova linha do arquivo, disponibilizada na variável linha.

arquivo.close()
