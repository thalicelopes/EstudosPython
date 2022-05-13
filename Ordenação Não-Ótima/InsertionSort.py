# Considere um vetor de duas partes: uma ordenada e uma desordenada

def InsertionSort(arr):
    tamanho = len(arr)
    for x in range(0, tamanho):
        varAux = arr[x]
        indice = x - 1
        while indice>=0 and varAux < arr[indice]: #Inserção do maior valor para ordená-lo corretamente
            arr[indice + 1] =  arr[indice]
            indice-=1
        arr[indice+1] = varAux
    return arr

vetor = [0, -1, 3, 2, 1, 4]
print(InsertionSort(vetor))