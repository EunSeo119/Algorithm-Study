def solution(n):
    three=[]
    result=0
    while n>0:
        three.append(n%3)
        n=n//3
    for i in range(0,len(three)):
        result+=three[len(three)-i-1]*(3**i)
    return result
