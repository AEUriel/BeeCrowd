n = int(input())
x = input().split()
l = [int(num) for num in x]
index = 0
minimo = 0
for i in l:
    if i == min(l):
        minimo = i
        break
    index += 1

print(f'Menor valor: {minimo}')
print(f'Posicao: {index}')
