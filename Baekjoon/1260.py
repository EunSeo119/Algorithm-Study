from collections import deque

def dfs(graph, V, visited):
    visited[V]=True
    print(V, end = ' ')
    for i in range(len(graph[V])):
        if visited[i]==False and graph[V][i]==1:
            dfs(graph, i, visited)
            
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(len(graph[v])):
            if visited[i]==False and graph[v][i]==1:
                queue.append(i)
                visited[i]=True
        

N, M, V = map(int, input().split())

graph = [[0 for col in range(N+1)] for row in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1

visited = [False]*(N+1)
visited[0] = True

dfs(graph, V, visited)
print()

visited = [False]*(N+1)
visited[0] = True

bfs(graph, V, visited)
