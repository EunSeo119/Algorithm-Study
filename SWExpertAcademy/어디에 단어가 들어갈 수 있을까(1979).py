T=int(input())
for t in range(T):
    N, K = map(int,input().split())
    matrix=[list(map(int, input().split())) for _ in range(N)]
    result=0
    for i in range(N):
        count=0
        for j in range(N):
            if matrix[i][j]==1:
                count+=1
            if matrix[i][j]==0:
                if count == K:
                    result += 1
                count=0
        if count == K:
            result+=1
    for i in range(N):
        count=0
        for j in range(N):
            if matrix[j][i] == 1:
                count += 1
            if matrix[j][i] == 0:
                if count == K:
                    result += 1
                count = 0
        if count == K:
            result += 1
    print("#{} {}".format(t+1, result))
