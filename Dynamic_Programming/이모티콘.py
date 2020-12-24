import sys
input = sys.stdin.readline
s = int(input())
INF = int(1e9)
dp = [INF] * 1001
dp[1] = 0
for i in range(1, 1001):
  clip = i
  seconds = dp[i] + 1
  steps = 1
  while i + (steps * clip) < 1001:
    j = i + (steps * clip)
    dp[j] = min(dp[j], seconds + steps)
    for delete in range(1, clip):
      dp[j - delete] = min(dp[j - delete], dp[j] + delete)
    steps += 1
print(dp[s])
