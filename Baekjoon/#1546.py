result=0
N = int(input())

A = list(map(int, input().split()))

high = max(A)

for i in range(N):
    result=result+(A[i]/high*100)
    
print(result/N)
