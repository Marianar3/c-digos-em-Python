palavra = "banana"
letras_certas = []
tentativas = 6
print("Bem-vindo ao Jogo da Forca!")
while tentativas > 0:
    # Mostrar palavra com letras descobertas
    exibicao = ""
    for letra in palavra:
        if letra in letras_certas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    print("\nPalavra:", exibicao.strip())
    # Verificar vitória
    if all(letra in letras_certas for letra in palavra):
        print("Parabéns! Você acertou a palavra:", palavra)
        break
    # Pedir letra
    chute = input("Digite uma letra: ").lower()
    if chute in palavra and chute not in letras_certas:
        letras_certas.append(chute)
        print("Letra correta!")
    else:
        tentativas -= 1
        print("Letra errada! Tentativas restantes:", tentativas)
if tentativas == 0:
    print("\nVocê perdeu! A palavra era:", palavra)
