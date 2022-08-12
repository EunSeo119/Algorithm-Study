def solution(absolutes, signs):
    sum=0
    for i in range(len(absolutes)):
        if signs[i]==False:
            absolutes[i]*=-1
        sum+=absolutes[i]
    return sum
