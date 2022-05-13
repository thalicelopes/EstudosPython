# Bubble Sort possui Dois laços de repetição

def BubbleSort(arr):
    tamanho = len(arr) - 1
    for x in range(0, tamanho):
        for y in range(tamanho - 1, x - 1, -1): #comparação de dois valores para ordenar
            if arr[y] > arr[y+1]:
                varAux = arr[y]
                arr[y] = arr[y+1]
                arr[y+1] = varAux
    return arr

vetor = [0, -1, 3, 2, 1, 4]
print(BubbleSort(vetor))  


