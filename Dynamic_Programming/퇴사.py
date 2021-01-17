import sys
input = sys.stdin.readline

n = int(input())
schedule = []
d = [0] * 16

for _ in range(n):
  schedule.append(list(map(int, input().split())))

for i in reversed(range(n)):
  time, pay = schedule[i][0], schedule[i][1]
  if i + time > n:
   d[i] = d[i+1]
  else:
    d[i] = max(d[i + 1], pay + d[i + time])
print(d[0])
