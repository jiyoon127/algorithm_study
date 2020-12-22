import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
v, e = map(int,input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
  a, b, w = map(int, input().split())
  graph[a].append((b, w))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: continue
    for x in graph[now]:
      cost = dist + x[1]
      if cost < distance[x[0]]:
        distance[x[0]] = cost
        heapq.heappush(q, (cost, x[0]))

dijkstra(k)

for i in range(1, len(distance)):
  if distance[i] == INF:
    print("INF")
  else: print(distance[i])
