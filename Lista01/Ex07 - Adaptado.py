Nota1 = float(input("Digite a primeira nota do aluno:"))
Nota2 = float(input("Digite a segunda nota do aluno:"))
print("Média: ", (Nota1+Nota2)/2)
if (Nota1+Nota2)/2 < 3:
    print("REPROVADO")
elif (Nota1+Nota2)/2 <= 6.9:
    print("FINAL")
elif (Nota1+Nota2)/2 <= 9.5:
    print("APROVADO")
else:
    print("APROVADO COM LOUVOR")
