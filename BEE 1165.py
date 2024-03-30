n = int(input())
for i in range(n):
    y = int(input())
    suma = 0
    for j in range(1,y+1):
        if y%j == 0:
            suma += 1
    if suma > 2:
        print(f'{y} nao eh primo')
    else:
        print(f'{y} eh primo')