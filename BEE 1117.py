y = 0
suma = 0
while y < 2:
    x = float(input())
    if x < 0 or x > 10:
        print('nota invalida')
    else:
        suma += x
        y += 1
print(f'media = {suma/2:.2f}')