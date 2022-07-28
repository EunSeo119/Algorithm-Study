L, P = map(int, input().split())

num=L*P
A=list(map(int, input().split()))
for i in A:
    print(i-num,end=" ")
