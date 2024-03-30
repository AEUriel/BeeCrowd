while True:
    x = int(input())
    y = 0
    suma = 0
    if x == 0:
        break
    elif x%2 != 0:
        x += 1
    while y < 5:
        y += 1
        suma += x
        x += 2
    print(suma)
            