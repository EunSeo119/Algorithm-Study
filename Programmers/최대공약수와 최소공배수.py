def solution(n, m):
    answer = []
    A=1
    B=n*m
    for i in range(1,n+1):
        if n%i==0 and m%i==0:
            A=i
    for i in range(n*m,m-1,-1):
        if i%n==0 and i%m==0:
            B=i
    answer.append(A)
    answer.append(B)
    return answer
