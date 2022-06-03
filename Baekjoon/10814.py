N = int(input())
result=[]

for i in range(N):
    s=list(input().split())
    result.append(s)
    
result.sort(key=lambda x:int(x[0]))
    
for i in range(N):
    print(result[i][0], end=" ")
    print(result[i][1])
