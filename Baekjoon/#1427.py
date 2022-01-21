list = list(map(int, input()))
list.sort(reverse=True)
for i in range(len(list)):
    print(list[i], end="")
