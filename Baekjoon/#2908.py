A, B= map(str, input().split())

listA=list(A)
listB=list(B)
reA=[]
reB=[]

for i in range(2,-1,-1):
    reA.append(int(listA[i]))
    reB.append(int(listB[i]))
    
resultA=int(reA[0])*100+int(reA[1])*10+int(reA[2])
resultB=int(reB[0])*100+int(reB[1])*10+int(reB[2])

print(max(resultA, resultB))
