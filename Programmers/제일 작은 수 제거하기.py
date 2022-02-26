def solution(arr):
    small=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<small:
            small=arr[i]
    arr.remove(small)
    if len(arr)==0:
        arr.append(-1)
    return arr
