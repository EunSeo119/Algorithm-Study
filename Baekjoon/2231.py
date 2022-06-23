N = int(input())
result = 0

for i in range(1, N+1):
    sample=i+sum(map(int, str(i)))
    if sample==N:
        result=i
        break

print(result)
