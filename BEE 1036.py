a,b,c = map(float, input().split())

aux = (pow(b, 2))- (4 * a * c)

if aux < 0 or a == 0:
    print("Impossivel calcular")
else:
    aux = pow(aux, 1/2)
    r2 = ((-b) - aux)/(2 *a)
    r1 = ((-b) + aux)/(2 *a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")