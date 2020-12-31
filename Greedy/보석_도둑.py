import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
weights = []
jewelries = []
jewelries_w = []
bag = 0
for _ in range(n):
  heapq.heappush(jewelries, list(map(int, input().split())))

for _ in range(k):
  heapq.heappush(weights, int(input()))

for _ in range(k):
  cur_w = heapq.heappop(weights)
  while jewelries and cur_w >= jewelries[0][0]:
    m, v = heapq.heappop(jewelries)
    heapq.heappush(jewelries_w, -v)
  if jewelries_w:
    bag -= heapq.heappop(jewelries_w)
  if not cur_w: break

print(bag)
