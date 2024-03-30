dia_inicio = input()
hi, mi, si = map(int, input().split(':'))
dia_fin = input()
hf, mf, sf= map(int, input().split(':'))
dia_inicio = int(dia_inicio[-1])
dia_fin = int(dia_fin[-1])
segundos = sf - si
minutos = mf - mi
horas = hf - hi
dias = dia_fin - dia_inicio
if segundos < 0:
    segundos += 60
    minutos -= 1
if minutos < 0:
    minutos += 60
    horas -= 1
if horas < 0:
    horas += 24
    dias -= 1
print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')
