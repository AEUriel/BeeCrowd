while True:
    try:
        x = int(input())
        array = [[3] * x for _ in range (x)]
        for i in range(x):
            for j in range(x-i):
                pass
            array[i][i] = 1
            array[i][j] = 2
        for fila in array:
            for num in fila:
                print(f'{num}', end='')
            print()
    except EOFError:
        break
