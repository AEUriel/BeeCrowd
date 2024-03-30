par = list()
impar = list()
cont = 0
while cont < 15:
    x = int(input())
    if x %2 == 0:
        par.append(x)
    else:
        impar.append(x)
    if len(par) == 5:
        for i in range(5):
            print(f'par[{i}] = {par[i]}')
        par.clear()
    if len(impar) == 5:
        for i in range(5):
            print(f'impar[{i}] = {impar[i]}')
        impar.clear()
    cont += 1
for i in range(len(impar)):
    print(f'impar[{i}] = {impar[i]}')
for i in range(len(par)):
    print(f'par[{i}] = {par[i]}')
