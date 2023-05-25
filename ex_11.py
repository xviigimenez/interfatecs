import math

print("Descobrindo o valor da área de uma circunferência: ")
raio = float(input("Digite o valor do raio: "))

def area_circunf(rai):
    area = (math.pi * math.pow(rai,2))
    return area

resultado = area_circunf(raio)

print("A Área da circunferência é:", resultado)