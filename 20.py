import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

x1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)

print("Os possíveis resultados são ", x1, " e ", x2, ".", sep='')
