res = ''
n = int(input())
for i in range(1,n*4, 4):
    res = str(i) +' '+str(i+1)+' '+str(i+2)
    print(f'{res} PUM')