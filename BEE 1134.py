alcool = 0
gas = 0
diesel = 0
print('MUITO OBRIGADO')
while True:
    x = int(input())
    if x == 1:
        alcool += 1
    elif x == 2:
        gas += 1
    elif x == 3:
        diesel += 1
    elif x == 4:
        print(f'Alcool: {alcool}')
        print(f'Gasolina: {gas}')
        print(f'Diesel: {diesel}')
        break
    else:
        continue
