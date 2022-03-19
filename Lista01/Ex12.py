salario = float(input("Por favor, digite seu salário atual: "))
if salario == 0 or salario < 0:
    print("Seu salário é nulo.")
else:
    print("Salário Atual: ", salario)
    print("Salário com aumento: ", salario + (salario * 15/100))
    print("Salário final: ", salario + (salario * 15/100) - (salario * 8/100))
