T=int(input())
for t in range(T):
    N= int(input())
    block=[list(map(int, input().split())) for _ in range(N)]

    turn_90=[[0 for _ in range(N)] for _ in range(N)]
    turn_180=[[0 for _ in range(N)] for _ in range(N)]
    turn_270=[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            turn_90[i][j] = block[N-j-1][i]
    for i in range(N):
        for j in range(N):
            turn_180[i][j] = turn_90[N-j-1][i]
    for i in range(N):
        for j in range(N):
            turn_270[i][j] = turn_180[N-j-1][i]

    print("#{}".format(t+1))
    for i in range(N):
        for j in range(N):
            print(turn_90[i][j], end="")
        print(end=" ")
        for j in range(N):
            print(turn_180[i][j], end="")
        print(end=" ")
        for j in range(N):
            print(turn_270[i][j], end="")
        print()
