x = 1
y = 1
res = 0
while y < 39:
    res += y/x
    x += x
    y += 2
print(f'{res:.2f}')