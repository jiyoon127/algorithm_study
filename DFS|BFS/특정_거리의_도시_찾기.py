# 백준 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int ,input().split())
graph = [[] for _ in range(n+1)]
q = deque()
cities = []

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

def bfs(start):
  q.append(start)
  while q:
    now = q.popleft()
    for node in graph[now]:
      if distance[node] == -1:
        distance[node] = distance[now] + 1
        q.append(node)

bfs(x)

for (idx, dist) in enumerate(distance):
  if dist == k:
    cities.append(idx)
cities.sort()

if cities:
  for city in cities:
    print(city)
else: print(-1)
