distancia = float(input("Por favor, informe a distância: "))
litros = float(input("Por favor, informe quantos litros foram gastos: "))
print("Foram percorridos", (distancia/litros), "Km/L.")
if((distancia/litros)>15):
    print("Não é econômico.")
else:
    print("econômico! :D")
