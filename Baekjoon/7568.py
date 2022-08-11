N=int(input())
check=[]

for _ in range(N):
    w,h=map(int, input().split())
    check.append((w,h))

for i in range(N):
    rank=1
    for j in range(N):
        if check[i][0]<check[j][0] and check[i][1]<check[j][1]:
            rank+=1
    print(rank, end=" ")
