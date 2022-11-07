for t in range(10):
    N= int(input())
    result=0
    building=list(map(int, input().split()))
    for i in range(2,N-2):
        high=max(building[i-2],building[i-1],building[i+1],building[i+2])
        if high<building[i]:
            result+=(building[i]-high)
    print("#{} {}".format(t+1,result))
