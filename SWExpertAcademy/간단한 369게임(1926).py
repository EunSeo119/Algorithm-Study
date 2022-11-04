N = int(input())
result=""

for i in range(1, N+1):
    num = i
    isClap=0
    while num>10:
        if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
            result += "-"
            isClap=1
        num //= 10
    if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
        result += "-"
        isClap=1
    if isClap==0:
        result += str(i)
    result += " "

print(result)
