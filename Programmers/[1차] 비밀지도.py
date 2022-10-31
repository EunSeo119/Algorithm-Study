def solution2(n, arr1, arr2):
    result = []
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])

        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        result.append(tmp)
    return result
    
def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        a = bin(arr1[i])[2:]
        b = bin(arr2[i])[2:]
        if len(a)<n:
            while n-len(a):
                a = "0" + a
        if len(b)<n:
            while n-len(b):
                b = "0" + b
        save = ""
        for j in range(n):
            if a[j] == "1" or b[j] == "1":
                save += "#"
            else:
                save += " "
        result.append(save)
    return result    
