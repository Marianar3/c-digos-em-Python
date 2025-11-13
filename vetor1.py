def busca_linear(vetor, valor):
    """
    Função que realiza busca linear.
    Retorna o índice do valor procurado, ou -1 se não encontrar.
    """
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i
    return -1
import random
vetor = [random.randint(0, 100) for _ in range(25)]
print("Vetor:", vetor)
valor = int(input("Digite o valor que deseja buscar: "))
posicao = busca_linear(vetor, valor)
if posicao != 0:
    print(f"O valor {valor} foi encontrado na posição {posicao}.")
else:
    print(f"O valor {valor} não foi encontrado no vetor.")
