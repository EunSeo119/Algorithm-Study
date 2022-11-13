T=int(input())

for t in range(T):
    result=""
    num=input()
    year=int(num[0:4])
    month = int(num[4:6])
    day = int(num[6:8])
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day>=1 and day<=31:
            result=str(year).zfill(4)+"/"+str(month).zfill(2)+"/"+str(day).zfill(2)
        else:
            result="-1"
    elif month==4 or month==6 or month==9 or month==11:
        if day>=1 and day<=30:
            result=str(year).zfill(4)+"/"+str(month).zfill(2)+"/"+str(day).zfill(2)
        else:
            result="-1"
    elif month==2:
        if day>=1 and day<=28:
            result=str(year).zfill(4)+"/"+str(month).zfill(2)+"/"+str(day).zfill(2)
        else:
            result="-1"
    else:
        result="-1"
    print("#{} {}".format(t+1,result))
