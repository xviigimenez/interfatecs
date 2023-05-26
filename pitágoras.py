# a² + b² = c²

import math

val = []
x = str(input("Qual valor você deseja calcular? "))

match x:
    case 'a':
        val.append(float(input("Digite o valor de 'b': ")))
        val.append(float(input("Digite o valor de 'c': ")))
        val.insert(0, math.sqrt(val[1]) - math.sqrt(val[0]))
    case 'b':
        val.append(input("Digite o valor de 'a': "))
        val.append(input("Digite o valor de 'c': "))
    case 'c':
        val.append(input("Digite o valor de 'a': "))
        val.append(input("Digite o valor de 'b': "))
    case _:
        print("Escolha entre 'a', 'b' ou 'c'.")

print(val[0])
