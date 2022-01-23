import sys
input = sys.stdin.readline

result = 0
A, B = map(int, input().split())

for i in range(A, B+1):
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            result=1
            break;
    if result==0 and i!=1:
        print(i)
    result = 0
