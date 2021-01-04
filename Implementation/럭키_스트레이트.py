import sys
input = sys.stdin.readline

n = input().rstrip()
middle = len(n)//2
left, right = 0,0
for i, num in enumerate(n):
  if i < middle: left += int(num)
  else: right += int(num)

print("LUCKY" if left == right else "READY")
