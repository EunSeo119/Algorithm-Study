T=int(input())
for t in range(T):
    word=input()
    length=len(word)
    palindrome=1
    for i in range(length//2):
        if word[i]!=word[length-i-1]:
            palindrome=0
            break
    if palindrome==1:
        print("#{} {}".format(t+1, 1))
    else:
        print("#{} {}".format(t + 1, 0))
