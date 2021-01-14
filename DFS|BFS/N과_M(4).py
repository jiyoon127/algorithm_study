import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]
data = []

def dfs(length):
  if length == m:
    print(*data)
    return
  for i in range(n):
    if data and data[-1] > nums[i]:
      continue
    else: 
      data.append(nums[i])
      dfs(length + 1)
      data.pop()
dfs(0)
