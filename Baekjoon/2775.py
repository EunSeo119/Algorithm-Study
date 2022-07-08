T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    array = [[0]*n for i in range(k+1)]
    for i in range(n):
        array[0][i]=i+1
    for j in range(1,k+1):
        for i in range(n):
            if i==0:
                array[j][i]=1
                continue
            array[j][i]=array[j][i-1]+array[j-1][i]
    print(array[k][n-1])
