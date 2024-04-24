while True:
    n = int(input())
    if n == 0:
        break
    
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matriz[i][j] = min(i,j, n-1-i, n-1-j) + 1
        
    for fila in matriz:
        for num in fila:
            print(f'{num:3d}', end='')
        print()
    print()

