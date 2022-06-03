import sys

K = int(sys.stdin.readline())
result = []

for i in range(K):
    s=int(sys.stdin.readline())
    if s==0:
        result.pop()
        continue
    result.append(s)

print(sum(result))
