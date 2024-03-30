a,b,c,d = map(int,input().split())
if a>=c and b>=d:
    horas = (c+24)-a
else:
    horas = c-a
if b>d:
    minutos = (d+60)-b
    horas -= 1
    if minutos >= 60:
        minutos -= 60
else:
    minutos = (d-b)
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')