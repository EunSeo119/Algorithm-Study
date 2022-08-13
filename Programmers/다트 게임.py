def solution(dartResult):
    score=[]
    check=0
    now=0
    out=0
    for i in range(len(dartResult)):
        if out==1:
            out=0
            continue
        if dartResult[i]=='T':
            save=save*save*save
            score.append(save)
            now+=1
        elif dartResult[i]=='D':
            save=save*save
            score.append(save)
            now+=1
        elif dartResult[i]=='S':
            score.append(save)
            now+=1
        elif dartResult[i]=='*':
            save*=2
            if check>3:
                pre=score[now-2]
                score[now-2]=pre*2
            score[now-1]=save
        elif dartResult[i]=='#':
            save*=-1
            score[now-1]=save        
        else:
            if dartResult[i]=='1':
                if dartResult[i+1]=='0':
                    save=10
                    out=1
                    continue
            save=int(dartResult[i])
        check+=1
    return sum(score)
    
    
    
    
    
# def solution(dartResult):
#     point = []
#     answer = []
#     dartResult = dartResult.replace('10','k')
#     point = ['10' if i == 'k' else i for i in dartResult]
#     print(point)

#     i = -1
#     sdt = ['S', 'D', 'T']
#     for j in point:
#         if j in sdt :
#             answer[i] = answer[i] ** (sdt.index(j)+1)
#         elif j == '*':
#             answer[i] = answer[i] * 2
#             if i != 0 :
#                 answer[i - 1] = answer[i - 1] * 2
#         elif j == '#':
#             answer[i] = answer[i] * (-1)
#         else:
#             answer.append(int(j))
#             i += 1
#     return sum(answer)
