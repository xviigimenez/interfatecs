# Executa o bloco de código
try:
    numero = int(input("Digite um número entre 1 e 10: "))
    if (numero >= 1 and numero <= 10):
        print("Realmente, é um número entre 1 e 10...")
    else:
        # Se o usuário digitar um número inválido, uma excessão será lançada
        raise ValueError("Digite um valor válido.")
        # print("Digite um valor válido.")
# Exceção - se o usuário digitar algo que não for um número inteiro, um erro será lançado
except TypeError:
    print('Erro: uma exceção foi lançada.')
