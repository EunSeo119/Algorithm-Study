count=int(input())
for i in range(count):
    quiz = input()
    quiz_list=list(quiz)
    sum = 0
    sum2=1
    for i in quiz_list:
        if i=='O':
            sum+=sum2
            sum2+=1
        else:
            sum2=1
    print(sum)
