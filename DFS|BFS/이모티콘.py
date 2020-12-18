import sys
import math
from collections import deque
input = sys.stdin.readline

s = int(input())
visited = [[math.inf] * 1001 for _ in range(1001)]

def bfs(d, c): # display, clip board
  queue = deque()
  visited[d][c] = 0
  queue.append((d, c))
  while queue:
    d, c = queue.popleft()
    if visited[d][d] == math.inf:
      visited[d][d] = visited[d][c] + 1
      queue.append((d, d))
    if d + c <= s and visited[d + c][c] == math.inf:
      visited[d + c][c] = visited[d][c] + 1
      queue.append((d + c, c))
    if d - 1 >= 0 and visited[d - 1][c] == math.inf:
      visited[d - 1][c] = visited[d][c] + 1
      queue.append((d - 1, c))

bfs(1, 0)
print(min(visited[s]))
