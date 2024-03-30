n = int(input())
arr = list((0,1))
for i in range(0,n-1):
    if i >= 1:
        arr.append(arr[i] + arr[i-1])

for i in range(len(arr)):
    if (i == (n - 1)):
        print(arr[i])

    else:
        print(arr[i], end=" ")