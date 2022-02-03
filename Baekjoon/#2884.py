A, B = map(int, input().split())

if B>=45:
    B-=45
else:
    if A==0:
        A=23
        B+=15
    else:
        A-=1
        B+=15

print(A,B,sep=" ")
