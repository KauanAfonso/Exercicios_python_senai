# import math

# num = int(input('Digite um número: '))
# num2 = int(input('Digite um número: '))
# result = math.gcd(num,num2)#função para descobrir o MDC

# print(result)


def mdc():
    
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite um número: '))
    
    mdc = numero_1
    
    while (numero_1 % mdc != 0) or (numero_2 % mdc != 0):
        mdc = mdc - 1
    return mdc

print(mdc())
        
        
