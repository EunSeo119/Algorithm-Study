T=int(input())

for t in range(T):
    N=int(input())
    snail=[[0]*N for i in range(1,N+1)]
    length=N
    step="right"
    number=1
    row=0
    col=0
    while(length!=0):
        if step=="right":
            for _ in range(length):
                snail[row][col]=number
                number+=1
                col+=1
            length-=1
            step="down"
            row+=1
            col-=1
        elif step=="down":
            for _ in range(length):
                snail[row][col]=number
                number+=1
                row+=1
            step="left"
            row-=1
            col-=1
        elif step=="left":
            for _ in range(length):
                snail[row][col]=number
                number+=1
                col-=1
            length-=1
            step = "up"
            row-=1
            col+=1
        elif step=="up":
            for _ in range(length):
                snail[row][col]=number
                number+=1
                row-=1
            step="right"
            row+=1
            col+=1
    print("#{}".format(t+1))
    for i in range(N):
        for j in range(N):
            print(str(snail[i][j]), end= " ")
        print()
