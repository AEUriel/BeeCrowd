c = 0
r = 0
s = 0
n = int(input())
for i in range(n):
    num, letra = map(str, input().split())
    num = int(num)
    if letra == 'C':
        c += num
    elif letra == 'R':
        r += num
    elif letra == 'S':
        s += num
total = c+s+r
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {(c/total)*100:.2f} %')
print(f'Percentual de ratos: {(r/total)*100:.2f} %')
print(f'Percentual de sapos: {(s/total)*100:.2f} %')