from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = Counter(nums)
data = []

def dfs(length):
  if length == m:
    print(*data)
    return
  for i in visited.keys():
    if data and data[-1] > i: continue
    data.append(i)
    dfs(length + 1)
    data.pop()

dfs(0)
