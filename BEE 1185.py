m = []
o = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

res = 0
cont = 0
filas = 11

for i in range(11):
    for j in range(filas):
        cont += 1
        res += m[i][j]
    filas -= 1

if o == 'S':
    print(f'{res:.1f}')
else:
    print(f'{res/cont:.1f}')