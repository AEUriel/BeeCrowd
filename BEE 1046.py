a,b = map(int,input().split())
if a>=b:
    tiempo = (b+24)-a
else:
    tiempo = b-a
print(f'O JOGO DUROU {tiempo} HORA(S)')