N=int(input())

words=[]
wordLen=[]
preprint=0
for i in range(N):
    word=input()
    words.append(word)
    
for i in range(N):
    lenW=len(words[i])
    wordLen.append(lenW)
    
count=0
while len(words)!=0:  
    count+=1 
    minword=min(wordLen)
    min_list = [i for i, value in enumerate(wordLen) if value == minword]
    if len(min_list)==1:
        wordIndex=min_list[0]
        print(words[wordIndex])
        words.remove(words[wordIndex])
        wordLen.remove(wordLen[wordIndex])
    else:
        min_list2=[]
        for i in range(len(min_list)):
            min_list2.append(words[min_list[i]])
        min_list2.sort()
        for i in range(len(min_list2)):
            wordResult=min_list2[i]
            if preprint!=wordResult:
                print(wordResult)
            preprint=wordResult
            wordIndex=words.index(wordResult)
            words.remove(wordResult)
            del wordLen[wordIndex]
