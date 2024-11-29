# numero = int(input('digite um número: '))
# numeroanterior = numero - 1

# for i in range (0, 101):
#     proximoNum = numero + numeroanterior
#     print(proximoNum)
#     numeroanterior = numero
#     numero = proximoNum
     
     
def fibonnaci():
    
    #1 1 3 5 7 13 
    numero1 = 1
    numero2 = 1
    num_escolhido = int(input("digite um número"))
    for i in range (num_escolhido - 2):
        kauan =  numero1
        numero1 = numero2
        numero2 = kauan + numero2
    return numero2


print(fibonnaci())