#### Presentation Error :( ###

while True:
    x = int(input())
    if x == 0:
        break
    matrix = [[0]*x for _ in range(x)]
    z = 1
    for i in range(x):
        for j in range(x):
            matrix[i][j] = 2 ** (i + j)
                 
    x = max(max(matrix))
    x = len(str(x))
    
    for filas in matrix:
        for num  in filas:
            print(f'{num:{x}d}', end=' ')
        print()