n = int(input())
y = []
for l in range(n):
    x = input()
    y.append(x)

for i in range(n):
    convertido = int(y[i])
    if convertido > 0 and convertido%2 == 0:
        print('EVEN POSITIVE')
    elif convertido > 0 and convertido%2 != 0:
        print('ODD POSITIVE')
    elif convertido < 0 and convertido%2 == 0:
        print('EVEN NEGATIVE')
    elif convertido < 0 and convertido%2 != 0:
        print('ODD NEGATIVE')
    else:
        print('NULL')