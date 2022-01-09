import sys

count=int(input())
a=[0] * 10001
for i in range(count):
    pre_sort=int(sys.stdin.readline())
    a[pre_sort] += 1
for i in range(10001):
    if a[i]!=0:
        for j in range(a[i]):
            print(i)
