n = int(input())
x = list()
a = 0

for i in range(1000):
    x.append(a)
    if x[i] >= n:
        x[i] = 0
        a = 0
    a += 1
    print(f'N[{i}] = {x[i]}')
        