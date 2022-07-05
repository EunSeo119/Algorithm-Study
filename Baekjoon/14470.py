A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())

if A<0:
    result=(-A)*C
    result+=D
    result+=(B*E)
else:
    result=B-A
    result*=E
    
print(result)
