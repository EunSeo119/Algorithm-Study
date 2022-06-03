import sys

N = int(sys.stdin.readline())
result=[]

for i in range(N):
    s=int(sys.stdin.readline())
    result.append(s)
    
result.sort()
for i in range(N):
    print(result[i])
