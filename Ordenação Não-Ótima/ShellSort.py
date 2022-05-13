# Tenta reduzir o número de trocas do Insertion Sort

def ShellSort(arr):
    varAux = 1
    tamanho = len(arr)
    while varAux < tamanho:
        varAux = varAux * 3 + 1
    while varAux > 1:
        varAux = varAux // 3 
        for x in range(varAux, tamanho, varAux):
            current = arr[x]
            y = x - varAux
            while y >= 0 and current < arr[y]: 
                arr[y+varAux] = arr[y]
                y = y - varAux
            arr[y+varAux] = current
    return arr

vetor = [0, -1, 3, 2, 1, 4]
print(ShellSort(vetor))