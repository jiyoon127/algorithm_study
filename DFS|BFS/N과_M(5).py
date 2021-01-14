import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * n
data = []

def dfs(length):
  if length == m:
    print(*data)
    return
  for i in range(n):
    if visited[i]:
      continue
    visited[i] = True
    data.append(nums[i])
    dfs(length + 1)
    data.pop()
    visited[i] = False
dfs(0)
