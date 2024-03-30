x = int(input())
z = int(input())
while(z <= x):
    z = int(input())
suma = 0
cont = 1
for i in range(x,z):
    suma += i
    if suma < z:
        cont += 1    
print(cont)
