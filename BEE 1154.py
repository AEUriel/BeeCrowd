cont = 0
aux = 0
while True:
    edad = int(input())
    if edad < 0:
        break
    else:
        cont += 1
        aux += edad
print(f'{aux/cont:.2f}')