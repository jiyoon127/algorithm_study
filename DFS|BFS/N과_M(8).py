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
    if visited[i]: continue
    data.append(nums[i])
    dfs(length + 1)
    visited[i] = True
    data.pop()
    for j in range(i+1, n):
      visited[j] = False

dfs(0)
