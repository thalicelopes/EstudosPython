# Vetor em ordem crescente; Buscar em metade do espaço de busca;

def BuscaBinaria(arr, valor):
    indice = 0 
    fim = len(arr) - 1 
    while indice <= fim:
        centroVetor = (indice + fim)//2
        if valor == arr[centroVetor]: #Se o valor for igual ao centro do vetor, logo será retornado.
            return centroVetor
        elif valor < arr[centroVetor]: #Visto que para ocorrer uma busca binária o vetor precisa estar EM ORDEM,
            #Se o valor for menor que o centro, significa que ele está da metade do vetor para o início
            fim = centroVetor - 1
        else:
            #Se o valor for maior que o centro, significa que ele está da metade do vetor para o fim
            indice = centroVetor + 1
    return None

#Testando a função:
vetor = [1,2,3,4,5,6,7]
print("Posição que o número se encontra na lista: ", BuscaBinaria(vetor, 4))
print(BuscaBinaria(vetor, 10))