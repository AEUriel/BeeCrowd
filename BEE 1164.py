n = int(input())

for i in range(n):
    y = int(input())
    suma = 0
    for j in range(1,y):
        if y%j == 0:
            suma += j
    if suma == y:
        print(f'{y} eh perfeito')
    else:
        print(f'{y} nao eh perfeito')