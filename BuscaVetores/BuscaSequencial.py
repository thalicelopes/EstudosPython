# Função recebe a lista/vetor, e um valor a ser procurado no vetor.

def BuscaSequencial(arr, valor):
    tamanho = len(arr)
    for x in range(0, tamanho):
        if(arr[x] == valor):
            return x
    return None

v = [1, 2, 3, 4, 6] #Melhor caso: Buscar o número 1, o primeiro da lista. Pior caso: buscar um valor fora do vetor.
valor = 1
valor2 = 7
print("Posição que o número se encontra na lista: ", BuscaSequencial(v, valor))
print(BuscaSequencial(v, valor2))