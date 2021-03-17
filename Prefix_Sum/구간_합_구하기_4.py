import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
prefix_sum = [0]
sum = 0

for i in data:
    sum += i
    prefix_sum.append(sum)

for _ in range(m):
    left, right = map(int, input().split())
    print(prefix_sum[right] - prefix_sum[left - 1])
