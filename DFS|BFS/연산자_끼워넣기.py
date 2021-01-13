# 백준 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = int(1e9)
max_val = -int(1e9)

def dfs(i, now):
  global min_val, max_val, add, sub, mul, div
  if i == n:
    min_val = min(min_val, now)
    max_val = max(max_val, now)
  else:
    if add > 0:
      add -= 1
      dfs(i+1, now + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i+1, now - data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i+1, now * data[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i+1, int(now / data[i]))
      div += 1

dfs(1, data[0])
print(max_val, min_val, end = '\n')
