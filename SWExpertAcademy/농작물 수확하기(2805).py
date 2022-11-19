T=int(input())
for t in range(T):
    N=int(input())
    length=N//2
    result = 0
    for i in range(N):
        ground=input()
        getLength=(i+1)*2-1
        if getLength>N:
            get=ground[i-length:N-(i-length)]
            change=list(map(int, get))
        else:
            get = ground[length - i:length + i + 1]
            change = list(map(int, get))
        result+=sum(change)
    print("#{} {}".format(t+1,result))
