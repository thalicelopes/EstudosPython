#Selection Sort

def SelectionSort(arr):
    tamanho = len(arr)
    for x in range(0, tamanho-1):
        for y in range(x+1, tamanho): #Seleção do maior valor para ordená-lo corretamente
            if arr[x] > arr[y]:
                varAux = arr[x]
                arr[x] = arr[y]
                arr[y] = varAux
    return arr

vetor = [0, -1, 3, 2, 1, 4]
print(SelectionSort(vetor))  