while True:
    a = list(map(int, input().split()))
    if a[0]==0 and a[1]==0 and a[2]==0:
        break
    max_a=max(a)
    a.remove(max_a)
    if max_a*max_a==a[0]*a[0]+a[1]*a[1]:
        print("right")
    else:
        print("wrong")
