# import math

# num = int(input('Digite um número: '))
# num2 = int(input('Digite um número: '))
# result = math.lcm(num,num2) #função para descobrir o MMMC

# print(result)

def mmc():
    
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite um número: '))
    if numero_1 > numero_2:
        mmc = numero_1
        mario = numero_1
    else:
        mmc = numero_2 
        mario = numero_2
    while(mmc % numero_1 != 0) or (mmc % numero_2 != 0):
        mmc += mario 
    return mmc
 

print(mmc())
        