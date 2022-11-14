T = int(input())

for t in range(T):
    puzzle=[[0]*9 for _ in range(9)]
    for i in range(9):
        puzzle[i]=list(map(int, input().split()))
    for i in range(9):
        row = len(set(puzzle[i]))
        if row != 9:
            break
    for i in range(9):
        col = []
        for j in range(9):
            col.append(puzzle[j][i])
        if len(set(col)) != 9:
            break
    for i in range(0,9,3):
        square = []
        for j in range(0,9,3):
            square.append(puzzle[i][j])
            square.append(puzzle[i][j+1])
            square.append(puzzle[i][j+2])
            square.append(puzzle[i+1][j])
            square.append(puzzle[i + 1][j + 1])
            square.append(puzzle[i + 1][j + 2])
            square.append(puzzle[i+2][j])
            square.append(puzzle[i + 2][j + 1])
            square.append(puzzle[i + 2][j + 2])
            if len(set(square)) != 9:
                break
        if len(set(square)) != 9:
            break
    if row != 9 or len(set(col)) != 9 or len(set(square)) != 9:
        print("#{} {}".format(t + 1, 0))
    else:
        print("#{} {}".format(t + 1, 1))
