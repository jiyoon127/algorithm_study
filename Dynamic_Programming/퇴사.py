import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in reversed(range(n)):
    time, pay = data[i][0], data[i][1]
    if i + time > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], pay + dp[i + time])

print(dp[0])
