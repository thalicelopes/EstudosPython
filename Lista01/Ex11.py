TempDia = float(input("Por favor, insira a temperatura da manhã: "))
TempTarde = float(input("Por favor, insira a temperatura da tarde: "))
TempNoite = float(input("Por favor, insira a temperatura da noite: "))
TempAlta = 0.0
TempBaixa = 0.0
if TempDia>TempNoite and TempDia>TempTarde:
    TempAlta = TempDia
    if(TempNoite<TempTarde): TempBaixa = TempNoite
    else: TempBaixa = TempTarde
elif TempTarde>TempNoite and TempTarde>TempDia:
    TempAlta = TempTarde
    if(TempNoite<TempDia): TempBaixa = TempNoite
    else: TempBaixa = TempDia
elif TempNoite>TempTarde and TempNoite>TempDia:
    TempAlta = TempNoite
    if(TempTarde<TempDia): TempBaixa = TempTarde
    else: TempBaixa = TempDia
print("A temperatura mais baixa é: ", TempBaixa, " a mais alta é: ", TempAlta)