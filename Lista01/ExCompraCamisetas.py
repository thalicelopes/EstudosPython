QtdePeq = int(input("Por favor, insira a qtde de camisas pequenas da venda: "))
QtdeMedias = int(input("Por favor, insira a qtde de camisas médias da venda: "))
QtdeGrandes = int(input("Por favor, insira a qtde de camisas grandes da venda: "))
TotalCompra = 0.0
if(QtdePeq != 0):
    TotalCompra = TotalCompra + (QtdePeq*10)
if(QtdeMedias != 0):
    TotalCompra = TotalCompra + (QtdeMedias*12)
if(QtdeGrandes != 0):
    TotalCompra = TotalCompra + (QtdeGrandes*15)
print("O valor a ser pago é: ", TotalCompra)