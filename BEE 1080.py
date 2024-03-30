j = 0
index = 0
for i in range(0,100):
    n = int(input())
    if n > j:
        j = n
        index = i+1

print(j)
print(index)
