entrada = float(input())
if entrada <= 400:
    print(f'Novo salario: {entrada*1.15:.2f}\nReajuste ganho: {(entrada*1.15)-entrada:.2f}\nEm percentual: 15 %')
elif entrada > 400 and entrada <= 800:
    print(f'Novo salario: {entrada*1.12:.2f}\nReajuste ganho: {(entrada*1.12)-entrada:.2f}\nEm percentual: 12 %')
elif entrada > 800 and entrada <= 1200:
    print(f'Novo salario: {entrada*1.1:.2f}\nReajuste ganho: {(entrada*1.1)-entrada:.2f}\nEm percentual: 10 %')
elif entrada > 1200 and entrada <= 2000:
    print(f'Novo salario: {entrada*1.07:.2f}\nReajuste ganho: {(entrada*1.07)-entrada:.2f}\nEm percentual: 7 %')
else:
    print(f'Novo salario: {entrada*1.04:.2f}\nReajuste ganho: {(entrada*1.04)-entrada:.2f}\nEm percentual: 4 %')