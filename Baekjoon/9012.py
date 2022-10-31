N = int(input())

for i in range(N):
    check = input()
    left=0
    right=0
    no=0
    for j in range(len(check)):
        if check[j] == "(":
            left+=1
        else:
            right+=1
        if left<right:
            no=1
            break
    if no==1:
        print("NO")
    elif left == right:
        print("YES")
    else:
        print("NO")
