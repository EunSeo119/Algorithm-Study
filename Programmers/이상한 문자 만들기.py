def solution(s):
    result=""
    finish=0
    words=s.split(" ")
    for j in words:
        W=j
        count=0
        finish+=1
        for i in W:
            if count%2!=0:
                result+=(i.lower())
                count+=1
            else:
                result+=(i.upper())
                count+=1
        if finish!=len(words):
            result+=" "
    return result
