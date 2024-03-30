entrada = str(input()).split(" ")
a,b,c = entrada
a,b,c = int(a), int(b), int(c)

mayor = ((a+b+abs(a-b))/2)
res = ((mayor+c+abs(mayor-c))/2)

print(f"{int(res)} eh o maior")