N = int(input())
a=0
if N%2==1:
    a=N//2+1
else:
    a=N//2
b=N-a
print((a+1)*(b+1))
