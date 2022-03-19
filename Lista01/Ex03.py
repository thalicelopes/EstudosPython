x  = float(input("Por favor, insira o valor do ingresso: "))
dia = int(input("Por favor, insira um número de 1 a 7: "))
idade = int(input("Por favor, insira a idade do espectador: "))
PrecoIngresso = 0.0
if(dia == 3):
    PrecoIngresso = x * (5/10)
if(idade < 14):
    PrecoIngresso = PrecoIngresso * (5/10)
print("O preço do ingresso é: R$", PrecoIngresso)
