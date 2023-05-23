#Define o valor da variável opcao, como um número inteiro digitado pelo usuário
opcao = int(input("Escolha uma opção: \n1 - Banana \n2 - Maçã \n3 - Abacaxi \n4 - Laranja \n"))

#Realiza um comando de acordo com o valor de opcao
match(opcao):
    case 1:
       print("Banana escolhida.")
    case 2:
        print("Maçã escolhida.")
    case 3:
        print("Abacaxi escolhido.")
    case 4:
        print("Laranja escolhida")