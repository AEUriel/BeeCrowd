suma = 0
x = int(input())
y = int(input())
if x > y:
    z = y
    y = x
    x = z
for i in range(x, y+1):
    if i%13 != 0 and i <= y:
        suma += i
print(suma)