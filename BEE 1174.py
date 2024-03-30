a = [0] * 100
for i in range(100):
    x = float(input())
    a[i] = x
    if a[i] <= 10:
        print(f'A[{i}] = {a[i]:.1f}')