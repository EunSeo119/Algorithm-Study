N=list(map(int, input()))
list=[]
result=0

for i in range(10):
    list.append(0)
for i in range(len(N)):
    num=N[i]
    list[num]+=1

for i in range(10):
    if i==6:
        if (list[6]+list[9])%2==1:
            list[9]=int((list[6]+list[9])/2)+1
            list[6]=0
        else:
            list[9]=int((list[6]+list[9])/2)
            list[6]=0
    result=max(result,list[i])    
print(result)
