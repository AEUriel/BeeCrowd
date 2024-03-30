n = [0, 1]
for i in range(59):
    y = n[i] + n[i+1]
    n.append(y)
x = int(input())
for i in range(x):
    z = int(input())
    if z < 0 or z > 60:
        pass
    else:
        print(f'Fib({z}) = {n[z]}')