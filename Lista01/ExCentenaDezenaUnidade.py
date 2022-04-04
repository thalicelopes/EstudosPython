Numero = int(input("Por favor, insira um número entre 1 e 999: "))
if (Numero > 999 or Numero < 0):
    print("Número inválido!")
else:
    Centena = Numero // 100
    Numero = Numero - (Centena * 100)
    Dezena = Numero // 10
    Numero = Numero - (Dezena * 10)
    print("CENTENA: " ,Centena, "\nDEZENA: ", Dezena,"\nUNIDADE: ", Numero)
    
