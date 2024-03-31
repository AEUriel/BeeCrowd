m = []
o = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)
res = 0
cont = 0
aux = 5
limite = 1
for i in range(1, 12):
    for j in range(limite):
        res += m[i][j]
        cont += 1 
        # print(f'[{i}][{j}]')
    if i < 5:
        limite += 1
    elif i > 5:
        limite -= 1
if o == 'S':
    print(f'{res:.1f}')
else:
    print(f'{res/cont:.1f}')