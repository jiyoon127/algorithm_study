import sys
from collections import deque
input = sys.stdin.readline

s = int(input())
visited = {(1, 0): 0}

def bfs(d, c): # display, clip board
  queue = deque()
  queue.append((d, c))
  while queue:
    d, c = queue.popleft()
    if d == s:
      print(visited[d, c])
      break
    if (d, d) not in visited:
      visited[(d, d)] = visited[(d, c)] + 1
      queue.append((d, d))
    if d + c <= s and (d + c, c) not in visited:
      visited[(d + c, c)] = visited[(d, c)] + 1
      queue.append((d + c, c))
    if d - 1 >= 0 and (d - 1, c) not in visited:
      visited[(d - 1, c)] = visited[(d, c)] + 1
      queue.append((d - 1, c))

bfs(1, 0)
