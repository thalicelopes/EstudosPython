saldoinicial = float(input("Digite seu saldo inicial: "))
debito = float(input("Digite os débitos do mês: "))
credito = float(input("Digite os créditos do mês: "))
if saldoinicial - debito + credito > 0:
    print("R$ Saldo Positivo em: ", saldoinicial - debito + credito)
else:
    print("R$ Saldo Negativo em: ", saldoinicial - debito + credito)
