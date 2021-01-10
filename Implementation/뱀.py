# 백준 뱀
# https://www.acmicpc.net/problem/3190

import sys
input = sys.stdin.readline
n, k = int(input()), int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
info = []

for _ in range(k):
  a, b = map(int, input().split())
  graph[a][b] = 1

l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direct, c):
  if c == "L":
    direct = (direct - 1) % 4
  else:
    direct = (direct + 1) % 4
  return direct

def simulate():
  x, y = 1, 1
  graph[x][y] = 2
  direct = 0
  index = 0
  time = 0
  q = [(x, y)]
  while True:
    nx = x + dx[direct]
    ny = y + dy[direct]
    if 1 <= nx <= n and 1 <= ny <= n and graph[nx][ny] != 2:
      if graph[nx][ny] == 0:
        graph[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        graph[px][py] = 0
      if graph[nx][ny] == 1:
        graph[nx][ny] = 2
        q.append((nx, ny))
    else:
      time += 1
      break
    x, y = nx, ny
    time += 1
    if index < l and time == info[index][0]:
      direct = turn(direct, info[index][1])
      index += 1
  return time
print(simulate())
