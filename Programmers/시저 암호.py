def solution(s, n):
    result=""
    for i in s:
        if i==" ":
            result+=" "
            continue
        i=ord(i)
        for j in range(n):
            if i==90:
                i=65
            elif i==122:
                i=97
            else:
                i+=1          
        result+=chr(i)
    return result
