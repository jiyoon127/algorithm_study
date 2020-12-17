import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

total = 0
cnt = 0
spaces = []
m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(x1, x2):
    for j in range(y1, y2):
      graph[j][i] = 1

def dfs(x, y):
  global cnt
  if x < 0 or y < 0 or x >= m or y >= n:
    return False
  if graph[x][y] == 0:
    cnt += 1
    graph[x][y] = 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False

for i in range(m):
  for j in range(n):
    if dfs(i, j):
      total += 1
      spaces.append(cnt)
    cnt = 0
spaces.sort()
print(total)
for space in spaces: print(space, end = ' ')
