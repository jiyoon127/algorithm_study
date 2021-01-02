s = input()
result = int(s[0])
for n in s[1:]:
  if result not in (0,1) and int(n) not in (0, 1):
    result *= int(n)
  else: result += int(n)
print(result)
