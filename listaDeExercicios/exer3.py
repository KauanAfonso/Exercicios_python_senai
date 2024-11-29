num = int(input("Digite um número: "))
i = 1
numIteravel = num

while i <= num:
    numIteravel-=1
    if numIteravel < 0:
        break
    print(numIteravel)
    i+=1