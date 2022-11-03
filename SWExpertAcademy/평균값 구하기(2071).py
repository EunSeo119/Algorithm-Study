T=int(input())

for i in range(T):
    case = list(map(int, input().split()))
    result = sum(case)
    result = round(result/10)
    print('#'+str(i+1)+" "+str(result))
