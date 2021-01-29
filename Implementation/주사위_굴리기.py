import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m, x, y, k = map(int, input().split())
graph = []
dice_r = [0] * 4
dice_c = [0] * 4
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for _ in range(n):
  graph.append(list(map(int, input().split())))
moves = list(map(int, input().split()))

def moveDice(direct):
  global dice_r, dice_c
  if direct == 1:
    dice_r = dice_r[-1:] + dice_r[:-1]
    dice_c[1] = dice_r[1]
    dice_c[3] = dice_r[3]
  elif direct == 2:
    dice_r = dice_r[1:] + dice_r[:1]
    dice_c[1] = dice_r[1]
    dice_c[3] = dice_r[3]
  elif direct == 3:
    dice_c = dice_c[1:] + dice_c[:1]
    dice_r[1] = dice_c[1]
    dice_r[3] = dice_c[3]
  else:
    dice_c = dice_c[-1:] + dice_c[:-1]
    dice_r[1] = dice_c[1]
    dice_r[3] = dice_c[3]

def simulate(x, y, i):
  global dice
  if i == k: return

  direct = moves[i]
  nx = x + dx[direct]
  ny = y + dy[direct]

  if 0 <= nx < n and 0 <= ny < m:
    moveDice(direct)
    if graph[nx][ny] == 0:
      graph[nx][ny] = dice_r[3]
    else: 
      dice_r[3] = graph[nx][ny]
      dice_c[3] = graph[nx][ny]
      graph[nx][ny] = 0
    print(dice_r[1])
    simulate(nx, ny, i+1)
  else: simulate(x, y, i+1)

simulate(x, y, 0)
