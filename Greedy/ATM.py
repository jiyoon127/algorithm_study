n = int(input())
people = list(map(int, input().split()))
people.sort()
min_time = 0

for i in range(n):
  min_time += people[i] * (n - i)
print(min_time)
