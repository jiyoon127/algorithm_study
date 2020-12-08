n = 1000 - int(input())
c_type = [500, 100, 50, 10, 5, 1]
count = 0

for coin in c_type:
  count += n // coin
  n %= coin

print(count)
