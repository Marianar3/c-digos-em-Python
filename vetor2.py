import random
vetor = [random.randint(1, 100) for _ in range(25)]
print("Vetor original:")
print(vetor)
def busca_binaria(arr, chave, inicio, fim):
    while inicio < fim:
        meio = (inicio + fim) // 2
        if arr[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio
    return inicio
def insertion_sort_binaria(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        pos = busca_binaria(arr, chave, 0, i)
        j = i
        while j > pos:
            arr[j] = arr[j - 1]
            j -= 1
        arr[pos] = chave
    return arr
vetor_ordenado = insertion_sort_binaria(vetor)
print("\nVetor ordenado:")
print(vetor_ordenado)
