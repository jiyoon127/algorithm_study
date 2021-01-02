n = int(input())
ppl = list(map(int, input().split()))
ppl.sort()
result = 0
cnt  = 0

for p in ppl:
  cnt += 1
  if cnt >= p:
    result += 1
    cnt = 0
print(result)
