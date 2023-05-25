# Utilizando condicionais
salario = float(input("Digite o seu salário: "))

if(salario < 2000):
    salario = (1.10 * salario)
    print("Seu novo salário é :", round(salario, 2))
else:
    print("Não há aumentos disponíveis.")
