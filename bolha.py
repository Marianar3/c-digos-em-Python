import random
numeros = [random.randint(1, 100) for _ in range(25)]
print("Lista original:")
print(numeros)
for i in range(len(numeros) - 1):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
print("\nLista em ordem crescente:")
print(numeros)
for i in range(len(numeros) - 1):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] < numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
print("\nLista em ordem decrescente:")
print(numeros)