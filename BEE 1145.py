x, y = map(int, input().split())
cont = 0
if 1<x<20 and x<y<100000:
    for i in range(1,y+1):
        cont += 1
        if (cont == x):
            print(i)
            cont = 0
        else:
            print(i, end=" ")

###Parametro end concatena con su valor
###Por defecto salto de linea
###Si no usa la misma linea de impresion