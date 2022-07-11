def solution(numbers):
    result=0
    count=[0 for i in range(10)]
    for i in range(len(numbers)):
        index=numbers[i]
        count[index]=1
    for i in range(10):
        if count[i]==0:
            result+=i
    return result
