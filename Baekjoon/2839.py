N=int(input())
error=0
for i in range(N//5,-1,-1):
    save=N-(i*5)
    if(save%3==0):
        print(i+save//3)
        error=1
        break
    
if (error==0):
    print(-1)
