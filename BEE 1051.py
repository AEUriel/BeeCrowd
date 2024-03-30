sueldo = float(input())

if sueldo <= 2000:
    print('Isento')
elif sueldo > 2000 and sueldo <= 3000:
    res = sueldo - 2000
    resultado = res * 0.08
    print(f'R$ {resultado:.2f}')
elif sueldo > 3000 and sueldo < 4500:
    res = sueldo - 3000
    resultado = (res * 0.18) + (1000 * 0.08)
    print(f'R$ {resultado:.2f}')
else:
    res = sueldo - 4500
    resultado = (res * 0.28) + (1500 * 0.18)+ (1000 * 0.08)
    print(f'R$ {resultado:.2f}')