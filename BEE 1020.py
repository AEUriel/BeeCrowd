dias = int(input())
print(f'{int(dias/365)} ano(s)')
aux=dias%365
print(f'{int(aux/30)} mes(es)')
aux=aux%30
print(f'{int(aux)} dia(s)')