s = input()
prev = s[0]
cnt = [0, 0]
cnt[int(prev)] = 1
for n in s[1:]:
  if prev == n:
    continue
  else: 
    cnt[int(n)] += 1
    prev = n
print(min(cnt))
