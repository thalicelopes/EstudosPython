# Divisão recursiva dos elementos n por 2, ordenar na volta da recursão, intercalando.

def mergeSort(arr, inicio, fim):
    if(fim - inicio > 1):
        meio = (inicio + fim) // 2
        mergeSort(arr, inicio, meio)
        mergeSort(arr, meio, fim)
        intercalaVetor(arr, inicio, meio, fim)

def intercalaVetor(arr, inicio, meio, fim):
    vetor1 = arr[inicio:meio]
    vetor2 =  arr[meio:fim]
    print(vetor1, vetor2)
    vetorFinal = []
    for varAuvetor1 in range(0, len(vetor1)+len(vetor2)):
        vetorFinal.append(0)
    tamanhoVetorFinal = 0
    tamanhoVetor1 = 0
    tamanhoVetor2 = 0 
    while tamanhoVetorFinal < len(vetorFinal):
        if tamanhoVetor1 >= len(vetor1): # vetor1 já foi totalmente verificado
            vetorFinal[tamanhoVetorFinal] = vetor2[tamanhoVetor2]
            tamanhoVetor2 = tamanhoVetor2 + 1
            tamanhoVetorFinal = tamanhoVetorFinal + 1
            continue
        if tamanhoVetor2 >= len(vetor2): # vetor2 já foi totalmente verificado
            vetorFinal[tamanhoVetorFinal] = vetor1[tamanhoVetor1]
            tamanhoVetor1 = tamanhoVetor1 + 1
            tamanhoVetorFinal = tamanhoVetorFinal + 1
            continue
        if vetor1[tamanhoVetor1] < vetor2[tamanhoVetor2]:
            vetorFinal[tamanhoVetorFinal] = vetor1[tamanhoVetor1]
            tamanhoVetor1 = tamanhoVetor1 + 1
        else:
            vetorFinal[tamanhoVetorFinal] = vetor2[tamanhoVetor2]
            tamanhoVetor2 = tamanhoVetor2 + 1
        tamanhoVetorFinal = tamanhoVetorFinal + 1
    tamanhoVetorFinal = 0
    for i in range(inicio, fim):
        arr[i] = vetorFinal[tamanhoVetorFinal]
        tamanhoVetorFinal = tamanhoVetorFinal + 1

vetor = [0, 1, 2, 3, 4, 6, 2, 3, 2, 1]
mergeSort(vetor, 0, len(vetor))
print(vetor)

