import math

N=int(input())
a=list(map(int, input().split()))
num=0

for i in a:
    prime=1
    if i==1:
        prime=0
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            prime=0
    if prime==1:
        num+=1
print(num)
