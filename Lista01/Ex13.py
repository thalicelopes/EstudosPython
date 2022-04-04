Lado1 = int(input("Insira o lado 1: "))
Lado2 = int(input("Insira o lado 2: "))
Lado3 = int(input("Insira o lado 3: "))
if Lado1 > (Lado2 + Lado3) or Lado2 > (Lado1 + Lado3) or Lado3 > (Lado2 + Lado1):
    print("Com os dados informados, não é possível formar um triângulo. ")
elif Lado1 == Lado2 and Lado1 == Lado3 and Lado2 == Lado3:
    print("Triângulo Equilátero! ")
elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
    print("Triângulo Isósceles! ")
else:
    print("Triângulo Escaleno! ")