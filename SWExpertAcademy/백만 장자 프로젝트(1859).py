T=int(input())

for t in range(T):
    N=int(input())
    case=list(map(int, input().split()))
    buy=0
    count=0
    profit=0
    now=case[N-1]
    max=0
    for i in range(N-1,0,-1):
        if now>case[i-1]:
            buy+=case[i-1]
            count+=1
            if max<now:
                max=now
        else:
            profit+=(max*count-buy)
            count=0
            buy=0
            now=case[i-1]
    profit += (max * count - buy)
    print("#"+str(t+1)+" "+str(profit))
