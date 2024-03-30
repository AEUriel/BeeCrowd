n = int(input())
for i in range(n):
    suma = 0
    x, y= map(int,input().split())
    if x == y :
        print('0')
    else:
        z = 0
        if x>y:
            z = x
            x = y
            y = z
        while x < (y - 1):
            x += 1
            if x%2 != 0:
                suma+=x
        print(suma)

        

    

