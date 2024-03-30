n = int(input())

for i in range(n):
    a,b,c = map(float, input().split())
    cali = ((a*2)+(b*3)+(c*5))/10
    print(f'{cali:.1f}')