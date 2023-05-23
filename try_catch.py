#Executa o bloco de código 
try:
    numero = int(input("Digite um número entre 1 e 10\n"))
    if (numero >= 1 and numero <= 10):
        print("Realmente, é um número entre 1 e 10...")
    else:
        #Se o usuário digitar um número inválido, uma excessão será lançada
        raise Exception ("bruh")
#Exceção - se o usuário digitar algo que não for um número inteiro, um erro será lançado
except ValueError:
    print('ERRO: uma exceção foi lançada.')