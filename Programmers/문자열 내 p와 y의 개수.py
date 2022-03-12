def solution(s):
    slist=list(s)
    pcount=0
    ycount=0
    for i in s:
        if i=="y" or i=="Y":
            ycount+=1
        elif i=="p" or i=="P":
            pcount+=1
    if (pcount==0 and ycount==0) or (pcount==ycount):
        return True
    else:
        return False
