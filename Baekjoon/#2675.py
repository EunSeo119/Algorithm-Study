S=[]
T = int(input())

for i in range(T):
    S=[]
    R, S = input().split()
    R = int(R)
    for j in range(len(S)):
       for k in range(R):
           print(S[j], end="")
    print()
