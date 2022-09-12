from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i]==False:
                queue.append(i)
                check[i]=check[v]+1
                visited[i]=True

def dfs(V):
    visited[V] = True
    for i in graph[V]:
        if visited[i]==False:
            check[i]=check[V]+1
            dfs(i)
    
N = int(input())

A, B = map(int, input().split())

M = int(input())

graph = [[] for row in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * (N+1)
check=[0]*(N+1)

# bfs(A)
dfs(A)

if check[B]>0:
    print(check[B])
else:
    print(-1)
