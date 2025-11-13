import random  # importa a biblioteca random para gerar números aleatórios
numero = random.randint(1, 20)  # sorteia um número aleatório entre 1 e 20
print("Adivinhe o número entre 1 e 20!")  # mostra uma mensagem inicial para o usuário
palpite = 0  # inicializa a variável palpite com 0
while palpite != numero:  # enquanto o palpite for diferente do número secreto, continua pedindo
    palpite = int(input("Digite seu palpite: "))  # pede ao usuário um palpite e converte para inteiro
    if palpite < numero:  # se o palpite for menor que o número secreto
        print("O número é maior.")  # dá uma dica que o número é maior
    elif palpite > numero:  # se o palpite for maior que o número secreto
        print("O número é menor.")  # dá uma dica que o número é menor
print("Parabéns! Você acertou!")  # quando o palpite for igual ao número, mostra a mensagem de acerto

