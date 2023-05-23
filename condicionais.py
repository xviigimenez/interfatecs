#Utilizando condicionais
salario = float(input("Digite o seu salário: "))
novoSalario = 0.0

if(salario < 2000):
    novoSalario = (110.00 * salario)
    print("Seu novo salário é :", novoSalario)
else:
    print("Não há aumentos disponíveis.")