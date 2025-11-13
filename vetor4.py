import random
vetor = [random.randint(1, 100) for _ in range(25)]
print("Vetor original:")
print(vetor)
def insertion_sort(arr):  
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr
vetor_ordenado = insertion_sort(vetor)
print("\nVetor ordenado:")
print(vetor_ordenado)
