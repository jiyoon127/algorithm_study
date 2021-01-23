from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[0] * (n+1)]
chess_map = [[deque() for _ in range(n+1)] for _ in range(n+1)]
pieces = []
seconds = 1

for i in range(n):
  graph.append([0]+list(map(int, input().split())))

for i in range(k):
  chess = list(map(int, input().split()))
  pieces.append(chess)
  chess_map[chess[0]][chess[1]].append(i+1)

dx = [int(1e9), 0, 0, -1, 1]
dy = [int(1e9), 1, -1, 0, 0]

def turn(d):
  if d == 1: d = 2
  elif d == 2: d = 1
  elif d == 3: d = 4
  else: d = 3
  return d

def move(nr, nc, r, c, d, i):
  fr = chess_map[r][c].index(i+1)
  to = len(chess_map[r][c])

  if graph[nr][nc] == 0 or graph[nr][nc] == 1:
    # to white
    for x in range(to):
      if x < fr:
        if graph[nr][nc] == 0:
          chess_map[r][c].append(chess_map[r][c].popleft())
      else:
        if graph[nr][nc] == 0:
          target = chess_map[r][c].popleft()
          pieces[target - 1][0] = nr
          pieces[target - 1][1] = nc
        else:
          target = chess_map[r][c].pop()
          pieces[target - 1][0] = nr
          pieces[target - 1][1] = nc
        chess_map[nr][nc].append(target)
    if len(chess_map[nr][nc]) >= 4:
      return True
  return False

def simulate():
  global seconds
  while seconds <= 1000:
    for i in range(k):
      r, c, d = pieces[i]
      nr = r + dx[d]
      nc = c + dy[d]
      
      if 1 <= nr <= n and 1 <= nc <= n and graph[nr][nc] != 2:
        if move(nr, nc, r, c, d, i): return
      else:
        # out or blue
        d = turn(d)
        pieces[i][2] = d

        nr = r + dx[d]
        nc = c + dy[d]
        if 1 <= nr <= n and 1 <= nc <= n:
          if move(nr, nc, r, c, d, i): return
    seconds += 1

simulate()
print(seconds if seconds <= 1000 else -1)
