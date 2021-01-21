from copy import deepcopy
import sys
input = sys.stdin.readline

ans = int(1e9)
tot = 0
n = int(input())
graph = [[0] * (n+1)]
for _ in range(n):
  row = list(map(int,input().split()))
  tot += sum(row)
  graph.append([0] + row)

def div(x, y, d1, d2, graph):
  each_sec = [0 for _ in range(6)]
  graph = deepcopy(graph)
  for i in range(d1+1):
    graph[x+i][y-i] = False
    graph[x+d2+i][y+d2-i] = False
  for i in range(d2+1):
    graph[x+i][y+i] = False
    graph[x+d1+i][y-d1+i] = False
  
  for i in range(x+1, x+d1+d2):
    isFalse = False
    for j in range(1, n+1):
      if not graph[i][j]: isFalse = not isFalse
      if isFalse: graph[i][j] = False
  
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i < x+d1 and j <= y and graph[i][j]:
        each_sec[1] += graph[i][j]
      elif i <= x+d2 and y < j and graph[i][j]:
        each_sec[2] += graph[i][j]
      elif x+d1 <= i and j < y-d1+d2 and graph[i][j]: each_sec[3] += graph[i][j]
      elif x+d2 < i and y-d1+d2 <= j and graph[i][j]: each_sec[4] += graph[i][j]

  each_sec[5] = tot - sum(each_sec)
  return max(each_sec[1:]) - min(each_sec[1:])

for x in range(1, n+1):
  for y in range(1, n+1):
    for d1 in range(1, n+1):
      for d2 in range(1, n+1):
        if 1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n:
          ans = min(ans, div(x, y, d1, d2, graph))

print(ans)
