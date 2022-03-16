S=list(map(int, input().split()))
T=list(map(int, input().split()))

sumS=sum(S)
sumT=sum(T)

if sumS==sumT:
    print(sumS)
else:
    print(max(sumS,sumT))
