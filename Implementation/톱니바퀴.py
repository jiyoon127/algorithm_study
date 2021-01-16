from collections import deque
import sys
input = sys.stdin.readline

def turn(target, direct):
  if direct == -1:
    wheels[target-1].append(wheels[target-1].popleft())
  else:
    wheels[target-1].appendleft(wheels[target-1].pop())

def turn_nei(target, direct, nei):
  if nei > 4 or nei < 1: return
  if target < nei and wheels[target - 1][2] != wheels[nei - 1][6]:
    turn_nei(nei, -direct, nei + 1)
    turn(nei, direct)
  if target > nei and wheels[target - 1][6] != wheels[nei - 1][2]:
    turn_nei(nei, -direct, nei - 1)
    turn(nei, direct)

wheels = []
for _ in range(4):
  wheels.append(deque(map(int,input().rstrip())))

k = int(input())
for i in range(k):
  target, direct = map(int, input().split())
  turn_nei(target, -direct, target + 1)
  turn_nei(target, -direct, target - 1) 
  turn(target, direct)

ans = 0
for i in range(4):
  ans += wheels[i][0] * (2**i)
print(ans)
