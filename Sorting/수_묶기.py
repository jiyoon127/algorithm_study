import sys
input = sys.stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]
plus = list(filter(lambda x: x > 0, data))
minus = list(filter(lambda x: x <= 0, data))
result = 0
plus.sort(reverse=True)
minus.sort()

def get_sum(datas):
  sum = 0
  temp = 0
  for i, num in enumerate(datas):
    if i %2 == 0:
      temp = num
    if i %2 == 1:
      if 1 in (num, temp):
        temp += num
      else :
        temp *= num
      sum += temp
  if len(datas) %2 == 1:
    sum += temp
  return sum

result = get_sum(plus) + get_sum(minus)
print(result)
