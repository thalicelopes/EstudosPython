totalCompra = int(input("Por favor, insira o total de sanduíches a serem feitos: "))
QtdeQueijo = 0.0
QtdePresunto = 0.0
QtdeHamburguer = 0.0
for i in range(0, totalCompra):
    QtdeQueijo = QtdeQueijo + (0.05 * 2)
    QtdePresunto = QtdePresunto + (0.05 * 2)
    QtdeHamburguer = QtdeHamburguer + 0.10
print("É necessário comprar ", QtdeQueijo, " Kilos de queijo\n, ", QtdePresunto, "Kilos de presunto\n e ", QtdeHamburguer, " Kilos de hambúrguer.")
    
    

    
