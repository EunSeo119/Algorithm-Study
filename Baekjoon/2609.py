import math
   
A, B=map(int, input().split())

result=math.gcd(A,B)
print(result)
print(A*B//result)
