import sys

N = int(sys.stdin.readline())
result=[]
s=[]

for i in range(N):
    a, b = map(int, input().split())
    result.append([b, a])

result.sort()

for i in range(N):
    print(result[i][1], end=" ")
    print(result[i][0])
