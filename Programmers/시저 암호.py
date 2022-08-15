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




# def caesar(s, n):
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#         elif s[i].islower():
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

#     return "".join(s)
