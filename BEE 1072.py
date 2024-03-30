n = int(input())
cont_in = 0
cont_out = 0
for i in range(n):
    x = int(input())
    if x >= 10 and x <=20:
        cont_in += 1
    else:
        cont_out += 1
print(f"{cont_in} in")
print(f"{cont_out} out")