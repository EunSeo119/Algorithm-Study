T=int(input())
for t in range(T):
    case=input()
    check=""
    for i in range(10):
        correct = 0
        check=case[0:i+1]
        num=30//(i+1)
        subCase=case
        for j in range(num-1):
            subCase=subCase[i+1:]
            if check != subCase[0:i+1]:
                correct=1
                break
        if correct!=1:
            print("#{} {}".format(t+1,i+1))
            break
