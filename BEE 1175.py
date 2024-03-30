n = [0] * 20
for i in range(20):
    y = int(input())
    n[i] = y
n.reverse()
for i in range(20):
    print(f'N[{i}] = {n[i]}')