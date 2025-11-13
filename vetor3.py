import random
vetor = [random.randint(1, 100) for _ in range(25)]
print("Vetor original:")
print(vetor)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
vetor_ordenado = selection_sort(vetor)
print("\nVetor ordenado:")
print(vetor_ordenado)
