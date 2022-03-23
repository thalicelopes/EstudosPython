print("Resultado da série 1 / 11 + 1 + 2 / 22 + 1 ...")
qtde = float(input("Por favor, informe a quantidade de vezes que a série será repetida."))
numero = 0
resultado = 0 
while qtde != numero:
    numero = numero + 1
    resultado = resultado + (numero / (numero * 11) + 1)
print("O resultado do algoritmo é: ", resultado)