juegos = 0
inter = 0
gremio = 0
empates = 0
while True:
    x, y = map(int, input().split())
    if x > y:
        inter += 1
        juegos += 1
    elif y > x:
        gremio += 1
        juegos += 1
    else:
        empates += 1
        juegos += 1
    while True:
        print('Novo grenal (1-sim 2-nao)')
        z = int(input())
        if z == 1 or z == 2:
            break
    if z == 2:
        print(f'{juegos} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empates}')
        if inter > gremio:
            print('Inter venceu mais')
        elif gremio > inter:
            print('Gremio venceu mais')
        else:
            print('Não houve vencedor')
        break