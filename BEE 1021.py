billetes = float(input())
print('NOTAS:')    
print(f'{int(billetes/100)} nota(s) de R$ 100.00')
aux = billetes%100
print(f'{int(aux/50)} nota(s) de R$ 50.00')
aux = aux % 50
print(f'{int(aux/20)} nota(s) de R$ 20.00')
aux =aux % 20
print(f'{int(aux/10)} nota(s) de R$ 10.00')
aux =aux % 10
print(f'{int(aux/5)} nota(s) de R$ 5.00')
aux =aux % 5
print(f'{int(aux/2)} nota(s) de R$ 2.00')
aux = aux % 2
print('MOEDAS:')
print(f'{int(aux)} moeda(s) de R$ 1.00')
aux = billetes * 100
aux = aux % 100
print(f'{int(aux/50)} moeda(s) de R$ 0.50')
aux = aux % 50
print(f'{int(aux/25)} moeda(s) de R$ 0.25')
aux = aux % 25
print(f'{int(aux/10)} moeda(s) de R$ 0.10')
aux = aux % 10
print(f'{int(aux/5)} moeda(s) de R$ 0.05')
aux = aux % 5
print(f'{int(aux/1)} moeda(s) de R$ 0.01')