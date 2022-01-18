s1 = list(input())
s0=list(s1)
count1=0
count0=0
len=len(s1)
for i in range(len):
    if s1[i]=='1':
        if i==len-1:
            count2=0
        elif s1[i+1]=='1':
            count1-=1
        count1+=1
        s1[i]='0'
        
    if s0[i]=='0':
        if i==len-1:
            count2=0
        elif s0[i+1]=='0':
            count0-=1
        count0+=1
        s0[i]='1'
        
print(min(count1, count0))
