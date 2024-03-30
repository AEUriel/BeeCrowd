# m = 0
# o = input()
# for i in range(12):
#     m.append([])
#     for j in range(12):
#         x = float(input())
#         m[i].append(x)

res = 0
cont = 0
filas = 12
for i in range(1,12):
    for j in range(1, filas):
        print(f'[{12-i}][{12- j}]')
    filas -= 1
    