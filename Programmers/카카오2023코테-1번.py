def solution(today, terms, privacies):
    result=[]
    count=1
    tyear, tmonth, tday = map(int, today.split("."))
    tdate=int(tyear)*12*28 + int(tmonth)*28 + int(tday)
    for i in privacies:
        date, types = i.split()
        year,month,day=map(int, date.split("."))
        pdate=int(year)*12*28 + int(month)*28 + int(day)
        for j in terms:
            t, m = j.split()
            if types == t:
                types_month=int(m)
        pdate+=types_month*28
        if tdate<pdate:
            count+=1
            continue
        else:
            result.append(count)
            count+=1
            continue   
    return result
