x = []
cont = 0
num = 0
y = []
while cont<3:
    num = int(input("Digite um número: "))
    x.append(num)
    cont = cont + 1
num = 0
while cont>0:
    cont = cont - 1
    print("Valor lista ordenada: ", x[num], "| Valor lista desordenada: ", x[cont])
    num = num + 1
