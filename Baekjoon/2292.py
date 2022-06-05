N=int(input())
count=1
pre=0
result=1
while True:
    if N==1:
        print(result)
        break
    pre+=6
    count=pre+count
    result+=1
    if N<=count:
        print(result)
        break
