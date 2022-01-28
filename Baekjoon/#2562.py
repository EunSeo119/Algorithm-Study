list=[]

for i in range(9):
    list.append(int(input()))
    
MAX=max(list)
print(MAX)
print(list.index(MAX)+1)
