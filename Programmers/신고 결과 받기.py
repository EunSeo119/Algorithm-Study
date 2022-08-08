def solution(id_list, report, k):
    report=set(report)
    check={}
    result=[0]*len(id_list)
    for i in report:
        a,b=i.split()
        if b not in check:
            check[b]=a
        else:
            c=check[b]
            check[b]=c+" "+a
    for i in check:
        d=check[i]
        if d.count(" ")>=k-1:
            e=list(d.split())
            for i in e:
                f=id_list.index(i)
                result[f]+=1
        
    return result
