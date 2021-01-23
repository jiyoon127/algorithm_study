from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0] * 2 * n)
stage = 0

while belt.count(0) < k:
  stage += 1
  belt.rotate(1)
  robots.rotate(1)
  robots[n-1] = 0

  for i in range(n - 2, -1, -1):
    if robots[i] and robots[i + 1] == 0 and belt[i + 1] >= 1:
      robots[i] = 0
      belt[i + 1] -= 1
      if i + 1 == n - 1:
        robots[i + 1] = 0
        continue
      robots[i + 1] = 1

  if belt[0] >= 1:
    robots[0] = 1
    belt[0] -= 1

print(stage)
