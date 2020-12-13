import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a, c))
start, end = map(int, input().split())

min_w, max_w = 1, 1000000000

def bfs(limit):
  queue = deque([start])
  visited = [False] * (n+1)
  visited[start] = True
  while queue:
    a = queue.popleft()
    for b, c in graph[a]:
      if not visited[b] and c >= limit:
        queue.append(b)
        visited[b] = True
  return visited[end]

result = min_w
while min_w <= max_w:
  mid = (min_w + max_w) // 2
  if bfs(mid):
    result = mid
    min_w = mid + 1
  else: max_w = mid - 1
print(result)
