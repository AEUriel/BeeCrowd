l = int(input())
t = input()
m = []
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

res = 0
for i in range(12):
    res += m[l][i]
if t == 'S':
    print(res)
else:
    print(res/12)