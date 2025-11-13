# Lista com 20 números (deve estar ORDENADA para busca binária funcionar)
numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
           22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

# Solicita o número que o usuário quer procurar
busca = int(input("Digite o número que deseja procurar: "))

# Definindo os limites da busca
inicio = 0
fim = len(numeros) - 1
encontrado = False
passo = 1  # contador para mostrar as etapas

# Busca binária com exibição passo a passo
while inicio <= fim:
    meio = (inicio + fim) // 2
    print(f"\nPasso {passo}:")
    print(f"Início = {inicio}, Fim = {fim}, Meio = {meio}, Valor do meio = {numeros[meio]}")

    if numeros[meio] == busca:
        print(f"\n✅ Número {busca} encontrado na posição {meio} da lista!")
        encontrado = True
        break
    elif numeros[meio] < busca:
        print(f"O número {busca} é MAIOR que {numeros[meio]}, então busca segue para a direita.")
        inicio = meio + 1
    else:
        print(f"O número {busca} é MENOR que {numeros[meio]}, então busca segue para a esquerda.")
        fim = meio - 1

    passo += 1

if not encontrado:
    print(f"\n❌ O número {busca} não foi encontrado na lista.")
