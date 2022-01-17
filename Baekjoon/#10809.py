s = input();
abc="abcdefghijklmnopqrstuvwxyz"
result=[]

for i in abc:
    if i in s:
        result.append(s.index(i))
    else:
        result.append(-1)
        
for i in result:
    print(i,end=" ")
