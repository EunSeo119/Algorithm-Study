N, M = map(int, input().split())

A=list(map(int, input().split()))
len=len(A)
sum = 0

for i in range(0, len-2):
    for j in range(i+1, len-1):
        for k in range(j+1, len):
            if A[i]+A[j]+A[k]>M:
                continue
            else:
                sum=max(sum, A[i]+A[j]+A[k])
                
print(sum)
