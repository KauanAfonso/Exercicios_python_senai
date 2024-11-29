def menu():
    print(F"Escolha sua opção:\n1-Soma\n2-Subtracao\n3-Mutilplicacao\n4-Divisao\n0-Sair")
    escolha = int(input("Digite aqui: "))
    return escolha

def soma(num1,num2):
    return num1 + num2
def subtracao(num1,num2):
    return num1 - num2
def divsao(num1,num2):
    if num2 !=0:
        return num1 / num2
    else:
        print('NÃO PODE DIVIDIR POR ZERO !')
def multiplicacao(num1,num2):
    return num1 * num2

def pedir_numeros():
    n1 = float(input("digite um número"))
    n2 = float(input("digite um número"))
    return n1,n2
def caulculdora():
    while True:
        opcao = menu()
        if opcao == 1:
            n1,n2 = pedir_numeros()
            resultado = soma(n1,n2)
            print(f"o resultado da soma é de {resultado}")
        elif opcao == 2:
            n1,n2 = pedir_numeros()
            resultado = subtracao(n1,n2)
            print(f"o resultado da subtração é de {resultado}")
        elif opcao == 3:
            n1,n2 = pedir_numeros()
            resultado = divsao(n1,n2)
            print(f"o resultado da divisao é de {resultado}")
        elif opcao == 4:
            n1,n2 = pedir_numeros()
            resultado = multiplicacao(n1,n2)
            print(f"o resultado da multiplicacao é de {resultado}")
        elif opcao == 0:
            print("Você saiu...")
            break
        else:
            print("Número inválido")

caulculdora()