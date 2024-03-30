positivos = 0
promedio = 0
for i in range(6):
    entrada = float(input())
    if entrada > 0:
        positivos += 1
        promedio += entrada

print(f'{positivos} valores positivos')
print(f'{promedio/positivos:.1f}')
