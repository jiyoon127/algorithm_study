from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  l, i = map(int, input().split())
  prints = deque(list(map(int, input().split())))
  count = 0
  while prints:
    top = max(prints)
    i -= 1
    pop = prints.popleft()
    if top == pop:
      count += 1
      l -= 1
      if i == -1:
        print(count)
        break
    else:
      prints.append(pop)
      if i == -1:
        i += l
