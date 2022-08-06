num=int(input())
a=input()
sum=0
for i in range(num):
    sum+=(ord(a[i])-96)*(31**i)
print(sum%1234567891)
