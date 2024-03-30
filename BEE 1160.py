t = int(input())
for i in range(t):
    pa, pb, g1, g2 = map(float, input().split())
    a1, a2 , cont = 0, 0, 0
    
    while int(pa) <= int(pb):
        a1 = pa * (g1/100) 
        a2 = pb * (g2/100
        )
        pa += int(a1)
        pb += int(a2)
        cont += 1
        if cont > 100:
            break
    if cont <= 100:
        print(f'{cont} anos.')
    else:
        print('Mais de 1 seculo.')