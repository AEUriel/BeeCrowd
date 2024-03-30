m = []
o = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)
cont = 0
res = 0
filas = 12
columnas = 12
for i in range(filas):
    for j in range(1, columnas):
        
        res = m[i][12-j]
        cont += 1
    columnas -= 1
if o == 'S':
    print(f'{res:.1f}')
else:
    print(f'{res/cont:.1f}')