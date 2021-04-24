import sys
input = sys.stdin.readline
_min = [sys.maxsize] * 2 + [1, 7, 4, 2, 6, 8, 10] + [int(sys.maxsize)] * 92
add = [1, 7, 4, 2, 0, 8]

for i in range(9, 101):
    for j in range(2, 8):
        cur = str(_min[i - j]) + str(add[j - 2])
        _min[i] = min(_min[i], int(cur))

for _ in range(int(input())):
    n = int(input())

    if n % 2 == 1: _max = int(str(7) + str(1) * ((n - 3) // 2))
    else: _max = int(str(1) * (n // 2))
    print(_min[n], _max)
