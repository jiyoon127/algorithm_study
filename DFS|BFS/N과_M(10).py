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
    if visited[i] == 0 or (data and data[-1] > i): continue
    visited[i] -= 1
    data.append(i)
    dfs(length + 1)
    data.pop()
    visited[i] +=  1

dfs(0)
