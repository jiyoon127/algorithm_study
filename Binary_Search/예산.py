import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
max_budget = int(input())
start = 0
end = max(budgets)

result = 0
while(start <= end):
  total = 0
  mid = (start + end) //2
  for x in budgets:
    if x > mid: total += mid
    else: total += x

  if total <= max_budget:
    result = mid
    start = mid + 1
  else: end = mid - 1
print(result)
