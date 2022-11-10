N=int(input())
list=list(map(int,input().split()))
list.sort()
num=N//2+1
print(list[num])
