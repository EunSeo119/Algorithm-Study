def solution(phone_number):
    answer = ''
    s = list(phone_number)
    size=len(s)
    for i in range(size-4):
        answer+="*"
    for i in range(size-4,size):
        answer +=s[i]
    
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + solution('01033334444'));

#다른사람이 짠 코드
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]
