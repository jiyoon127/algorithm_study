import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[0]*n for _ in range(n)]

for _ in range(k):
  a, b = map(int, input().split())
  graph[a-1][b-1] = 1

def floyd(graph):
  for x in range(n):
    for a in range(n):
      for b in range(n):
          if graph[a][x] and graph[x][b]:
            graph[a][b] = 1
floyd(graph)

s = int(input())
for _ in range(s):
  a, b = map(int, input().split())
  if graph[a-1][b-1]: print(-1)
  elif graph[b-1][a-1]: print(1)
  else: print(0)
