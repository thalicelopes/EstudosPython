Dia = int(input("Por favor, informe o dia de hoje: "))
Mes = int(input("Por favor, informe o mês atual: "))
if Mes > 12 or Mes < 0 or Dia < 0 or Dia > 30:
    print("Data inválida! ")
else:
    qtdeDias = 30 - Dia
    qtdeDiasMeses = (30 * Mes) - qtdeDias
    print("Já se passaram: ", qtdeDiasMeses, " dias.")