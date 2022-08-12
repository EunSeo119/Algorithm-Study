def solution(a, b):
    save='FRI'
    result=['THU','FRI','SAT','SUN','MON','TUE','WED']
    for i in range(1,a+1):
        if i==a:
            return result[b%7]
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            result.append(result.pop(0))
            result.append(result.pop(0))
            result.append(result.pop(0))
        elif i==2:
            result.append(result.pop(0))
        else:
            result.append(result.pop(0))
            result.append(result.pop(0))
