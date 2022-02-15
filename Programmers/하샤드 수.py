def solution(x):
    sum = 0
    x=str(x)
    xlist = list(map(int, x))
    
    for i in range(len(xlist)):
        sum+=xlist[i]
    
    return int(x)%sum == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(13));
