entrada = map(int, input().split())
x, y = entrada
item = {1:4, 2:4.50, 3:5, 4:2, 5:1.5}
print(f'Total: R$ {y*item[x]:.2f}')