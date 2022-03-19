peso = float(input("Por favor, digite seu peso: "))
altura = float(input("Por favor, digite sua altura: "))
print("Seu IMC é: ", peso/(altura*altura))
if peso/(altura*altura) < 18.5:
    print("Abaixo do peso")
elif peso/(altura*altura) < 25:
    print("Peso normal")
elif peso/(altura*altura) < 30:
    print("Sobrepeso")
elif peso/(altura*altura) < 35:
    print("Obeso Leve")
elif peso/(altura*altura) < 40:
    print("Obeso moderado")
elif peso/(altura*altura) >= 40:
    print("Obeso mórbido")