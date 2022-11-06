T = int(input())

for t in range(T):
    N,M=map(int, input().split())

    flys = [[0]*N for i in range(N)]

    for i in range(N):
        flys[i]=list(map(int, input().split()))

    maxFlys=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum=0
            for k in range(M):
                for l in range(M):
                    sum+=flys[i+k][j+l]
            if maxFlys<sum:
                maxFlys=sum

    print("#"+str(t+1)+" "+str(maxFlys))
