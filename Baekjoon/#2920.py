A = list(map(int, input().split()))
asc=0
des=0
len=len(A)
for i in range(len):
    if A[i]==i+1:
        asc+=1
    if A[i]==len-i:
        des+=1

if asc==8:
    print("ascending")
elif des==8:
    print("descending")
else:
    print("mixed")
