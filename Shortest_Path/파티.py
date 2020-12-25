import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m, x = map(int,  input().split())
graph = [[] for _ in range(n+1)]
answer = [0] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  distance = [INF] * (n+1)
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance

for i in range(1, n+1):
  forward = dijkstra(i)
  backward = dijkstra(x)
  answer[i] += forward[x] + backward[i]

print(max(answer))
