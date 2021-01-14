import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]
visited = [False] * n
data = []

def dfs(length):
  if length == m:
    print(*data)
    return
  for i in range(n):
    if visited[i]: continue
    visited[i] = True
    data.append(nums[i])
    dfs(length + 1)
    data.pop()
    for j in range(i + 1, n):
      visited[j] = False

dfs(0)
