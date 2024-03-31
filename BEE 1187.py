m = []
o = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

res = 0
cont = 0
aux = 1
limite = 11
for i in range(5):
    for j in range(aux,limite):
        res += m[i][j]
        cont += 1
    aux += 1
    limite -= 1

if o == 'S':
    print(f'{res:.1f}')
else:
    print(f'{res/cont:.1f}')