n = 10
for n2 in range(2, n+1):
    p = True
    for i in range(2, n2):
        if n2 % i == 0:
            p = False
            break
    if p:
        print(n2)
        
        