import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, count = int(input()), 1
  candid = sorted([list(map(int, input().split())) for x in range(n)])
  
  min = candid[0][1]

  for i in range(1, n):
    if candid[i][1] < min:
      min = candid[i][1]
      count += 1
  print(count)
