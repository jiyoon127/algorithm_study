import sys
from collections import deque
input = sys.stdin.readline

days = -1
graph = []
ripe = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m, n = map(int, input().split())
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(m):
    if graph[i][j] == 1:
      ripe.append((i, j))

def bfs():
  global days
  while ripe:
    days += 1
    for _ in range(len(ripe)):
      x, y = ripe.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
          continue
        if graph[nx][ny] == -1: continue
        if graph[nx][ny] == 0:
          graph[nx][ny] = 1
          ripe.append((nx, ny))

bfs()

print(days if all(0 not in i for i in graph) else -1)
