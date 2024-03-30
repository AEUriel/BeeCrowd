entrada_1 = str(input()).split(" ")
entrada_2 = str(input()).split(" ")

x1, y1 = entrada_1
x1, y1 = float(x1), float(y1)
x2, y2 = entrada_2
x2, y2 = float(x2), float(y2)
 
distancia = (pow((x2 - x1),2) + pow((y2 - y1),2))
raiz = pow(distancia, 1/2)
print(f'{raiz:.4f}')
