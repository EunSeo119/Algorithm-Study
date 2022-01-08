word=input().upper()
word_set=list(set(word))
count_result=[]

for i in word_set:
    count=word.count(i)
    count_result.append(count)

if count_result.count(max(count_result)) >= 2:
    print("?")
else:
    print(word_set[count_result.index((max(count_result)))])
