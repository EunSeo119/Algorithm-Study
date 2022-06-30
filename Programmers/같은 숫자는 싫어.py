def solution(arr):
    result =[]
    same=-1
    for i in range(len(arr)):
        if same!=arr[i]:
           result.append(arr[i])
        same=arr[i]
        
    return result
