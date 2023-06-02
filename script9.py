arquivo_escrita = open("dados_write.txt", "w") # Abrimos no script9, o arquivo dados_write.txt ´para escrita utilizando o modo w 
arquivo_escrita.write("Conteúdo da primeira linha") # Escrevemos o conteúdo utilizando o método write, conforme linhas 2 e 3 e 4.
arquivo_escrita.write("\nConteúdo da segunda linha.")
arquivo_escrita.write("\nConteudo da terceira linha.")
arquivo_escrita.close() # fechamos o arquivo

