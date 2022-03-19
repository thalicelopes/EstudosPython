x = []
cont = 0
num = 0
y = []
while cont<3:
    num = int(input("Digite um número: "))
    x.append(num)
    cont = cont + 1
while cont>0:
    cont = cont - 1
    y.append(x[cont])
while cont<3:
    print("Lista 1: ", x[cont])
    print("Lista 2: ", y[cont])
    cont = cont + 1
