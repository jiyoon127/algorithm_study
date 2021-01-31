import sys
input = sys.stdin.readline

n = int(input())
classroom = list(map(int, input().split()))
b, c = map(int, input().split())

for i in range(n):
    if classroom[i] - b > 0:
        n += (classroom[i] - b) // c
        if (classroom[i] - b) % c: n += 1
print(n)
