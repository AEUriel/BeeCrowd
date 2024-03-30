while True:
    x,y = map(int, input().split())
    suma = 0
    cadena = ''
    if x <= 0 or y <=0:
        break
    if x>y:
        z = x
        x = y
        y = z
    for i in range(x,y+1):
        suma += x
        x += 1
        cadena += str(i) + ' '
    print(f'{cadena}Sum={suma}')