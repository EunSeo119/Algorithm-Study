def solution(array, commands):
    result=[]
    for z in range(len(commands)):
        i=commands[z][0]
        j=commands[z][1]
        k=commands[z][2]
        mid=array[i-1:j]
        mid.sort()
        result.append(mid[k-1])
    return result
