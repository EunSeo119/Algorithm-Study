def solution(strings, n):
    result2=[]
    array=dict()
    for i in strings:
        array[i]=i[n]
        
    array2=list(array.items())  
    # items() 안하면 정렬 후 key만 표기해줌!(그러므로 key랑 value 둘 다 표기하고 싶을 땐 items()), 그래서 items()붙이고 list로 만들어서 제작함
    array3=sorted(array2)   # key 값으로 정렬하기
    result=sorted(array3, key=lambda k : k[1])   # value 값으로 정렬하기
    for key in result:
        result2.append(key[0])
    return result2
