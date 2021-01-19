from collections import Counter
import sys
inptut = sys.stdin.readline

seconds = 0
a = []
r, c, k = map(int, input().split())
for _ in range(3):
  a.append(list(map(int, input().split())))

while seconds <= 100:
  c_cal = False
  if r <= len(a) and c <= len(a[0]) and a[r-1][c-1] == k: break
  if len(a) < len(a[0]):
    c_cal = True
    a = list(zip(*a))
  
  new_a = []
  max_len = 0
  for row in a:
    counter = Counter(row)
    if counter[0]: del counter[0]
    temp = list(map(list, counter.items()))
    temp.sort(key = lambda x: (x[1],x[0]))
    new_a.append(list(sum(temp, []))[:100])
    max_len = max(max_len, len(new_a[-1]))
    
  for i in range(len(new_a)):
    if len(new_a[i]) < max_len:
      new_a[i] += [0] * (max_len - len(new_a[i]))
  
  a = new_a

  if c_cal: a = list(zip(*a))
  seconds += 1
print(seconds if seconds <= 100 else -1)
