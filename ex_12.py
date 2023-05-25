import random

num_01 = float(random.randrange(1, 100))
num_02 = float(random.randrange(1, 100))

print("Primeiro número:", num_01, "\nSegundo número: ", num_02)

soma = lambda val_01, val_02 : val_01 + val_02
def media(val_01, val_02):
    resultado = (val_01 + val_02)/2
    return resultado

print("Soma:", soma(num_01,num_02), "\nMédia: ", media(num_01, num_02))
