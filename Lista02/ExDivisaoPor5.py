#No intervalo de 1000 a 1999, quais números dividos por 11 tem resto 5?

Contador = 1000

while Contador < 2000:
    if(Contador%11 == 5): 
        print(Contador)
    Contador = Contador + 1