def solution(arr, divisor):
    result=[]
    for i in arr:
        if i%divisor==0:
            result.append(i)
    if len(result)==0:
        result.append(-1)
    result.sort()
    return result
