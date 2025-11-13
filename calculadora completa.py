import math  # Importa o módulo math para usar funções matemáticas avançadas

print("=== Calculadora Interativa Completa ===")  # Mostra o título da calculadora

while True:  # Inicia um loop que vai repetir até o usuário sair
    print("\nOperações disponíveis:")  # Mostra as opções de operações
    print(" +  : Adição")  # Indica a operação de soma
    print(" -  : Subtração")  # Indica a operação de subtração
    print(" *  : Multiplicação")  # Indica a operação de multiplicação
    print(" /  : Divisão")  # Indica a operação de divisão
    print(" ** : Potência")  # Indica a operação de potência
    print(" %  : Módulo")  # Indica a operação de resto da divisão
    print(" sqrt : Raiz quadrada")  # Indica a operação de raiz quadrada
    print(" !  : Fatorial")  # Indica a operação de fatorial
    print(" log : Logaritmo")  # Indica a operação de logaritmo natural
    print(" sin : Seno")  # Indica a operação de seno
    print(" cos : Cosseno")  # Indica a operação de cosseno
    print(" tan : Tangente")  # Indica a operação de tangente
    print(" exit : Sair da calculadora")  # Indica como sair da calculadora

    operacao = input("\nEscolha a operação: ").lower()  # Pede a operação ao usuário e transforma em minúscula

    if operacao == "exit":  # Se o usuário digitar "exit"
        print("Saindo da calculadora...")  # Mostra mensagem de saída
        break  # Encerra o loop e sai do programa

    # Verifica se a operação precisa de apenas um número
    if operacao in ["sqrt", "!", "sin", "cos", "tan", "log"]:
        num = float(input("Digite o número: "))  # Pede um único número
    else:
        num1 = float(input("Digite o primeiro número: "))  # Pede o primeiro número
        num2 = float(input("Digite o segundo número: "))  # Pede o segundo número

    # Executa a operação escolhida
    if operacao in ["+", "adição"]:
        resultado = num1 + num2  # Soma
    elif operacao in ["-", "subtração"]:
        resultado = num1 - num2  # Subtração
    elif operacao in ["*", "multiplicação"]:
        resultado = num1 * num2  # Multiplicação
    elif operacao in ["/", "divisão"]:
        if num2 != 0:  # Evita divisão por zero
            resultado = num1 / num2  # Divisão
        else:
            resultado = "Erro: divisão por zero!"  # Mensagem de erro
    elif operacao in ["**", "potência"]:
        resultado = num1 ** num2  # Potência
    elif operacao in ["%", "módulo"]:
        resultado = num1 % num2  # Resto da divisão
    elif operacao == "sqrt":
        if num >= 0:  # Raiz só de números não-negativos
            resultado = math.sqrt(num)  # Raiz quadrada
        else:
            resultado = "Erro: raiz de número negativo!"  # Mensagem de erro
    elif operacao == "!":
        if num >= 0 and num.is_integer():  # Fatorial só de números inteiros não-negativos
            resultado = math.factorial(int(num))  # Calcula o fatorial
        else:
            resultado = "Erro: fatorial só de números inteiros não-negativos!"  # Mensagem de erro
    elif operacao == "log":
        if num > 0:  # Logaritmo só de números positivos
            resultado = math.log(num)  # Calcula logaritmo natural
        else:
            resultado = "Erro: logaritmo de número não positivo!"  # Mensagem de erro
    elif operacao == "sin":
        resultado = math.sin(math.radians(num))  # Calcula seno (converte grau para radiano)
    elif operacao == "cos":
        resultado = math.cos(math.radians(num))  # Calcula cosseno
    elif operacao == "tan":
        resultado = math.tan(math.radians(num))  # Calcula tangente
    else:
        resultado = "Operação inválida!"  # Caso a operação digitada não exista

    print("Resultado:", resultado)  # Mostra o resultado da operação


