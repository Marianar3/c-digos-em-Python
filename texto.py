texto = input("Digite um texto: ")  # pede um texto ao usuário
invertido = ""  # cria uma variável vazia para guardar o texto invertido
for letra in texto:  # percorre cada letra do texto
    invertido = letra + invertido  # adiciona cada letra na frente do que já estava
print("Texto ao contrário:", invertido)  # mostra o texto invertido
