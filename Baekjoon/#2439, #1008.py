#2439
N=int(input())

for i in range(1, N+1):
    for j in range(N-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()


#1008
A, B = map(int, input().split())

print(A/B)
