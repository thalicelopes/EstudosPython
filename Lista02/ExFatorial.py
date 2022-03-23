from unittest import result


qtde = int(input("Por favor, informe um número inteiro para checar o fatorial: "))
resultado = 1
print("O fatorial de ", qtde, ":")
while qtde != 0:
    resultado = resultado * qtde 
    qtde = qtde - 1
print(resultado)
