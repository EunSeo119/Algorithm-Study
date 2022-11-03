N = int(input())

for i in range(N):
    check=list(map(int, input().split()))
    sum=0
    for j in range(10):
        if check[j]%2!=0:
            sum+=check[j]
    print("#"+str(i+1) + " "+str(sum))
