x = 2
y = 10

for i in range(4):
    while y > 3:
        if x % 2 == 0:
            y-=4
        else:
            y-=3
        x+=1
    y =10
print(x,y)