import sys
input = sys.stdin.readline

s = input().rstrip()
num = 0
chars = []
for ch in s:
  if ch.isalpha():
    chars.append(ch)
  else:
    num += int(ch)

chars.sort()
for c in chars:
  print(c, end = '')
print(num)
