def rank(correct):
    if correct==6:
        return 1
    elif correct==5:
        return 2
    elif correct==4:
        return 3
    elif correct==3:
        return 4
    elif correct==2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    correct=0
    zero=0
    result=[]
    for i in lottos:
        if i==0:
            zero+=1
        else:
            if i in win_nums:
                correct+=1
    
    result.append(rank(correct+zero))
    result.append(rank(correct))
                
    return result
