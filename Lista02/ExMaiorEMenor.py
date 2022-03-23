#Números primos entre 1 e 1000:
from re import M


i = 0
cont = 1
qtde = 0
media = 0
while i < 5:
    numero = int(input("Por favor, informe um número inteiro positivo: "))
    media = media + numero
    if i == 0:
        MaiorNumero = numero
        MenorNumero = numero
        
    else:
        if (numero > MaiorNumero):
            MaiorNumero = numero
        if (numero < MenorNumero):
            MenorNumero = numero
    i = i + 1
print("O maior número é: ", MaiorNumero)
print("O menor número é: ", MenorNumero)
print("A média dos números é: ", media/(i+1))