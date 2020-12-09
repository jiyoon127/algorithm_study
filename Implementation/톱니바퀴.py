import sys
from collections import deque
input = sys.stdin.readline

def turn(start, direction, next_step):
  nei = start + next_step
  if nei > 4 or nei < 1: return
  if next_step == 1:
    if(gears[start - 1][2] != gears[nei - 1][6]):
      turn(nei, -direction, next_step)
      gears[nei - 1].rotate(direction)
  else:
    if(gears[start - 1][6] != gears[nei - 1][2]):
      turn(nei, -direction, next_step)
      gears[nei - 1].rotate(direction)

gears = []
score = 0
for _ in range(4):
  gears.append(deque(map(int, list(input().strip()))))
t = int(input())
for _ in range(t):
  start, direction = map(int, input().split())
  turn(start, -direction, 1)
  turn(start, -direction, -1)
  gears[start - 1].rotate(direction)

for i in range(4):
  score += (2**i) * gears[i][0]
print(score)
