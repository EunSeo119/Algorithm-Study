import math

def solution(s):
    result=''
    N=math.ceil(len(s)/2)
    if len(s)%2==0:
        result+=s[N-1]
        result+=s[N]
    else:
        result+=s[N-1]
        
    return result
