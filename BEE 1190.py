m = []
o = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

res = 0
cont = 0
inicio = 12
fin = 12
for i in range(1, 11):
    if i > 6:
        inicio += 1
    elif i < 6:
        inicio -= 1
    for j in range(inicio, fin):
        res += m[i][j]
        cont += 1

if o == 'S':
    print(f'{res:.1f}')
else:
    print(f'{res/cont:.1f}')