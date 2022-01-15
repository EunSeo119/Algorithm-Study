#198542
score = int(input())

if 90<=score<=100:
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
else:
    print('F')

#2753
year=int(input())

if year%4==0 and (year%100!=0 or year%400==0):
    print("1")
else:
    print("0")

#2742
N=int(input())

# for i in range(N):
#     print(N-i)
    
for i in range(N,0,-1):
    print(i)
