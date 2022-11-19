T = int(input())
for t in range(T):
    result=""
    a, b = map(int, input().split())
    if a>b:
        result=">"
    elif a<b:
        result="<"
    elif a==b:
        result="="
    print("#{} {}".format(t+1, result))
