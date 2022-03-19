nome1 = input("Por favor, digite o nome do primeiro candidato: ")
nome2 = input("Por favor, digite o nome do segundo candidato: ")
nome3 = input("Por favor, digite o nome do terceiro candidato: ")
voto = 1
candidato1 = 0
candidato2 = 0
candidato3 = 0
print("Digite 1 para votar em ",nome1," digite 2 para votar em ",nome2," e digite 3 para votar em ",nome3, ".0 TERMINA a eleição. Outros números não serão contabilizados. ")
while voto != 0:
    voto = int(input("Seu voto: "))
    if voto == 1: candidato1+=1
    elif voto == 2: candidato2+=1
    elif voto == 3: candidato3+=1
print("O candidato ", nome1, " possui ", candidato1, " votos. O candidato", nome2, " possui ", candidato2, " votos. O candidato", nome3, " possui ", candidato3, " votos.")
if candidato3==candidato2 and candidato3==candidato1 and candidato1==candidato2: print("EMPATE ENTRE OS TRÊS CANDIDATOS. ")
elif candidato2==candidato1: print("Empate entre", nome1, " e ", nome2, ".")
elif candidato2==candidato3: print("Empate entre", nome2, " e ", nome3, ".")
elif candidato3==candidato1: print("Empate entre", nome1, " e ", nome3, ".")
elif candidato1>candidato2 and candidato1>candidato3: print("Sendo assim, o candidato(a) ", nome1, " é o vencedor.")
elif candidato2>candidato1 and candidato2>candidato3: print("Sendo assim, o candidato(a) ", nome2, " é o vencedor.")
else: print("Sendo assim, o candidato(a)", nome3, " é o vencedor.")