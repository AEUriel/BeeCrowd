entrada = map(float, input().split())
a,b,c,d = entrada
prom = ((a*2)+(b*3) +(c*4) + d)/10
if prom >= 5 and prom <= 6.9:
    examen = float(input())
    final = (examen + prom)/2
print(f"Media: {prom:.1f}")
if prom >= 7:
    print('Aluno aprovado.')
elif prom < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    print(f'Nota do exame: {examen:.1f}')
    if final >= 5:
        print('Aluno aprovado.') 
    else:
        print('Aluno reprovado.')
    print(f'Media final: {final:.1f}')