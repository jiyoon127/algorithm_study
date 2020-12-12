import sys
input = sys.stdin.readline
n = int(input())
weights = list(map(int, input().split()))
weights.sort()
cur_max = 1
for i in weights:
  if cur_max < i: break
  cur_max += i

print(cur_max)
