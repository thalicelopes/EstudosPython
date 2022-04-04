QtdeDias = int(input("Por favor, insira a de dias sem acidente:  "))
Ano = 0
Meses = 0
Ano = QtdeDias // 365
QtdeDias = QtdeDias - (Ano * 365)
Meses = QtdeDias // 30
QtdeDias = QtdeDias - (Meses * 30)
print("Estamos a ", Ano, " anos, ", Meses, " meses e ", QtdeDias, " dias sem acidente.")
    
