from collections import deque

def bfs(graph):
    queue = deque([1])
    visited[1]==True
    while deque:
        v=queue.popleft()
        for i in range(len(graph[v])):
            if visited[i]==False and graph[v][i]==1:
                queue.append(i)
                visited[i]=True
        if len(queue)==0:
            break

N=int(input())
M=int(input())

graph = [[0 for col in range(N+1)] for row in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1
    
visited = [False] * (N+1)
visited[0] = True
    
bfs(graph)
count=0
for i in visited:
    if i==True:
        count+=1
print(count-2)
