import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
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
