n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print("A distância entre os dois números é ", n1 - n2, ".", sep='')
elif n2 > n1:
    print("A distância entre os dois números é ", n2 - n1, ".", sep='')
else:
    print("Os dois números são iguais.")
