suma = 0
y = 0
while True:
    x = float(input())
    if x < 0 or x > 10:
        print('nota invalida')
    else:
        suma += x
        y += 1
    if y == 2:
        print(f'media = {suma/2:.2f}')
        while True:
            suma = 0
            y = 0
            z = 0
            z = int(input('novo calculo (1-sim 2-nao)\n'))
            if z == 1 or z ==2:
                break
        if z == 2:
            break