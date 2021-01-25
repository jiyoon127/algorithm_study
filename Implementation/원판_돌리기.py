from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

data = deque([0])
turn_info = []
ans = 0
cnt = 0
n, m, t = map(int, input().split())
tot_cnt = n * m

for _ in range(n):
  data.append(deque(map(int, input().split())))

for _ in range(t):
  turn_info.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0 ,1, 0, -1]

def turn(x, d, k):
  for i in range(x, n+1, x):
    if d == 0:
      data[i].rotate(k)
    else:
      data[i].rotate(-k)

def erase(x, y, target):
  global cnt
  for i in range(4):
    nx = (x + dx[i])
    ny = (y + dy[i]) % m
    if 1 <= nx <= n and 0 <= ny < m and data[nx][ny] == target:
      cnt += 1
      data[nx][ny] = 0
      erase(nx, ny, target)

for i in range(1, n+1):
  for j in range(m):
    ans += data[i][j]

for (x, d, k) in turn_info:
  flag = True
  turn(x, d, k)

  for i in range(1, n+1):
    for j in range(m):
      if data[i][j]:
        cnt = 0
        target = data[i][j]
        erase(i, j, target)
        if cnt != 0: flag = False
        ans -= (cnt * target)
        tot_cnt -= cnt

  if ans == 0: break
  if flag:
    avg = ans / tot_cnt
    for i in range(1, n+1):
      for j in range(m):
        if data[i][j] and data[i][j] > avg:
          data[i][j] -= 1
          ans -= 1
        elif data[i][j] and data[i][j] < avg:
          data[i][j] += 1
          ans += 1

print(ans)
