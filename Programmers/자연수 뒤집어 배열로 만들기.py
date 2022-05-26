def solution(n):
    num=str(n)
    result=[]
    count=len(num)
    for i in range(count):
        count-=1
        result.append(int(num[count]))
    return result
