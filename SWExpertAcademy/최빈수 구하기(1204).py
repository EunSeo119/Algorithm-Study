T = int(input())

for i in range(T):
    num = int(input())
    case = list(map(int, input().split()))
    frequency = [0 for i in range(101)]
    for j in range(1000):
        frequency[case[j]] += 1
    maxNum = max(frequency)
    maxIndex = frequency.index(max(frequency))
    while True:
        if maxNum in frequency:
            maxIndex = frequency.index(max(frequency))
            frequency[maxIndex] = 0
        else:
            break
    print("#" + str(num) + " " + str(maxIndex))
