qtdePaes = int(input("Por favor, informe a quantidade de Pães vendidos: "))
qtdeBroas =  int(input("Por favor, informe a quantidade de Broas vendidas: "))
print("Você arrecadou um total de: " , ((qtdePaes*0.12)+(qtdeBroas*1.50)))
print("Total em dinheiro de Pães vendidos: " , (qtdePaes*0.12))
print("Total em dinheiro Broas vendidas: " , (qtdeBroas*1.50))
print("Para sua poupança, você deve guardar 10% do valor, que equivale a: " , ((qtdePaes*0.12)+(qtdeBroas*1.50))*0.1)