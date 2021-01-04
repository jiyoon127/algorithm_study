import sys
input = sys.stdin.readline

n = int(input())
coins = list(map(int, input().split()))
target = 1
coins.sort()

for coin in coins:
  if target < coin: break
  target += coin

print(target)
