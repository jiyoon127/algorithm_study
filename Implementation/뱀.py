# 백준 뱀
# https://www.acmicpc.net/problem/3190

import sys
input = sys.stdin.readline
n, k = int(input()), int(input())
graph = [[0] * n for _ in range(n)]
moves = []

dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

for _ in range(k):
  r, c = map(int, input().split())
  graph[r-1][c-1] = 1 # apple

l = int(input())
for _ in range(l):
  x, c = input().split()
  moves.append((int(x), c))

def turn(idx, direct):
  if direct == "L":
    idx = (idx - 1) % 4
  else: idx = (idx + 1) % 4
  return idx

def simulate():
  x, y = 0, 0
  graph[x][y] = 2
  direct_idx = 0
  move_idx = 0
  seconds = 0
  snake = [(x, y)]
  while True:
    nx = x + dx[direct_idx]
    ny = y + dy[direct_idx]
    seconds += 1
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 2:
      if graph[nx][ny] == 1:
        graph[nx][ny] = 2
        snake.append((nx, ny))
      else:
        graph[nx][ny] = 2
        snake.append((nx, ny))
        px, py = snake.pop(0)
        graph[px][py] = 0
    else: 
      break
    x, y = nx, ny
    if move_idx < l and seconds == moves[move_idx][0]:
      direct_idx = turn(direct_idx, moves[move_idx][1])
      move_idx += 1
  print(seconds)
simulate()
