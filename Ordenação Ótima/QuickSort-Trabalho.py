# Divisão de vetor, escolha de um pivô para comparação

from random import randint, random
import time
def divisaoVetor(vetor, inicioVetor, fimVetor):
    i = inicioVetor
    pivo = vetor[fimVetor]
    for x in range(inicioVetor, fimVetor):
        if vetor[x] <= pivo:
            vetor[i], vetor[x] = vetor[x], vetor[i]
            i += 1
    vetor[i], vetor[fimVetor] = vetor[fimVetor] ,vetor[i]
    return i

def quickSort(vetor, inicioVetor, fimVetor):
    if inicioVetor < fimVetor:
        centroVetor = divisaoVetor(vetor, inicioVetor, fimVetor)
        quickSort(vetor, inicioVetor, centroVetor - 1)
        quickSort(vetor, centroVetor + 1, fimVetor)
vetor = []

for i in range(0, 100):
    vetor.append(randint(0, 100))
print(vetor)
inicio = time.time() #CALCULO DE TEMPO PARA COMPLETAR TABELA
quickSort(vetor, 0, len(vetor) - 1)
fim = time.time() #CALCULO DE TEMPO PARA COMPLETAR TABELA
print(vetor)
print("Tempo de execução: ")
print(fim-inicio)