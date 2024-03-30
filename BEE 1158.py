n = int(input())
for i in range(n):
    x,y= map(int, input().split())
    res = 0
    if x %2 == 0:
        x += 1
    j = 0
    while j < y:
        if x %2 != 0:
            res += x
            j += 1
        x += 1
    print(res)