peso = float(input("Por favor, digite seu peso: "))
altura = float(input("Por favor, digite sua altura: "))
IMC = peso/(altura*altura)
print("Seu IMC é: ", IMC)
if IMC < 18.5:
    print("Abaixo do peso")
    pesoideal = (altura*altura) * 18.6
    pesoideal = pesoideal - peso
    print("Você precisa ganhar ", pesoideal, " quilos para alcançar o peso ideal.")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
    pesoideal = (altura*altura) * 25
    pesoideal = peso - pesoideal
    print("Você precisa perder ", pesoideal, " quilos para alcançar o peso ideal.")
elif IMC < 35:
    print("Obeso Leve")
    pesoideal = (altura*altura) * 25
    pesoideal = peso - pesoideal
    print("Você precisa perder ", pesoideal, " quilos para alcançar o peso ideal.")
elif IMC < 40:
    print("Obeso moderado")
    pesoideal = (altura*altura) * 25
    pesoideal = peso - pesoideal
    print("Você precisa perder ", pesoideal, " quilos para alcançar o peso ideal.")
elif IMC >= 40:
    print("Obeso mórbido")
    pesoideal = (altura*altura) * 25
    pesoideal = peso - pesoideal
    print("Você precisa perder ", pesoideal, " quilos para alcançar o peso ideal.")
