def solution(n):
    check=n
    for i in range(1,n):
        if n%i==1:
            check=min(check,i)
            break
    return check
