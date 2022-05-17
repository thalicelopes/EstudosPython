# Árvore binária em que cada nó tem filhos de menor valor

def HeapSort(arr):
    tamanhoVetor = len(arr)
    for cont in range(tamanhoVetor // 2 - 1, -1, -1):
        HeapGen(arr, tamanhoVetor, cont)
    for cont in range(tamanhoVetor - 1, 0, -1):
        arr[cont], arr[0] = arr[0], arr[cont] 
        HeapGen(arr, cont, 0)

def HeapGen(arr, tamanhoVetor, indice):
    raiz = indice
    esquerda = 2 * indice + 1  
    direita = 2 * indice + 2  
    if esquerda < tamanhoVetor and arr[indice] < arr[esquerda]:
        raiz = esquerda
    if direita < tamanhoVetor and arr[raiz] < arr[direita]:
        raiz = direita
    if raiz != indice:
        arr[indice], arr[raiz] = arr[raiz], arr[indice] 
        HeapGen(arr, tamanhoVetor, raiz)

x = [10, 4, 6, 2, 11, 23, 3]
HeapSort(x)
print("Fim do algoritmo -", x)
