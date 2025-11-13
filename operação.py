numero01 = float(input("Digite o primeiro número: "))  # pede o primeiro número e converte para float
numero02 = float(input("Digite o segundo número: "))   # pede o segundo número e converte para float
operacao = input("Digite a operação (+, -, *, /): ")    # pede a operação ao usuário

if operacao == "+":  # verifica se a operação é soma
    print(numero01 + numero02)  # realiza a soma e mostra o resultado
else:
    if operacao == "-":  # verifica se a operação é subtração
        print(numero01 - numero02)  # realiza a subtração e mostra o resultado
    else:
        if operacao == "*":  # verifica se a operação é multiplicação
            print(numero01 * numero02)  # realiza a multiplicação e mostra o resultado
        else:
            if operacao == "/":  # verifica se a operação é divisão
                print(numero01 / numero02)  # realiza a divisão e mostra o resultado
            else:
                print("Operação inválida!")  # caso a operação digitada não seja válida

