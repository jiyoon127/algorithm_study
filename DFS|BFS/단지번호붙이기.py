import sys
input = sys.stdin.readline

total = 0
units = []
cnt = 0
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

def dfs(x, y):
  global cnt
  if x < 0 or y < 0 or x > n - 1 or y > n - 1:
    return False
  if graph[x][y] != 0:
    cnt += 1
    graph[x][y] = 0
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False
for i in range(n):
  for j in range(n):
    if dfs(i,j):
      total += 1
      units.append(cnt)
    cnt = 0

units.sort()
print(total)
for i in units: print(i)
