dias=float(input("Quantos dias alugados? "))
km=float(input("Quantos Km rodados? "))
resultado=60*dias+0.15*km
print("O total a pagar é de R${:.2f}".format(resultado))