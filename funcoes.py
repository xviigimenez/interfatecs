#Função padrão
def soma(num_01, num_02):
    soma = num_01 + num_02
    return soma
print(soma(1,2))

#Variável como função lambda
somaLambda = lambda num_01, num_02 : num_01 + num_02
print(somaLambda(1,2))