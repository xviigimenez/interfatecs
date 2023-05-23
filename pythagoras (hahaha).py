# a² + b² = c²

import math

def a(b, c):
  return math.sqrt(c) - math.sqrt(b)

val = []

val.append(input("Digite o valor de 'b': "))
val.append(input("Digite o valor de 'c': "))

val.insert(a(val[0], val[1]))