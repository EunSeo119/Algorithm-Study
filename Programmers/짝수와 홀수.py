def solution(num):
    answer = ''
    if num%2==0:
        answer="Even"
    else:
        answer="Odd"
    return answer
    
    
#수정한 코드
def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"
