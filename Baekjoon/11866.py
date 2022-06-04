from collections import deque

N, K = map(int, input().split())

s=deque()
result=[]
for i in range(1,N+1):
    s.append(i)
    
while len(s)!=0:
    for i in range(K-1):
        s.append(s.popleft())
    result.append(s.popleft())
    
print("<", end="")
for i in range(N-1):
    print(result[i],end=", ")
print(str(result[N-1])+">")
