import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, node, visited):
  visited[node] = True
  print(node, end=' ')
  for i in graph[node]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

for i in range(m):
  n1, n2 = map(int, input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)

for lines in graph:
  lines.sort()

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)
