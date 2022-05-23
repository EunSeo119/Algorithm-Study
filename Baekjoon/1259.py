import math

while True:
    word = input()
    match=0
    if word=='0':
        break
    count=math.ceil(len(word)/2)
    
    for i in range(count):
        if(word[i]==word[-(i+1)]):
            match+=1
    
    if(match==count):
        print("yes")
    else:
        print("no")
