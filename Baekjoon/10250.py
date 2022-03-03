num = int(input())
for i in range(num):
    H, W, N = map(int, input().split())
    count=1
    while(H<N):
        N=N-H
        count+=1
    if(count<10):
        print(str(N)+"0"+str(count))
    else:
        print(str(N)+str(count))
