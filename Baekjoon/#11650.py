count = int(input())
list=[]
for i in range(count):
    [x, y] = map(int, input().split())
    list.append([x,y])
    
list.sort()

for i in range(count):
    print(list[i][0], list[i][1])
