x = float(input())
n = [x]

for i in range(100):
    x = x/2
    n.append(x)
    print(f'N[{i}] = {n[i]:.4f}')
