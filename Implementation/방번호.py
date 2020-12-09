import sys
number = sys.stdin.readline()[:-1]
counter = [0] * 9
for n in number:
  index = int(n)
  if index == 9: index = 6
  counter[index] += 1
counter[6] = (counter[6] + 1) // 2
print(max(counter))
