Pi = 3.14159
entrada = str(input()).split(" ")
a,b,c = entrada
a,b,c = float(a),float(b),float(c)

print(f"TRIANGULO: {(a*c)/2:.3f}")
print(f"CIRCULO: {(Pi*pow(c,2)):.3f}")
print(f"TRAPEZIO: {((a+b)*c)/2:.3f}")
print(f"QUADRADO: {b*b:.3f}")
print(f"RETANGULO: {(a*b):.3f}")