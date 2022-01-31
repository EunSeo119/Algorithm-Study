N=int(input())
result = 0

A=list(map(int, input().split()))
B=list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(N):
    a=A.pop()
    b=B.pop()
    result+=a*b

print(result)
