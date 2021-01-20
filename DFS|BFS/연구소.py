from collections import deque
from copy import deepcopy
import sys
inptut = sys.stdin.readline

graph = []
virus = []
temp = []
min_sec = int(1e9)

n, m = map(int, input().split())
for i in range(n):
  row = list(map(int, input().split()))
  graph.append(row)
  for j in range(n):
    if graph[i][j] == 2:
      virus.append((i, j, 0))

visited = [False] * len(virus)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(graph):
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 0:
        return False
  return True

def infection(candid, graph):
  v = [[0] * n for _ in range(n)]
  graph = deepcopy(graph)
  q = deque(candid)
  max_cnt = 0
  while q:
    x, y, cnt = q.popleft()
    v[x][y] = 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and not v[nx][ny] and graph[nx][ny] != 1:
        if graph[nx][ny] == 0:
          v[nx][ny] = 1
          graph[nx][ny] = 2
          max_cnt = cnt + 1
        q.append((nx, ny, cnt+1))
  if check(graph): return max_cnt
  else: return int(1e9)

def choose_virus():
  global min_sec
  if len(temp) == m:
    ans = infection(temp, graph)
    if ans != -1:
      min_sec = min(min_sec, ans)
    else: min_sec = ans
  for i in range(len(virus)):
    if visited[i]: continue
    visited[i] = True
    temp.append(virus[i])
    choose_virus()
    temp.pop()
    for j in range(i+1, len(virus)):
      visited[j] = False

choose_virus()
print(min_sec if min_sec < int(1e9) else -1)
