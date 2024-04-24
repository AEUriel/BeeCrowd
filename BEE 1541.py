while True:
    x = input()
    if x == '0':
        break
    a, b, c = map(int, x.split())
    area_casa = a*b
    area_terreno = (area_casa*100) / c
    res = area_terreno**0.5
    print(f'{res:.0f}')