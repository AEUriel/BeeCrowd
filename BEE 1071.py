x = int(input())
y = int(input())
inicio = min(x,y)+1
end = max(x,y)
if inicio %2 == 0:
    inicio += 1
cont = 0
for i in range(inicio, end, 2):
    cont += i
print(cont)