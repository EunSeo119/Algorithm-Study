def solution(answers):
    math1=[1,2,3,4,5]
    math2=[2,1,2,3,2,4,2,5]
    math3=[3,3,1,1,2,2,4,4,5,5]
    result_arr=[]
    result1=0
    result2=0
    result3=0
    lens=len(answers)
    save=lens//5+1
    math1=math1*save
    math2=math2*save
    math3=math3*save
    for i in answers:
        if i==math1.pop(0):
            result1+=1
        if i==math2.pop(0):
            result2+=1
        if i==math3.pop(0):
            result3+=1
    
    max_result=max(result1,result2,result3)
    if result1==max_result:
        result_arr.append(1)
    if result2==max_result:
        result_arr.append(2)
    if result3==max_result:
        result_arr.append(3)
    return result_arr
