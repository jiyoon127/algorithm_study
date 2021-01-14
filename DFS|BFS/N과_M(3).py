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
    data.append(nums[i])
    dfs(length + 1)
    data.pop()

dfs(0)
