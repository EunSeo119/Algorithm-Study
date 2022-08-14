def solution(d, budget):
    d.sort()
    sum=0
    count=0
    for i in d:
        if sum>budget:
            return count-1
        sum+=i
        count+=1
    if sum>budget:
        return count-1
    else:
        return count
