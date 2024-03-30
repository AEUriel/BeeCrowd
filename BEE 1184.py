m = []
o = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = int(input)
        m[i].append(x)

cont = 0
res = 0
filas = 11
for i in range(11):
    for j in range(filas):
        # print(f'[{11-i}][{j}]')
        res += m[11-i][j]
        cont += 1
    filas -= 1
if o == 'S':
    print(f'{res:.1f}')
else:
    print(f'{res/cont:.1f}')