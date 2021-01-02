from collections import Counter
n, m = map(int, input().split())
balls = list(map(int, input().split()))
counter = Counter(balls)
left_balls = len(balls)
result = 0
if m == 1:
  print(0)
for i in counter.keys():
  cur_ball = counter[i]
  left_balls -= cur_ball
  result += cur_ball * left_balls
print(result)
