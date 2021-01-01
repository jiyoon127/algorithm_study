import sys
input = sys.stdin.readline
r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
step = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  global step
  q = set([(0, 0, graph[0][0])])
  while q:
    x, y, path = q.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < r) and (0 <= ny < c) and graph[nx][ny] not in path:
        q.add((nx, ny, path + graph[nx][ny]))
        step = max(step, len(path) + 1)
bfs()
print(step)
